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
const int MAXN = 101;
const int inf = ( 1 << 16 );

int a[MAXN][MAXN], w, h;
int b[MAXN * MAXN];
int c[MAXN * MAXN];
int d[MAXN * MAXN];
char s[MAXN][MAXN];

int get_height( int x, int y )
{
	if ( x < 0 || x >= w || y < 0 || y >= h )
		return inf;
	return a[y][x];
}

int hash( int hh, int ww )
{
	return hh * w + ww;
}

int getc( int n )
{
	if ( c[n] != n )
		c[n] = getc( c[n] );
	return c[n];
}

void solve( )
{
	int i, k, q;
	scanf( "%d%d", &h, &w );
	for ( i = 0; i < h; i++ )
		for ( k = 0; k < w; k++ )
			scanf( "%d", &a[i][k] );
	for ( i = 0; i < h; i++ )
	{
		for ( k = 0; k < w; k++ )
		{
			q = a[i][k];
			c[hash( i, k )] = hash( i, k );
			if ( get_height( k, i - 1 ) < q )
			{
				q = a[i - 1][k];
				c[hash( i, k )] = hash( i - 1, k );
			}
			if ( get_height( k - 1, i ) < q )
			{
				q = a[i][k - 1];
				c[hash( i, k )] = hash( i, k - 1 );
			}
			if ( get_height( k + 1, i ) < q )
			{
				q = a[i][k + 1];
				c[hash( i, k )] = hash( i, k + 1 );
			}
			if ( get_height( k, i + 1 ) < q )
			{
				q = a[i + 1][k];
				c[hash( i, k )] = hash( i + 1, k );
			}
		}
	}
	for ( i = h * w - 1; i >= 0; i-- )
	{
		if ( getc( i ) == i )
			b[i] = i;
	}
	for ( i = h * w - 1; i >= 0; i-- )
	{
		if ( i < b[getc( i )] )
			b[getc( i )] = i;
	}
	for ( i = h * w - 1; i >= 0; i-- )
	{
		b[i] = b[getc( i )];
	}
	for ( i = h * w - 1; i >= 0; i-- )
		d[i] = b[i];
	memset( s, 0, sizeof( s ) );
	sort( d, d + w * h );
	k = unique( d, d + w * h ) - d;
	for ( i = k - 1; i >= 0; i-- )
		s[d[i] / w][d[i] % w] = ( i + 'a' );
	for ( i = 0; i < h; i++ )
		for ( k = 0; k < w; k++ )
			s[i][k] = s[b[hash( i, k )] / w][b[hash( i, k )] % w];
	for ( i = 0; i < h; i++ )
		for ( k = 0; k < w; k++ )
			printf( "%c%c", s[i][k], k + 1 == w ? '\n' : ' ' );
}

int main( )
{
	prepare( );
	int t, i;
	scanf( "%d", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d:\n", i + 1 );
		solve( );
	}
	return 0;
}
