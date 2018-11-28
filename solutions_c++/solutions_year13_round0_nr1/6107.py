#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int checkColumn(char board[4][4], int j)
{
	if((board[0][j] == 'O' || board[0][j] == 'T')
		&& (board[1][j] == 'O' || board[1][j] == 'T')
		&& (board[2][j] == 'O' || board[2][j] == 'T')
		&& (board[3][j] == 'O' || board[3][j] == 'T'))
		return 1;

	if((board[0][j] == 'X' || board[0][j] == 'T')
		&& (board[1][j] == 'X' || board[1][j] == 'T')
		&& (board[2][j] == 'X' || board[2][j] == 'T')
		&& (board[3][j] == 'X' || board[3][j] == 'T'))
		return 2;

	return 3;
}

int checkRow(char board[4][4], int i)
{
	if((board[i][0] == 'O' || board[i][0] == 'T')
		&& (board[i][1] == 'O' || board[i][1] == 'T')
		&& (board[i][2] == 'O' || board[i][2] == 'T')
		&& (board[i][3] == 'O' || board[i][3] == 'T'))
		return 1;

	if((board[i][0] == 'X' || board[i][0] == 'T')
		&& (board[i][1] == 'X' || board[i][1] == 'T')
		&& (board[i][2] == 'X' || board[i][2] == 'T')
		&& (board[i][3] == 'X' || board[i][3] == 'T'))
		return 2;

	return 3;
}

int checkDiag(char board[4][4])
{
	if((board[0][0] == 'O' || board[0][0] == 'T')
		&& (board[1][1] == 'O' || board[1][1] == 'T')
		&& (board[2][2] == 'O' || board[2][2] == 'T')
		&& (board[3][3] == 'O' || board[3][3] == 'T'))
		return 1;

	if((board[0][3] == 'O' || board[0][3] == 'T')
		&& (board[1][2] == 'O' || board[1][2] == 'T')
		&& (board[2][1] == 'O' || board[2][1] == 'T')
		&& (board[3][0] == 'O' || board[3][0] == 'T'))
		return 1;

	if((board[0][0] == 'X' || board[0][0] == 'T')
		&& (board[1][1] == 'X' || board[1][1] == 'T')
		&& (board[2][2] == 'X' || board[2][2] == 'T')
		&& (board[3][3] == 'X' || board[3][3] == 'T'))
		return 2;

	if((board[0][3] == 'X' || board[0][3] == 'T')
		&& (board[1][2] == 'X' || board[1][2] == 'T')
		&& (board[2][1] == 'X' || board[2][1] == 'T')
		&& (board[3][0] == 'X' || board[3][0] == 'T'))
		return 2;

	return 3;
}

bool checkEnd(char board[4][4])
{
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(board[i][j] == '.')
				return false;
		}
	}
	return true;
}

void testTic(char board[4][4])
{
	for(int i = 0; i < 4; i++)
	{
		if(checkColumn(board, i) == 1 || checkRow(board, i) == 1 || checkDiag(board) == 1)
		{
			cout << "O won";
			return;
		}

		if(checkColumn(board, i) == 2 || checkRow(board, i) == 2 || checkDiag(board) == 2)
		{
			cout << "X won";
			return;
		}
	}

	if(checkEnd(board))
		cout << "Draw";
	else
		cout << "Game has not completed";
}

int main(int argc, char *argv[])
{
	ifstream input;
	input.open(argv[1]);
	if(!input.is_open())
	{
		cout << "Error Opening";
		return 0;
	}
	char add;
	int total;
	input >> total;
	char board[4][4];
	for(int count = 0; count < total; count++)
	{
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				input >> add;
				board[i][j] = add;
			}
		}
		cout << "Case #" << count + 1 << ": ";
		testTic(board);
		cout << endl;
	}
	
}