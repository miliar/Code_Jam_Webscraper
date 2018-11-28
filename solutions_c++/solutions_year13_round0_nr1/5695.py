#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
using namespace std;

char board[5][5];

int checkBoard()
{
	for (int i = 0; i <4; i++)
	{
		char symbol = board[i][0];
		int start = 1;
		if (symbol == '.')
			continue;
		if (symbol == 'T')
		{
			symbol = board[i][1];
			start = 2;
		}
		bool win = true;
		for (int j = start; j < 4; j++)
			if (board[i][j] != symbol && board[i][j] != 'T')
				win = false;
		if (win)
		{
			if (symbol == 'X') return 1;
			else return 2;
		}
	}

	for (int i = 0; i < 4; i++)
	{
		char symbol = board[0][i];
		int start = 1;
		if (symbol == '.')
			continue;
		if (symbol == 'T')
		{
			symbol = board[1][i];
			start = 2;
		}
		bool win = true;
		for (int j = start; j < 4; j++)
			if (board[j][i] != symbol && board[j][i] != 'T')
				win = false;
		if (win)
		{
			if (symbol == 'X') return 1;
			else return 2;
		}
	}
	string diag = "";
	for (int i = 0; i < 4; i++) diag += board[i][i];
	char symbol = diag[0];
	int start = 1;
	if (symbol != '.')
	{
		if (symbol == 'T') symbol = diag[1], start = 2;
		bool win = true;
		for (int i = start; i < 4; i++) 
			if (diag[i] != symbol && diag[i] != 'T')
				win = false;
		if (win)
		{
			if (symbol == 'X') return 1;
			else return 2;
		}
	}
	diag = "";
	for (int i = 0; i < 4; i++) diag += board[i][3 - i];
	symbol = diag[0];
	start = 1;
	if (symbol != '.')
	{
		if (symbol == 'T') symbol = diag[1], start = 2;
		bool win = true;
		for (int i = start; i < 4; i++) 
			if (diag[i] != symbol && diag[i] != 'T')
				win = false;
		if (win)
		{
			if (symbol == 'X') return 1;
			else return 2;
		}
	}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (board[i][j] == '.')
				return 4;
	return 3;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("issabelle.out", "w", stdout);
	int cases = 1, _;
	scanf("%d", &_);
	while (_--)
	{
		for (int i = 0; i < 4; i++)
			scanf("%s", board[i]);
		int status = checkBoard();
		printf("Case #%d: ", cases++);
		switch (status)
		{
		case 1:
			puts("X won");
			break;
		case 2:
			puts("O won");
			break;
		case 3:
			puts("Draw");
			break;
		case 4:
			puts("Game has not completed");
			break;
		default:
			break;
		}
	}
	return 0;
}