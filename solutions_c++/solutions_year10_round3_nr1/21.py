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

vector < pair < int, int > > a;

bool solve( )
{
	a.clear( );
	int n, i, k, x, y;
	scanf( "%d", &n );
	for ( i = 0; i < n; i++ )
	{
		scanf( "%d%d", &x, &y );
		a.push_back( make_pair( x, y ) );
	}
	sort( a.begin( ), a.end( ) );
	int res = 0;
	for ( i = 0; i < n; i++ )
	{
		for ( k = 0; k < i; k++ )
			if ( a[i].second < a[k].second )
				res++;
	}
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
