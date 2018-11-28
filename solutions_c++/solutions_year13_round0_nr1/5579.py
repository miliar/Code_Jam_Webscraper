// CodeJamTemplate.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void initialize()
{
}

void check_square(char& sq, char& checking)
{
	// If we are checking for invalid, bail.
	if(checking == '.')
		return;

	else if(sq == '.')
	{
		checking = '.';
		return;
	}

	// If we are checking for unknown (first was T)
	else if(checking == 'T')
		checking = sq;

	else
		if(sq == checking || sq == 'T')
			return;
		else
			checking = '.';
}

void solve_case(int test_case)
{

	vector <vector<char>> board;

	board.resize(4);

	for(int i = 0; i < 4; i++)
	{
		string line;
		cin >> line;
		board[i].resize(4);
		for(int j = 0; j < 4; j++)
		{
			board[i][j] = line[j];
		}
	}

	char across, down, diag1, diag2;
	bool over = true;

	diag1 = board[0][0];
	diag2 = board[3][0];

	for(int i = 0; i < 4; i++)
	{
		across = board[i][0];
		down = board[0][i];

		// Check diaganols
		check_square(board[i][i], diag1);
		check_square(board[i][3-i], diag2);

		for(int j = 0; j < 4; j++)
		{
			check_square(board[i][j], across);
			check_square(board[j][i], down);

			if(board[i][j] == '.')
			{
				over = false;
			}
		}

		if(across == 'X' || across == 'O' || down == 'X' || down == 'O')
			break;
	}

	if(across == 'X' || down == 'X' || diag1 == 'X' || diag2 == 'X')
		printf("Case #%d: %s\n", test_case, "X won");
	else if(across == 'O' || down == 'O' || diag1 == 'O' || diag2 == 'O')
		printf("Case #%d: %s\n", test_case, "O won");
	else if(over)
		printf("Case #%d: %s\n", test_case, "Draw");
	else
		printf("Case #%d: %s\n", test_case, "Game has not completed");
}

int _tmain(int argc, _TCHAR* argv[])
{
	initialize();

	int iCases;
	cin >> iCases;

	for (int i = 1; i <= iCases; i++)
		solve_case(i);

	return 0;
}
