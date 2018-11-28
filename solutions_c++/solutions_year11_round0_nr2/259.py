#include <QFile>
#include <QTextStream>
#include <QStringList>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1


QFile inFile("C:/CodeJam0b/test.in");
QFile outFile("C:/CodeJam0b/output.txt");


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
		QStringList formBasedElements;	// formBasedElements
		QList<char> formResults;
		QList<char> opposedElements;  //i and i+1 make one combination
		QList<char> currentList;

		char tChar, tChar2;
		int C;
		inData >> C;
		for(int i=0; i<C; i++)
		{
			inData >> tChar; //space
			inData >> tChar;
			inData >> tChar2;
			formBasedElements.append( QString("%1%2").arg(tChar).arg(tChar2) );
			formBasedElements.append( QString("%1%2").arg(tChar2).arg(tChar) );  //and reversed
			inData >> tChar;
			formResults.append(tChar);
			formResults.append(tChar); //the same result for the reversed combination
		}

		int D;
		inData >> D;
		for(int i=0; i<D; i++)
		{
			inData >> tChar; //space
			inData >> tChar;
			opposedElements.append(tChar);
			inData >> tChar;
			opposedElements.append(tChar);
		}

		int N;
		int tPos;
		inData >> N;
		inData >> tChar; //space
		int combResIndex;
		for(int i=0; i<N; i++)
		{
			inData >> tChar;
			if(currentList.count()==0)	//just add
			{
				currentList.append(tChar);
				continue;
			}

			//now try to combine last current list element with the new one
			combResIndex = formBasedElements.indexOf( QString("%1%2").arg(currentList.last()).arg(tChar) );
			if( combResIndex<0 ) currentList.append(tChar); //just add
			else currentList.last() = formResults[combResIndex];  //change the last one to the combination's result

			//now try to clear the list, trying to find combination of the last element with others 
			for(int tOppos=-1;;)
			{
				tOppos = opposedElements.indexOf(currentList.last(), tOppos+1);
				if(tOppos==-1) break; //no more combinations to check

				if((tOppos%2) == 0)	tChar2 = opposedElements[tOppos+1];	//find the second from the combination
				else				tChar2 = opposedElements[tOppos-1];

				tPos = currentList.indexOf(tChar2);
				if( (tPos>=0) && (tPos!=(currentList.count()-1)) )  //currentList contains the second element of the combination and it's not the last one
				{
					currentList.clear();
					break;
				}
			}
		}


		outData << QString("Case #%1: [").arg(t+1);
		for(int i=0; i<currentList.count(); i++)
		{
			outData << currentList[i];
			if(i!=(currentList.count()-1))  outData << ", ";
		}
		outData << "]\r\n";
	}
}