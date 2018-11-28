// ALarge.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

#include "Helper.h"

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream read_file;
	ofstream write_file;

	write_file.open("C:\\Users\\Matthew\\Documents\\Visual Studio 2010\\Projects\\CodeJam\\Answers\\A-large-answers.txt");
	read_file.open("C:\\Users\\Matthew\\Documents\\Visual Studio 2010\\Projects\\CodeJam\\Data Sets\\A-large.in");
	
	CJ::Utils utils;

	int output;
	if (read_file.is_open()) 
	{
		int test_count;
		read_file >> test_count;

		for(int ii = 0; ii < test_count; ++ii)
		{
			char board[4][4];

			for(int rr = 0; rr < 4; ++rr)
			{
				for(int jj = 0; jj < 4; ++jj)
				{
					char c;
					read_file >> c;
					board[rr][jj] = c;
				}
			}

			bool done = false;

			//test X row win
			for(int rr = 0; rr < 4; ++rr)
			{
				int x_row_win = 0;
				for(int jj = 0; jj < 4; ++jj)
					if(board[rr][jj] == 'X' || board[rr][jj] == 'T') ++x_row_win;

				if(x_row_win == 4)
				{
					if(!done)
						write_file << "Case #" << ii + 1 << ": X won" << endl;
					
					done = true;
				}
			}

			//test X col win
			for(int rr = 0; rr < 4; ++rr)
			{
				int x_row_win = 0;
				for(int jj = 0; jj < 4; ++jj)
					if(board[jj][rr] == 'X' || board[jj][rr] == 'T') ++x_row_win;

				if(x_row_win == 4)
				{
					if(!done)
					write_file << "Case #" << ii + 1 << ": X won" << endl;
					
					done = true;
				}
			}

			//test X diagonal win
			if((board[0][3] == 'X' || board[0][3] == 'T') && (board[1][2] == 'X' || board[1][2] == 'T') &&
				(board[2][1] == 'X' || board[2][1] == 'T') && (board[3][0] == 'X' || board[3][0] == 'T'))
			{
				if(!done)
				write_file << "Case #" << ii + 1 << ": X won" << endl;
				
				done = true;
			}
			else if((board[0][0] == 'X' || board[0][0] == 'T') && (board[1][1] == 'X' || board[1][1] == 'T') &&
				(board[2][2] == 'X' || board[2][2] == 'T') && (board[3][3] == 'X' || board[3][3] == 'T'))
			{
				if(!done)
				write_file << "Case #" << ii + 1 << ": X won" << endl;
				
				done = true;
			}

			//test O row win
			for(int rr = 0; rr < 4; ++rr)
			{
				int x_row_win = 0;
				for(int jj = 0; jj < 4; ++jj)
					if(board[rr][jj] == 'O' || board[rr][jj] == 'T') ++x_row_win;

				if(x_row_win == 4)
				{
					if(!done)
					write_file << "Case #" << ii + 1 << ": O won" << endl;
					
					done = true;
				}
			}

			//test O col win
			for(int rr = 0; rr < 4; ++rr)
			{
				int x_row_win = 0;
				for(int jj = 0; jj < 4; ++jj)
					if(board[jj][rr] == 'O' || board[jj][rr] == 'T') ++x_row_win;

				if(x_row_win == 4)
				{
					if(!done)
					write_file << "Case #" << ii + 1 << ": O won" << endl;
					
					done = true;
				}
			}

			//test O diagonal win
			if((board[0][3] == 'O' || board[0][3] == 'T') && (board[1][2] == 'O' || board[1][2] == 'T') &&
				(board[2][1] == 'O' || board[2][1] == 'T') && (board[3][0] == 'O' || board[3][0] == 'T'))
			{
				if(!done)
				write_file << "Case #" << ii + 1 << ": O won" << endl;
				
				done = true;
			}
			else if((board[0][0] == 'O' || board[0][0] == 'T') && (board[1][1] == 'O' || board[1][1] == 'T') &&
				(board[2][2] == 'O' || board[2][2] == 'T') && (board[3][3] == 'O' || board[3][3] == 'T'))
			{
				if(!done)
				write_file << "Case #" << ii + 1 << ": O won" << endl;
				
				done = true;
			}

			for(int rr = 0; rr < 4; ++rr)
			{
				for(int jj = 0; jj < 4; ++jj)
				{
					if(board[rr][jj] == '.')
					{
						if(!done)
						write_file << "Case #" << ii + 1 << ": Game has not completed" << endl;
						
						done = true;
					}
				}
			}

			if(!done)
			write_file << "Case #" << ii + 1 << ": Draw" << endl;
		}
	}

	read_file.close();
	write_file.close();

	return 0;
}


