/*
ID: junwang1
LANG: C++
TASK: maze1
*/

#include <stdio.h>

#include <stdlib.h>

#include <algorithm>

#include <sstream>

#include <memory.h>

#include <math.h>

#include <string>

#include <functional>

#include <iostream>

#include <set>

#include <vector>

#include <list>

#include <map>

#include <queue>

#include <stack>

using namespace std;

const int MAX_N =  256;

const int MAX_L = 200001;


int Win(char board[5][5], char x)
{
		int i = 0;
		int j = 0;

		for (i = 0; i < 4; ++i)
		{
			for (j = 0; j < 4; ++j)
			{
				if (!(board[i][j] == x || board[i][j] == 'T'))
				{
					break;
				}
			}
			if (j == 4)
			{
				return 1;
			}

			for (j = 0; j < 4; ++j)
			{
				if (!(board[j][i] == x || board[j][i] == 'T'))
				{
					break;
				}
			}

			if (j == 4)
			{
				return 1;
			}
		}

		if ((board[0][0] == x || board[0][0] == 'T') && 
			(board[1][1] == x || board[1][1] == 'T') && 
			(board[2][2] == x || board[2][2] == 'T') &&
			(board[3][3] == x || board[3][3] == 'T'))
		{
			return 1;
		}

		if ((board[0][3] == x || board[0][3] == 'T') && 
			(board[1][2] == x || board[1][2] == 'T') && 
			(board[2][1] == x || board[2][1] == 'T') &&
			(board[3][0] == x || board[3][0] == 'T'))
		{
			return 1;
		}


		return 0;

}

void Work ()
{
	freopen ("Tic-Tac-Toe-Tomek.in", "r", stdin);
	freopen ("Tic-Tac-Toe-Tomek.out", "w", stdout);

	int T = 0;
	int t = 0;
	int N = 0;
	int M =  0;
	int i = 0;
	int j = 0;

	char board[5][5];
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		for(i = 0; i < 4; ++i)
		{
			scanf("%s", board[i]);
		}

		int status = 0;
		// X won
		if (Win(board, 'X'))
		{
			printf("Case #%d: X won\n", t);
		}
		else
		{
			if (Win(board, 'O'))
			{
				printf("Case #%d: O won\n", t);
			}
			else
			{
				bool draw = true;
				for (i = 0; i < 4; ++i)
				{
					for (j = 0; j < 4; ++j)
					{
						if (board[i][j] == '.')
						{
							draw = false; 
							break;
						}
					}
				}

				if (draw)
				{
					printf("Case #%d: Draw\n", t);
				}
				else
				{
					printf("Case #%d: Game has not completed\n", t);
				}
			}
		}



		
	}


	
}

int main()
{
	Work ();

	return 0;
}

