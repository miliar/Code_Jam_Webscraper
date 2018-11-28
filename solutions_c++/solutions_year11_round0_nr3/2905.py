#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>
#include <QString>
#include <QList>
#include <QStringList>


int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);
	QStringList results;
	QFile file("C:\\input.txt");
	if(file.open(QIODevice::ReadOnly))
	{
		QTextStream textStream(&file);
		QString line = textStream.readLine();
		QStringList processedLine;
		while(!(line = textStream.readLine()).isNull())
		{
			QList<int> numbers;
			line = textStream.readLine();
			processedLine = line.split(" ");
			foreach(QString number,processedLine)
			{
				numbers.append(number.toInt());
			}
			int xorResult = 0;
			int smallest = 1000001;
			int sum = 0;
			foreach(int number,numbers)
			{
				xorResult = xorResult ^ number;
				if(number<smallest) smallest = number;
				sum += number;
			}
			if(xorResult) results.append("NO");
			else
			{
				results.append(QString::number(sum-smallest));				
			}
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
