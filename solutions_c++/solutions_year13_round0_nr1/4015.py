#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <list>
#include <map>
#include <string>

using namespace std;

#define ProblemName "A"
#define InputSize   "large"

int checkifwonby(char board[][5], char P)
{
	int r;
	int d1 = 0, d2 = 0;

	for(r = 0; r < 4; r++)
	{
		int c;
		for(c = 0; c < 4; c++)
		{
			if ( board[r][c] == P
				|| board[r][c] == 'T')
			{
			} else
			{
				break;
			}
		}

		if ( c == 4 )
			return 1;

		for(c = 0; c < 4; c++)
		{
			if ( board[c][r] == P
				|| board[c][r] == 'T')
			{
			} else
			{
				break;
			}
		}

		if ( c == 4 )
			return 1;

		if ( board[r][r] == P
			|| board[r][r] == 'T' )
		{
			d1++;
		}

		if ( board[r][3 - r] == P
			|| board[r][3 - r] == 'T' )
		{
			d2++;
		}
	}

	return ( d1 == 4 || d2 == 4 );
}

char* check(char board[][5])
{
	if ( checkifwonby( board, 'X') )
	{
		return "X won";
	} else if ( checkifwonby( board, 'O') )
	{
		return "O won";
	}

	for ( int i = 0; i < 4; i++ )
	{
		for ( int j = 0; j < 4; j++ )
		{
			if ( board[i][j] == '.' )
			{
				return "Game has not completed";
			}
		}
	}

	return "Draw";
}

int main(int argc, char **argv)
{
	freopen(ProblemName "-" InputSize ".in", "rb", stdin);
	freopen(ProblemName "-" InputSize ".out", "wb", stdout);

	int T;
	char board[4][5];
	scanf("%d", &T);
	for ( int t = 1;
		  t <= T;
		  t++ )
	{
		for(int r = 0; r < 4; r++)
		{
			scanf( "%s", board[r]);
		}

		printf("Case #%d: %s\n", t, check(board));
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}