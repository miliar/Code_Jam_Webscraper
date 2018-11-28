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

void solve( )
{
	int n, i, x, y = 0, s = 0;
	vector <int> a;
	scanf( "%d\n", &n );
	for ( i = 0; i < n; i++ )
	{
		scanf( "%d", &x );
		y ^= x;
		s += x;
		a.push_back( x );
	}
	if ( y != 0 )
	{
		printf( "NO\n" );
		return;
	}
	sort( a.begin( ), a.end( ) );
	printf( "%d\n", s - a[0] );
	return;
}

int main( )
{
	int t, i, n;
	scanf( "%d\n", &t );
	for ( i = 0; i < t; i++ )
	{
		printf( "Case #%d: ", i + 1 );
		solve( );
	}
	return 0;
}












