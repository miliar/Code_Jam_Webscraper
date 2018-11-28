#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

char s[500][502];
int r, c, d;

bool verify_blade( int n, int ci, int cj )
{
	int bi, ei, bj, ej;
	double bdi, bdj;
	int i, j;
	double di, dj;
	double sx, sy;

	bi = ci - (n / 2);
	bj = cj - (n / 2);
	ei = bi + n - 1;
	ej = bj + n;
	if( n & 1 )
		{
		bdi = bi - ci;
		bdj = bj - cj;
		}
	else{
		bdi = bi - ci + 0.5;
		bdj = bj - cj + 0.5;
		}//end if
	
	sx = sy = 0.0;
	i = bi;
	di = bdi;
	for( dj = bdj + 1.0, j = bj + 1; j < ej - 1; ++j, dj += 1.0 )
		{
		sx += di * (s[i][j] - '0');
		sy += dj * (s[i][j] - '0');
		}//end for
	for( ++i, di += 1.0; i < ei; ++i, di += 1.0 )
		{
		for( dj = bdj, j = bj; j < ej; ++j, dj += 1.0 )
			{
			sx += di * (s[i][j] - '0');
			sy += dj * (s[i][j] - '0');
			}//end for
		}//end for
	for( dj = bdj + 1.0, j = bj + 1; j < ej - 1; ++j, dj += 1.0 )
		{
		sx += di * (s[i][j] - '0');
		sy += dj * (s[i][j] - '0');
		}//end for
	return fabs(sx) < 1e-10 && fabs(sy) < 1e-10;
}//end verify_blade

bool find( int n )
{
	int cbi, cei, cbj, cej;
	int ci, cj;

	cbi = n / 2;
	cbj = n / 2;
	if( n & 1 )
		{
		cei = r - cbi;
		cej = c - cbj;
		}
	else{
		cei = r - cbi + 1;
		cej = c - cbj + 1;
		}//end if
	for( ci = cbi; ci < cei; ++ci )
		{
		for( cj = cbj; cj < cej; ++cj )
			{
			if( verify_blade( n, ci, cj ) )
				{
				return true;
				}//end if
			}//end for
		}//end for
	return false;
}//end find

int bsearch( int first, int last )
{
	int mid;

	if( first == last )
		{
		return first;
		}//end if

	mid = (last - first) / 2 + first;
	if( mid + 1 == last )
		{
		return find( mid ) ? mid : -1;
		}//end if
	if( find( mid ) )
		{
		return bsearch( mid, last );
		}//end if
	if( first + 1 == mid )
		{
		return first;
		}//end if
	return bsearch( first, mid );
}//end bsearch

int main()
{
	freopen( "B.in", "r", stdin );
	freopen( "B.out", "w", stdout );

	int t, i;
	int n;
	int res;
	int j;

	for( scanf( "%d", &t ), i = 1; i <= t; ++i )
		{
		scanf( "%d%d%d", &r, &c, &d );
		for( j = 0; j < r; ++j )
			{
			scanf( "%s", s[j] );
			}//end for
		n = min( r, c );
		/*if( find( n ) )
			{
			res = n;
			}
		else if( n == 3 || !find( 3 ) )
			{
			res = -1;
			}
		else{
			res = bsearch( 3, n );
			}//end if*/
		res = -1;
		for( j = n; j >= 3; --j )
			{
			if( find( j ) )
				{
				res = j;
				break;
				}//end if
			}//end for
		printf( "Case #%d: ", i );
		if( res >= 0 )
			{
			printf( "%d\n", res );
			}
		else{
			printf( "IMPOSSIBLE\n" );
			}//end if
		}//end for

	return 0;
}
