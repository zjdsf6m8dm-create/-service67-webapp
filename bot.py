import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


WEB_APP_URL = "https://zjdsf6m8dm-create.github.io/-service67-webapp/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🛍 Ouvrir la boutique",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    await update.message.reply_text(
        "Bienvenue sur SERVICE67SHOPP 👋\n\n"
        "Clique sur le bouton ci-dessous pour ouvrir la boutique.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    token = os.environ["BOT_TOKEN"]

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    app.run_polling()


if __name__ == "__main__":
    main()