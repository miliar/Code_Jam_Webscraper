#include <vector>
#include <stdio.h>
#include <string>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <memory.h>
#include <iostream>
#include <math.h>
using namespace std;

#define filein "test"

void prepare( )
{
	freopen( filein ".in", "r", stdin );
	freopen( filein ".out", "w", stdout );
}

typedef long double lod;
const int MAXN = 111;
char s[MAXN][MAXN];

struct pr
{
	int x, y;
	pr(){x=0; y=0;}
	pr(int X, int Y){x = X; y = Y;}
	pr operator +( const pr &b ) const { return pr( x + b.x, y + b.y ); }
	pr operator -( const pr &b ) const { return pr( x - b.x, y - b.y ); }
	lod C(){return (lod)x / (lod)y; }
};

pr w[MAXN];
lod ow[MAXN];
lod oow[MAXN];

void solve( )
{
	int n, i, k, j;
	scanf( "%d", &n );
	for (i = 0; i < n; i++)
		scanf( "%s", s[i] );
	for ( i = 0; i < n; i++ )
	{
		w[i] = pr(0, 0);
		for ( k = 0; k < n; k++ )
		{
			if ( s[i][k] == '.' )
				continue;
			w[i] = w[i] + pr( s[i][k] - '0', 1 );
		}
	}
	for ( i = 0; i < n; i++ )
	{
		ow[i] = 0;
		j = 0;
		for ( k = 0; k < n; k++ )
		{
			if ( s[i][k] == '.' )
				continue;
			ow[i] = ow[i] + ( w[k] - pr( s[k][i] - '0', 1 ) ).C( );
			j++;
		}
		ow[i] /= j;
	}
	for ( i = 0; i < n; i++ )
	{
		oow[i] = 0;
		j = 0;
		for ( k = 0; k < n; k++ )
		{
			if ( s[i][k] == '.' )
				continue;
			oow[i] = oow[i] + ow[k];
			j++;
		}
		oow[i] /= j;
	}
	lod res;
	for ( i = 0; i < n; i++ )
	{
		res = ( w[i].C( ) + ow[i] * (lod)2 + oow[i] ) / (lod)4;
		printf( "%.15lf\n", (double)res );
	}
	return;
}

int main( )
{
	int t, i;
	scanf( "%d\n", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d:\n", i + 1 );
		solve( );
	}
	return 0;
}















