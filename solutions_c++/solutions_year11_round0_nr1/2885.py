
#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QString>
#include <QList>
#include <QStringList>
#include "Bot.h"

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	QList<int> results;

	QFile file("C:\\input.txt");
	if(file.open(QIODevice::ReadOnly))
	{
		QTextStream textStream(&file);
		QString line = textStream.readLine();
		QStringList processedLine;
		while(!(line = textStream.readLine()).isNull())
		{
			Bot* orangeBot = new Bot();
			Bot* blueBot = new Bot();
			QList<bool> orangeTurn;
			int time = 0;
			processedLine = line.split(" ");
			for(int i=1;i<processedLine.size();i++)
			{
				if(processedLine.value(i) == "O")
				{
					i++;
					orangeBot->addButton(processedLine.value(i).toInt());
					orangeTurn.append(true);
				}
				else
				{
					i++;
					blueBot->addButton(processedLine.value(i).toInt());
					orangeTurn.append(false);
				}
			}
			for(int j=0;j<orangeTurn.size();j++)
			{
				bool turncompleted = false;
				if(orangeTurn.value(j))
				{
					orangeBot->setTurn(true);
					blueBot->setTurn(false);
					while(!turncompleted)
					{
						turncompleted = orangeBot->performAction();
						blueBot->performAction();
						time++;
					}
				}
				else
				{
					orangeBot->setTurn(false);
					blueBot->setTurn(true);
					while(!turncompleted)
					{
						orangeBot->performAction();
						turncompleted = blueBot->performAction();
						time++;
					}
				}
			}
			results.append(time);
			
			delete orangeBot;
			delete blueBot;
		}
		file.close();
	}

	QFile data("output.txt");
	if (data.open(QFile::WriteOnly | QFile::Truncate)) {
		QTextStream out(&data);
		for(int i=0;i<results.size();i++)
		{
			out << "Case #" << i+1 << ": " << results.value(i) << "\r\n";
		}
		data.close();
	}

	return a.exec();
}
