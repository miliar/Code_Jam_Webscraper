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

typedef pair <int, int> pii;
const int MAXN = 55;

char s[MAXN][MAXN];
set < pii > a;

void solve( )
{
	int n, m, i, k, x, y;
	a.clear( );
	scanf( "%d%d", &n, &m );
	for ( i = 0; i < n; i++ )
		scanf( "%s", s[i] );
	for ( i = 0; i < n; i++ )
	{
		for ( k = 0; k < m; k++ )
		{
			if ( s[i][k] == '#' )
				a.insert( make_pair( i, k ) );
		}
	}
	pii q;
	while ( a.size( ) > 0 )
	{
		q = *a.begin( );
		x = q.first;
		y = q.second;
		if ( x + 1 >= n || y + 1 >= m )
		{
			printf( "Impossible\n" );
			return;
		}
		if ( s[x + 1][y] != '#' || s[x][y + 1] != '#' || s[x + 1][y + 1] != '#' )
		{
			printf( "Impossible\n" );
			return;
		}
		s[x][y] = '/';
		s[x + 1][y + 1] = '/';
		s[x][y + 1] = '\\';
		s[x + 1][y] = '\\';
		a.erase( make_pair( x, y ) );
		a.erase( make_pair( x, y + 1 ) );
		a.erase( make_pair( x + 1, y ) );
		a.erase( make_pair( x + 1, y + 1 ) );
	}
	for ( i = 0; i < n; i++ )
		printf( "%s\n", s[i] );
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














