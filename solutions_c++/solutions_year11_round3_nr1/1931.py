#include <iostream>



using namespace std;
char blu = '#';
char wht = '#';

char redLeftTop = '/';
char redrightTop = '\\';
char redrightBot = '/';
char redLeftBot = '\\';



bool repTile(char** tileArr , int row , int col , int curBluRowInx , int curBluColInx)
{
	int topLeftRowInx = curBluRowInx;
	int topLeftColInx = curBluColInx;

	int topRgtRowInx = topLeftRowInx;  
	int topRgtColInx = topLeftColInx + 1;

	int botLeftRowInx = topLeftRowInx + 1;
	int botLeftColInx = topLeftColInx;

	int botRgtRowInx = botLeftRowInx;  
	int botRgtColInx = botLeftColInx + 1;

	if(botRgtRowInx >= row || botRgtColInx >= col)
		return false;

	char topLeftChar = tileArr[topLeftRowInx][topLeftColInx];
	char topRghtChar = tileArr[topRgtRowInx][topRgtColInx];
	char botLeftChar = tileArr[botLeftRowInx][botLeftColInx];
	char botRghtChar = tileArr[botRgtRowInx][botRgtColInx];

	if(topLeftChar == blu)
		tileArr[topLeftRowInx][topLeftColInx] = redLeftTop;
	else 
		return false;


	if(topRghtChar == blu)
		tileArr[topRgtRowInx][topRgtColInx] = redrightTop;
	else 
		return false;


	if(botLeftChar == blu)
		tileArr[botLeftRowInx][botLeftColInx] = redLeftBot;
	else 
		return false;


	if(botRghtChar == blu)
		tileArr[botRgtRowInx][botRgtColInx] = redrightBot;
	else 
		return false;


	return true;

}

bool getRes(char** tileArr , int row , int col)
{
	for(int rowNum = 0 ; rowNum < row; rowNum++)
	{
		for(int colNum = 0 ; colNum < col; colNum++)
		{
			char curChar = tileArr[rowNum][colNum];
			if(curChar == blu)
			{
				if(repTile(tileArr,row,col,rowNum,colNum) == false)
					return false;
			}
		}
		
	}
	return true;
}

int main()
{
	int testCase;
	cin >> testCase;
	for(int caseNum = 1; caseNum <= testCase; caseNum++)
	{
		int row,  col;
		cin >> row;
		cin >> col;
		char* rowArr = new char[row];
		char* colArr = new char[col];


		char **tileArray = 0;

		//memory allocated for elements of rows.
		tileArray = new char *[row] ;

		for(int rowNum = 0 ; rowNum < row; rowNum++)
		{
			tileArray[rowNum] = new char[col]; 	 
			for(int colNum = 0 ; colNum < col; colNum++)
			{
				char curTile;
				cin >> curTile;
				tileArray[rowNum][colNum] = curTile;
			}
		}
		

		cout << "Case #" << caseNum << ":" << endl;

		if(getRes(tileArray , row ,col))
		{
			for(int rowNum = 0 ; rowNum < row; rowNum++)
			{
				for(int colNum = 0 ; colNum < col; colNum++)
				{
					cout << tileArray[rowNum][colNum];
				}
				cout << endl;
			}
		}
		else 
		{
			cout << "Impossible" << endl;
		}

		for( int i = 0 ; i < row ; i++ )
			delete [] tileArray[i] ;
	
		delete [] tileArray ;
		

	}

}

