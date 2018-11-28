#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char getWinner(char *board);
bool notFull(char *board);

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A_large.out");

	int cases;
	fin >> cases;
	for (int i=0; i<cases; ++i)
	{
		char board[16];
		for (int b=0; b<4; ++b)
		{
			for (int c=0; c<4; ++c)
			{
				fin >> board[4*b+c];
			}
		}

		char winner = getWinner(board);

		switch (winner)
		{
			case 'X':
				fout << "Case #" << i+1 << ": X won" << endl;
				break;
			case 'O':
				fout << "Case #" << i+1 << ": O won" << endl;
				break;
			default:
				if (notFull(board))
					fout << "Case #" << i+1 << ": Game has not completed" << endl;
				else
					fout << "Case #" << i+1 << ": Draw" << endl;
		}
	}

	return 0;
}

char getWinner(char *board)
{
	for (int i=0; i<4; ++i)
	{
		string row;
		row += board[4*i];
		row += board[4*i+1];
		row += board[4*i+2];
		row += board[4*i+3];
		if (row.find_first_not_of("XT") == -1)
			return 'X';
		if (row.find_first_not_of("OT") == -1)
			return 'O';

		string col;
		col += board[i];
		col += board[4+i];
		col += board[8+i];
		col += board[12+i];
		if (col.find_first_not_of("XT") == -1)
			return 'X';
		if (col.find_first_not_of("OT") == -1)
			return 'O';
	}

	string diag;
	diag += board[0];
	diag += board[5];
	diag += board[10];
	diag += board[15];
	if (diag.find_first_not_of("XT") == -1)
		return 'X';
	if (diag.find_first_not_of("OT") == -1)
		return 'O';

	diag = "";
	diag += board[3];
	diag += board[6];
	diag += board[9];
	diag += board[12];
	if (diag.find_first_not_of("XT") == -1)
		return 'X';
	if (diag.find_first_not_of("OT") == -1)
		return 'O';

	return ' ';
}

bool notFull(char *board)
{
	for (int a=0; a<4; ++a)
	{
		for (int b=0; b<4; ++b)
		{
			if (board[4*a+b] == '.')
				return true;
		}
	}
	return false;
}