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
			QList<QString> combined;
			QList<QString> opposed;
			QString combinations;
			processedLine = line.split(" ");
			int nrOfCombined = processedLine.value(0).toInt();
			int i=1;
			while(nrOfCombined>0)
			{
				combined.append(processedLine.value(i));
				nrOfCombined--;
				i++;
			}
			int nrOfOpposed = processedLine.value(i).toInt();
			i++;
			while(nrOfOpposed>0)
			{
				opposed.append(processedLine.value(i));
				nrOfOpposed--;
				i++;
			}
			i++;
			QString sequence = processedLine.value(i);
			combinations.append(sequence.at(0));
			for(int j=1;j<sequence.size();j++)
			{
				QChar newElement = sequence.at(j);
				combinations.append(newElement);
				bool wasrecombined = false;
				foreach(QString combination, combined)
				{
					if(combinations.size()>1)
					{
						if(combination.at(0)==newElement && (combination.at(1)==combinations.at(combinations.size()-2)))
						{
							combinations.remove(combinations.size()-2,2);
							combinations.append(combination.at(2));
							wasrecombined = true;
						}
						else if(combination.at(1)==newElement && (combination.at(0)==combinations.at(combinations.size()-2)))
						{
							combinations.remove(combinations.size()-2,2);
							combinations.append(combination.at(2));
							wasrecombined = true;
						}
					}
				}
				if(wasrecombined) continue;
				foreach(QString opposing, opposed)
				{
					if((opposing.at(0)==newElement)&&(combinations.contains(opposing.at(1))))
					{
						combinations.clear();
					}
					else if((opposing.at(1)==newElement)&&(combinations.contains(opposing.at(0))))
					{
						combinations.clear();
					}
				}
			}
			results.append(combinations);


						
		}
		file.close();
	}

	QFile data("output.txt");
	if (data.open(QFile::WriteOnly | QFile::Truncate)) {
		QTextStream out(&data);
		for(int i=0;i<results.size();i++)
		{
			QString result = "[";
			for(int k=0;k<results.value(i).size();k++)
			{
				result.append(results.value(i).at(k));
				result.append(", ");
			}
			if(result.size()>1) result.remove(result.size()-2,2);
			result.append("]");
			out << "Case #" << i+1 << ": " << result << "\r\n";
		}
		data.close();
	}

	return a.exec();
}
