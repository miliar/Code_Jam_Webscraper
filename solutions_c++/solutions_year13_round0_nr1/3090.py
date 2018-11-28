#include <QFile>
#include <QTextStream>
#include <QStringList>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1


QFile inFile("C:/CodeJam0a/A-small-attempt1.in");
QFile outFile("C:/CodeJam0a/output.txt");

char matrix[4][4];

bool DidPlayerWin(char playerSymb)
{
	int i,j;

	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			if( (matrix[i][j]!=playerSymb) && (matrix[i][j]!='T') ) break;
		}

		if(j==4) return 1;
	}

	for(j=0; j<4; j++)
	{
		for(i=0; i<4; i++)
		{
			if( (matrix[i][j]!=playerSymb) && (matrix[i][j]!='T') ) break;
		}

		if(i==4) return 1;
	}

	for(i=0; i<4; i++)
	{
		if( (matrix[i][i]!=playerSymb) && (matrix[i][i]!='T') ) break;
	}
	if(i==4) return 1;

	for(i=0; i<4; i++)
	{
		if( (matrix[i][3-i]!=playerSymb) && (matrix[i][3-i]!='T') ) break;
	}
	if(i==4) return 1;

	return 0;
}

bool NoMoreEmptyCells()
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(matrix[i][j]=='.') return 0;
		}
	}

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
		char spaceSymb;
		for(int i=0; i<4; i++)
		{
			inData >> spaceSymb;
			//inData >> spaceSymb;
			for(int j=0; j<4; j++) 
			{
				inData >> matrix[i][j];
			}
		}
		inData >> spaceSymb;
		//inData >> spaceSymb;

		outData << QString("Case #%1: ").arg(t+1);

		if( DidPlayerWin('X') )				outData << "X won\r\n";
		else if( DidPlayerWin('O') )		outData << "O won\r\n";
		else if( NoMoreEmptyCells() )		outData << "Draw\r\n";
		else								outData << "Game has not completed\r\n";
	}
}
