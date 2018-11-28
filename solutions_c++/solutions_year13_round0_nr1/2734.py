#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

bool playerWon(char x, string board[])
{
	int row, col, d1, d2;

	d1 = d2 = 0;
	for (int i = 0; i < 4; i++)
	{
		row = 0;
		col = 0;
		for (int j = 0; j < 4; j++)
		{
			if (board[i][j] == x) row++;
			if (board[j][i] == x) col++;
		}

		if ((row == 4) || (col == 4)) return true;

		if (board[i][i] == x) d1++;
		if (board[i][3-i] == x) d2++;
	}

	if ((d1 == 4) || (d2 == 4)) return true;

	return false;
}


string	solve(string board[])
{
	bool game_ended = true;
	int  t_row = -1, t_col = -1;

	for (int  i = 0; i < 4; i++)
	{
		if (board[i].find('.') != -1) game_ended = false;

		if (t_row == -1)
		{
			t_col = board[i].find('T');

			if (t_col != -1) t_row = i;
		}
	}

	if (t_row != -1) board[t_row][t_col] = 'X';
	if (playerWon('X', board)) return string("X won");

	if (t_row != -1) board[t_row][t_col] = 'O';
	if (playerWon('O', board)) return string("O won");

	if (game_ended) return string("Draw");

	return string("Game has not completed");
}


int main()
{
	fstream 	f, g;
	int			tests;
	string		board[4];

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> tests;
	for (int k = 1; k <= tests; k++)
	{
		for (int i = 0; i < 4; i++)
		{
			f >> board[i];
		}

		g << "Case #" << k << ": " << solve(board) << endl;
	}

	f.close();
	g.close();

	return 0;
}
