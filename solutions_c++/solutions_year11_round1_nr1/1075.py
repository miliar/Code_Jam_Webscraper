#include <QFile>
#include <QTextStream>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1


QFile inFile("C:/CodeJam1a/A-large.in");
QFile outFile("C:/CodeJam1a/output.txt");

bool CheckIfPossibel(quint64 N, int Pd, int Pg)
{
	//first let's check if he really could play at least N games to reach exact Pd
		int a=Pd;
		int b=100;
		for(int n=100; n>1; n--)
		{
			if( ((a%n)==0) && ((b%n)==0) )
			{
				a /= n;
				b /= n;
			}
		}
		if(N<b) return 0;  //not possible to reach Pd

	if(Pd==Pg) return 1;
	
	if( Pg==0 ) return (Pd==0);
	if( Pg==100 ) return (Pd==100);

	return 1;
}

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
		quint64 N;
		inData >> N;
		int Pd, Pg;
		inData >> Pd;
		inData >> Pg;

		if( CheckIfPossibel(N,Pd,Pg) )	outData << QString("Case #%1: Possible").arg(t+1);
		else							outData << QString("Case #%1: Broken").arg(t+1);
		outData << "\r\n";
	}
}