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

typedef long long lint;
typedef long double lod;

void prepare( )
{
	#ifdef _DEBUG
		freopen( "in.txt", "r", stdin );
	#else
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	#endif
}

const int MAXN = 155;

char s[MAXN][MAXN];
int n;

int get( int x, int y )
{
	if ( x < 0 || n <= x )
		return 0;
	if ( y < 0 || n <= y )
		return 0;
	if ( s[x][y] == ' ' )
		return 0;
	return s[x][y];
}

bool is_true( int x, int y )
{
	int i, k, a, b;
	for ( i = 0; i < n; i++ )
	{
		for ( k = 0; k < n; k++ )
		{
			a = get( i, k );
			b = get( x - i, k );
			if ( a != 0 && b != 0 && a != b )
				return false;
			a = get( i, k );
			b = get( i, y - k );
			if ( a != 0 && b != 0 && a != b )
				return false;
			a = get( i, k );
			b = get( x - i, y - k );
			if ( a != 0 && b != 0 && a != b )
				return false;
		}
	}
	return true;
}

bool solve( )
{
	int i, k;
	memset( s, 0, sizeof( s ) );
	scanf( "%d", &n );
	gets( s[0] );
	n = n * 2 - 1;
	for ( i = 0; i < n; i++ )
		gets( s[i] );
	int res = -1;
	for ( i = 0; i < n; i++ )
	{
		for ( k = -i; k <= i; k++ )
		{
			if ( is_true( n + 2 * k - 1, n - 2 * ( i - abs( k ) ) - 1 ) )
				break;
			if ( is_true( n + 2 * k - 1, n + 2 * ( i - abs( k ) ) - 1 ) )
				break;
		}
		if ( k <= i )
			break;
	}
	n = ( n + 1 ) / 2;
	res = ( n + i ) * ( n + i ) - n * n;
	printf( "%d\n", res );
	return true;
}

int main( )
{
	prepare( );
	int i, t;
	scanf( "%d", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d: ", i + 1 );
		( solve( ) );
	}
	return 0;
}
