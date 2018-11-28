#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <memory.h>
#include <set>
#include <map>
using namespace std;

#define lint long long

#define file ""

void prepare( )
{
	#ifdef _DEBUG
		freopen( "in.txt", "r", stdin );
	#else
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	#endif
}

const int MAXN = 1001;

int a[MAXN];
lint c[MAXN];
int b[MAXN];

bool solve( )
{
	int i, n, k, s, r;
	lint res;
	scanf( "%d%d%d", &r, &k, &n );
	s = 0;
	for ( i = 0; i < n; i++ )
	{
		scanf( "%d", b + i );
		s += b[i];
	}
	if ( k > s )
		k = s;
	res = 0;
	memset( a, 0, sizeof( a ) );
	memset( c, 0, sizeof( c ) );
	a[0] = r;
	i = 0;
	while ( r > 0 )
	{
		s = 0;
		for ( ; s <= k; i = ( i + 1 ) % n )
			s += b[i];
		i = ( i + n - 1 ) % n;
		res += s - b[i];
		r--;
		if ( r == 0 )
			break;
		if ( a[i] == 0 )
		{
			a[i] = r;
			c[i] = res;
		}
		else
		{
			s = r / ( a[i] - r );
			res += (lint)s * ( res - c[i] );
			r %= ( a[i] - r );
			memset( a, 0, sizeof( a ) );
			memset( c, 0, sizeof( c ) );
		}
	}
	printf( "%lld\n", res );
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
		solve( );
	}
	return 0;
}