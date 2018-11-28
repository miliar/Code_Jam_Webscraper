//
// Problem A. Tic-Tac-Toe-Tomek
// Author: Tom Richards
// Remarks: Brute force method
//

#include <iostream>
#include <string.h>
using namespace std;

bool xwon;
bool owon;
bool blankSpaces;

char board[4][4];
char oboard[4][4];
char xboard[4][4];

void checkXGame()
{
	//rows
	for(int i=0; i < 4; i++)
	{
		if(strncmp(xboard[i], "XXXX", 4) == 0)
		{
			xwon = true;
			//gameComplete = true;
		}
	}

	//columns
	for(int col=0; col<4; col++)
	{
		int colCount = 0;
		for(int row=0; row < 4; row++)
		{
			if(xboard[row][col] == 'X')
				colCount++;
		}

		if(colCount == 4)
		{
			xwon = true;
			//gameComplete = true;
		}
	}

	//diagonal
	if(xboard[0][0] == 'X' && xboard[1][1] == 'X' && xboard[2][2] == 'X' && xboard[3][3] == 'X')
	{
		xwon = true;
		//gameComplete = true;
	}
	
	if(xboard[0][3] == 'X' && xboard[1][2] == 'X' && xboard[2][1] == 'X' && xboard[3][0] == 'X')
	{
		xwon = true;
		//gameComplete = true;
	}
}

void checkOGame()
{
	//rows
	for(int i=0; i < 4; i++)
	{
		if(strncmp(oboard[i], "OOOO", 4) == 0)
		{
			owon = true;
			//gameComplete = true;
		}
	}

	//columns
	for(int col=0; col<4; col++)
	{
		int colCount = 0;
		for(int row=0; row < 4; row++)
		{
			if(oboard[row][col] == 'O')
				colCount++;
		}

		if(colCount == 4)
		{
			owon = true;
			//gameComplete = true;
		}
	}

	//diagonal
	if(oboard[0][0] == 'O' && oboard[1][1] == 'O' && oboard[2][2] == 'O' && oboard[3][3] == 'O')
	{
		owon = true;
		//gameComplete = true;
	}

	if(oboard[0][3] == 'O' && oboard[1][2] == 'O' && oboard[2][1] == 'O' && oboard[3][0] == 'O')
	{
		owon = true;
		//gameComplete = true;
	}
}

void setupXGame()
{
	memcpy(xboard, board, sizeof(board));
	for(int i=0; i < 4; i++)
	{
		for(int j=0; j < 4; j++)
		{
			if(xboard[i][j] == 'T')
				xboard[i][j] = 'X';
		}
	}
}

void setupOGame()
{
	memcpy(oboard, board, sizeof(board));
	for(int i=0; i < 4; i++)
	{
		for(int j=0; j < 4; j++)
		{
			if(oboard[i][j] == 'T')
				oboard[i][j] = 'O';
		}
	}
}

void checkBlanks()
{
	for(int i=0; i < 4; i++)
	{
		for(int j=0; j < 4; j++)
		{
			if(board[i][j] == '.')
				blankSpaces = true;
		}
	}
}

int main()
{
	int numCases = 0;
	cin >> numCases;

	for(int c=1; c<= numCases; c++)
	{
		xwon = false;
		owon = false;
		blankSpaces = false;

		memset(xboard, 0, sizeof(xboard));
		memset(oboard, 0, sizeof(oboard));
		memset(board, 0, sizeof(board));

		//read board
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin >> board[i][j];
			}
		}

		//determine state
		setupOGame();
		setupXGame();
		checkOGame();
		checkXGame();
		checkBlanks();

		cout << "Case #" << c << ": ";

		if(xwon)
			cout << "X won";
		else if(owon)
			cout << "O won";
		else if(blankSpaces)
			cout << "Game has not completed";
		else 
			cout << "Draw";

		cout << endl;
	}
	
	return 0;
}