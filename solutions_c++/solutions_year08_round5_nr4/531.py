#pragma warning(disable: 4786)

#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <cctype>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <ctime>
#include <math.h>
#include <bitset>
#include <complex>
#include <cstdlib>

using namespace std;

typedef __int64 int64;

const double EPS(1E-6);
const double PI(2*cos(0.0));

const int NMAX(128);

int R, W, H;

char board[NMAX][NMAX];
int  cc[NMAX][NMAX];

#define _SUBMIT

int main()
{
	freopen("in.txt", "r", stdin);
#ifdef _SUBMIT
	freopen("out.txt", "w", stdout);
#endif
	int totCase;
	scanf("%d", &totCase);
	for( int nCase=1; nCase<=totCase; nCase++ )
	{
		printf("Case #%d: ", nCase);
		scanf("%d%d%d", &H, &W, &R);
		memset(board, 0, sizeof(board));
		for( int i=0; i<R; i++ )
		{
			int r, c;
			scanf("%d%d", &r, &c);
			r --, c --;
			board[r][c] = 1;
		}
		memset(cc, 0, sizeof(cc));
		cc[0][0] = 1;
		for( int i=0; i<H; i++ )
		{
			for( int j=0; j<W; j++ )
			{
				if( board[i][j]==1 ) continue;
				if( i-2>=0 && j-1>=0 )
				{
					cc[i][j] += cc[i-2][j-1];
				}
				if( i-1>=0 && j-2>=0 )
				{
					cc[i][j] += cc[i-1][j-2];
				}
				cc[i][j] %= 10007;
			}
		}
		printf("%d\n", cc[H-1][W-1]);
	}
	return 0;
}
