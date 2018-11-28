#define _CRT_SECURE_NO_DEPRECATE
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

#define filein "input"

void prepare( )
{
	freopen( "in.txt", "r", stdin );
	#ifndef _DEBUG
		freopen( "out.txt", "w", stdout );
	#endif
}

#define lint long long
const int MAXN = 5005;
const int MAXL = 17;

char a[MAXN][MAXL];
bool b[MAXL][33];

void readtoken( int n )
{
	static char c;
	if ( ( c = getchar( ) ) == '(' )
		while ( ( c = getchar( ) ) != ')' )
		{
			b[n][c - 'a'] = true;
		}
	else
		b[n][c - 'a'] = true;
}

void solve( )
{
	int l, n, m, i, k, j, res;
	scanf( "%d %d %d\n", &l, &n, &m );
	for ( i = 0; i < n; i++ )
		gets( a[i] );
	for ( i = 0; i < m; i++ )
	{
		memset( b, false, sizeof( b ) );
		res = 0;
		for ( j = 0; j < l; j++ )
			readtoken( j );
		getchar( );
		for ( k = 0; k < n; k++ )
		{
			for ( j = 0; j < l; j++ )
				if ( !b[j][a[k][j] - 'a'] )
					break;
			if ( j == l )
				res++;
		}
		printf( "Case #%d: %d\n", i + 1, res );
	}
}

int main( )
{
	prepare( );
	solve( );
	return 0;
}
