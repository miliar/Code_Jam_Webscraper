#include <QFile>
#include <QTextStream>
#include <QStringList>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1

//idea:  because all integers in the array are different, let's just output the number of integers, which are on wrong positions

QFile inFile("C:/CodeJam0d/test.in");
QFile outFile("C:/CodeJam0d/output.txt");


int main(int argc, char *argv[])
{
	inFile.open(QFile::ReadOnly);
	outFile.open(QFile::WriteOnly);
	QTextStream inData(&inFile);
	QTextStream outData(&outFile);

	int T;
	inData >> T;

	for(int t=0; t<T; t++)
	{
		int N;
		inData >> N;

		int tValue;
		QList<int> gorosArray, sortedArray;
		for(int n=0; n<N; n++)
		{
			inData >> tValue;
			gorosArray.append(tValue);
		}

		sortedArray = gorosArray;
		qSort(sortedArray);

		int diff=0;
		for(int i=0; i<gorosArray.count(); i++)
			if(gorosArray[i]!=sortedArray[i]) diff++;

		outData << QString("Case #%1: %2").arg(t+1).arg((double)diff,0,'f',6);
		outData << "\r\n";
	}
}