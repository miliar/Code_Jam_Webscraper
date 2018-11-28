/*
 * main.cpp
 *
 *  Created on: 2013-4-13
 *      Author: chenjd
 */

#include <iostream>
#include <fstream>

#define File

#ifdef File
#define cin fin
#define cout fout
#endif

using namespace std;

#define RIGHT 0
#define DOWN 1
#define RIGHT_DOWN 2
#define LEFT_DOWN 3
const int turn_i[4] = { 0, 1, 1, 1 };
const int turn_j[4] = { 1, 0, 1, -1 };

int FindSameCross(char board[][4], int x, int y, int forward);

int main()
{
	int T;
#ifdef File
	ifstream fin("A-large.in");
	ofstream fout("out.txt");
#endif
	cin >> T;
	int test_case;
	for (test_case = 1; test_case <= T; test_case++)
	{
		char board[4][4];
		int i, j;
		bool game_end = true;
		bool someone_win = false;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> board[i][j];
				if (board[i][j] == '.')
					game_end = false;
			}
		if (someone_win == false)
			for (i = 0; i < 4; i++)
			{
				if (FindSameCross(board, i, 0, RIGHT) == 1)
				{
					char begin = board[i][0];
					if (begin == 'T')
						begin = board[i + turn_i[RIGHT]][0 + turn_j[RIGHT]];
					cout << "Case #" << test_case << ": " << begin << " won" << endl;
					someone_win = true;
				}
			}

		if (someone_win == false)
			for (j = 0; j < 4; j++)
			{
				if (FindSameCross(board, 0, j, DOWN) == 1)
				{
					char begin = board[0][j];
					if (begin == 'T')
						begin = board[0 + turn_i[DOWN]][j + turn_j[DOWN]];
					cout << "Case #" << test_case << ": " << begin << " won" << endl;
					someone_win = true;
				}
			}

		if (someone_win == false)
		{
			if (FindSameCross(board, 0, 0, RIGHT_DOWN) == 1)
			{
				char begin = board[0][0];
				if (begin == 'T')
					begin = board[0 + turn_i[RIGHT_DOWN]][0 + turn_j[RIGHT_DOWN]];
				cout << "Case #" << test_case << ": " << begin << " won" << endl;
				someone_win = true;
			}
		}
		if (someone_win == false)
		{
			if (FindSameCross(board, 0, 3, LEFT_DOWN) == 1)
			{
				char begin = board[0][3];
				if (begin == 'T')
					begin = board[0 + turn_i[LEFT_DOWN]][3 + turn_j[LEFT_DOWN]];
				cout << "Case #" << test_case << ": " << begin << " won" << endl;
				someone_win = true;
			}
		}

		if (someone_win == false && game_end == true)
		{
			cout << "Case #" << test_case << ": Draw" << endl;
		}
		if (someone_win == false && game_end == false)
		{
			cout << "Case #" << test_case << ": Game has not completed" << endl;
		}
	}
#ifdef File
	fin.close();
	fout.close();
#endif
	return 0;
}

int FindSameCross(char board[][4], int x, int y, int forward)
{
	int i, j;
	int find_same = 1;
	char begin = board[x][y];
	if (begin == 'T')
		begin = board[x + turn_i[forward]][y + turn_j[forward]];
	if (begin == '.')
		return 0;

	for (i = x + turn_i[forward], j = y + turn_j[forward]; i >= 0 && i < 4 && j >= 0 && j < 4; i += turn_i[forward], j += turn_j[forward])
	{
		if (board[i][j] != begin && board[i][j] != 'T')
			break;
		else
			find_same++;
	}
	if (find_same == 4)
		return 1;
	else
		return 0;
}
