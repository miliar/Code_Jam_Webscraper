# include <fstream>
# include <iostream>
#define BOARDSIZE 4

using namespace std;
/*
char board[BOARDSIZE][BOARDSIZE]={ {'O','X','X','O'},
			  {'X','X','X','O'},
	          {'X','O','X','O'},
	          {'O','O','O','X'}
            };;
			*/

char board[BOARDSIZE][BOARDSIZE];

fstream fpIn,fpOut;

void checkBoard()
{
	int xRowCount[BOARDSIZE]={0},oRowCount[BOARDSIZE]={0},xColCount[BOARDSIZE]={0},oColCount[BOARDSIZE]={0};
	int xMajDiagCount=0,xMinDiagCount=0,oMajDiagCount=0,oMinDiagCount=0;
	
	int tCount=0,tColIndex=-1,tRowIndex=-1,dotCount=0;

	//preprocess - get count of X and O on the board
	for(int i=0;i<BOARDSIZE; i++)
	{
		for(int j=0;j<BOARDSIZE; j++)
		{
			//major diagnol
			if( i == j )
			{
				if(board[i][j] == 'X')
					xMajDiagCount++;
				else if(board[i][j] == 'O')
					oMajDiagCount++;
		
			}
			//minor diagnol
			if( i == (BOARDSIZE-j-1) )
			{
				if(board[i][j] == 'X')
					xMinDiagCount++;
				else if(board[i][j] == 'O')
					oMinDiagCount++;
			}

			if(board[i][j] == 'X')
			{
				xRowCount[i]++;
			    xColCount[j]++;
			}
			else if(board[i][j] == 'O')
			{
				oRowCount[i]++;
				oColCount[j]++;
			}
			else if(board[i][j] == 'T')
			{
				tCount++;
				tRowIndex = i;
				tColIndex = j;
			}
			else
				dotCount++;
		}
	}

	//check row and col
	for(int i=0;i<BOARDSIZE;i++)
	{
		//rows
		if( xRowCount[i] == 4 || (xRowCount[i] == 3 && tRowIndex == i) )
		{
			fpOut<<"X won";
			return;
		}
		if( oRowCount[i] == 4 || (oRowCount[i] == 3 && tRowIndex == i) )
		{
			fpOut<<"O won";
			return;
		}

		//cols
		if( xColCount[i] == 4 || (xColCount[i] == 3 && tColIndex == i) )
		{
			fpOut<<"X won";
			return;
		}
		if( oColCount[i] == 4 || (oColCount[i] == 3 && tColIndex == i) )
		{
			fpOut<<"O won";
			return;
		}

	}

	//check major diagnol
	if( xMajDiagCount == 4 || (( xMajDiagCount == 3 && (tColIndex == tRowIndex) && tCount!=0) ) )
	{
			fpOut<<"X won";
			return;
	}
	if( oMajDiagCount == 4 || (( oMajDiagCount == 3 && (tColIndex == tRowIndex) && tCount !=0) ) )
	{
			fpOut<<"O won";
			return;
	}

	//check minor diagnol
	if( xMinDiagCount == 4 || (( xMinDiagCount == 3 && (tColIndex == (tRowIndex-BOARDSIZE+1)) && tCount!=0) ) )
	{
			fpOut<<"X won";
			return;
	}
	if( oMinDiagCount == 4 || (( oMinDiagCount == 3 && (tColIndex == (tRowIndex-BOARDSIZE+1)) &&tCount!=0 ) ) )
	{
			fpOut<<"O won";
			return;
	}

	// check for other 2 scenarios
	if(dotCount > 0)
		fpOut<<"Game has not completed";
	else
		fpOut<<"Draw";
}

void readFile()
{
	char ch;
	int numOfTestCases;

	
	fpIn.open("C:\\Users\\pmalik\\Desktop\\A-small-attempt7.in",ios::in);
	fpOut.open("C:\\Users\\pmalik\\Desktop\\outputFile7.txt", ios::out);

	fpIn>>numOfTestCases;
	ch = fpIn.get();
	for(int i=1; i<=numOfTestCases; i++)
	{
		//read board input
		for(int j=0;j<BOARDSIZE;j++)
		{
			for(int k=0;k<BOARDSIZE;k++)
			{
				board[j][k]=fpIn.get();
			}
			ch = fpIn.get();
			
		}
        
		fpOut<<"Case #"<<i<<": ";
		//check board state
		checkBoard();
		if(i!=numOfTestCases)
		    fpOut<<"\n";

		ch = fpIn.get();
	}


	//close files
	fpIn.close();
	fpOut.close();
}


int main()
{
	readFile();

	char ch;
	cin>>ch;
	return 0;
}