#include <limits.h>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX_TOTAL_SCORE 		30
#define MAX_SCORE				10
#define MAX_N					104

bool ok[2][MAX_SCORE+1][MAX_TOTAL_SCORE+1];
//ok[isSurprising?][bestScore][totalScore]

int memo[MAX_N][MAX_N];
int score[MAX_N];

int main ( )
{
	freopen ( "input", "r", stdin );
	freopen ( "output", "w", stdout );

	int i, j, k, t;
	
	memset ( ok, false, sizeof ( ok ) );
	for ( i = 0; i <= MAX_SCORE; ++i )
		for ( j = i; j <= i+2 && j <= MAX_SCORE; ++j )
			for ( k = j; k <= i+2 && k <= MAX_SCORE; ++k )
				ok[(k==i+2)][k][i+j+k] = true;
	
	int ntests, n, nsurp, p;
	scanf ( "%d", &ntests );
	
	for ( t = 1; t <= ntests; ++t )
	{
		scanf ( "%d%d%d", &n, &nsurp, &p );
		for ( i = 1; i <= n; ++i )
			scanf ( "%d", &score[i] );
		
		memo[0][0] = 0;
		for ( j = 1; j <= n; ++j )
			memo[0][j] = INT_MIN;
	
		for ( i = 1; i <= n; ++i )
			for ( j = 0; j <= n; ++j )
			{
				memo[i][j] = 0;
				if ( i < j ) continue;
				for ( k = 0; k <= MAX_SCORE; ++k )
				{
					if ( ok[1][k][score[i]] && j > 0 )
						memo[i][j] = max ( memo[i][j], memo[i-1][j-1] + (k>=p) );
					if ( ok[0][k][score[i]] )
						memo[i][j] = max ( memo[i][j], memo[i-1][j] + (k>=p) );
				}
			}
		
		printf ( "Case #%d: %d\n", t, memo[n][nsurp] );
	}
	
	return 0;
}
