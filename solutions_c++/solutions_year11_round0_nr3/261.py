#include <QFile>
#include <QTextStream>
#include <QStringList>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1

//idea:  there must be even number of 1s in every bit of values, otherwise it's easy to see that we will not be able to split values to make equal XORs
//       so XOR of all values needs to be ==0, but if so, we can split candies in any random way and both XORs will still be the same,
//		 so, if Sean wants to have maximum, let's give Patrick just one smallest candy (I would cry...)


QFile inFile("C:/CodeJam0c/test.in");
QFile outFile("C:/CodeJam0c/output.txt");


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

		int realSum=0, patricksSum=0;
		int tValue;
		int minValue = 9999999;
		for(int n=0; n<N; n++)
		{
			inData >> tValue;
			if(tValue < minValue) minValue = tValue;

			realSum += tValue;
			patricksSum ^= tValue;
		}

		if(patricksSum!=0)	outData << QString("Case #%1: NO").arg(t+1);
		else				outData << QString("Case #%1: %2").arg(t+1).arg(realSum-minValue);

		outData << "\r\n";
	}
}