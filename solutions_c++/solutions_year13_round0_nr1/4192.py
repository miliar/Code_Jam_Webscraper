/*
 * tic_tac_toe_tomek.cpp
 *
 *  Created on: Apr 13, 2013
 *      Author: Matt
 */

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int scan_board(vector<string> board, char p)
{
	// Check for a horizontal win
	for(int i=0; i<4; i++)
	{
		if(board[i][0] == p || board[i][0] == 'T')
		{
			if(board[i][1] == p || board[i][1] == 'T')
			{
				if(board[i][2] == p || board[i][2] == 'T')
				{
					if(board[i][3] == p || board[i][3] == 'T')
					{
						return 1;
					}
				}
			}
		}
	}

	// Check for a vertical win
	for(int i=0; i<4; i++)
	{
		if(board[0][i] == p || board[0][i] == 'T')
		{
			if(board[1][i] == p || board[1][i] == 'T')
			{
				if(board[2][i] == p || board[2][i] == 'T')
				{
					if(board[3][i] == p || board[3][i] == 'T')
					{
						return 1;
					}
				}
			}
		}
	}

	// Check the diagonals
	if(board[0][0] == p || board[0][0] == 'T')
	{
		if(board[1][1] == p || board[1][1] == 'T')
		{
			if(board[2][2] == p || board[2][2] == 'T')
			{
				if(board[3][3] == p || board[3][3] == 'T')
				{
					return 1;
				}
			}
		}
	}

	if(board[0][3] == p || board[0][3] == 'T')
	{
		if(board[1][2] == p || board[1][2] == 'T')
		{
			if(board[2][1] == p || board[2][1] == 'T')
			{
				if(board[3][0] == p || board[3][0] == 'T')
				{
					return 1;
				}
			}
		}
	}

	return 0;
}

int completed(vector<string> board)
{
	for(int i=0; i<4; i++)
	{
		for(int j=0; j<4; j++)
		{
			if(board[i][j] == '.')
			{
				return 0;
			}
		}
	}
	return 1;
}

int main()
{
	int num_cases;
	cin >> num_cases;

	ofstream out;
	out.open("answer_small.txt");

	for(int i=1; i<=num_cases; i++)
	{
		vector<string> board(4);
		for(int j=0; j<4; j++)
		{
			cin >> board[j];
		}

		out << "Case #" << i << ": ";
		if(scan_board(board, 'X') == 1)
		{
			out << "X won" << endl;
		}
		else if(scan_board(board, 'O') == 1)
		{
			out << "O won" << endl;
		}
		else if(completed(board))
		{
			out << "Draw" << endl;
		}
		else
		{
			out << "Game has not completed" << endl;
		}
	}

	out.close();
}
