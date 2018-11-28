#include <iostream>
#include <string>
using namespace std;

char board[4][5];

bool hasDiag1(char c)
{
	for (int i = 0; i < 4; ++i)
	{
		if (board[i][i] != c && board[i][i] != 'T')
			return false;
	}
	return true;
}
bool hasDiag2(char c)
{
	for (int i = 0; i < 4; ++i)
	{
		if (board[3-i][i] != c && board[3-i][i] != 'T')
			return false;
	}
	return true;
}
bool hasRow(char c, int row)
{
	for (int i = 0; i < 4; ++i)
	{
		if (board[row][i] != c && board[row][i] != 'T')
			return false;
	}
	return true;
}
bool hasCol(char c, int col)
{
	for (int i = 0; i < 4; ++i)
	{
		if (board[i][col] != c && board[i][col] != 'T')
			return false;
	}
	return true;
}
bool hasWon(char c)
{
	if (hasDiag1(c) || hasDiag2(c))
		return true;
	for (int i = 0; i < 4; ++i)
	{
		if (hasRow(c, i) || hasCol(c, i))
			return true;
	}
	return false;
}
bool boardFilled()
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			if (board[i][j] == '.')
				return false;
		}
	}
	return true;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		for (int i = 0; i < 4; ++i)
			cin >> board[i];
		cout << "Case #" << t+1 << ": ";
		if (hasWon('X'))
			cout << "X won";
		else if (hasWon('O'))
			cout << "O won";
		else if (boardFilled())
			cout << "Draw";
		else
			cout << "Game has not completed";
		cout << endl;
	}
	return 0;
}
