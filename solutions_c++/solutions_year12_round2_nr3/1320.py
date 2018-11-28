#include "stdafx.h"
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

int gcd( int a, int b)
{
	return !b ? a : gcd( b, a%b );
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w+", stdout );

	int tc; scanf( "%d", &tc );
	for ( int _=0; _<tc; _++ )
	{
		int n; scanf( "%d", &n );
		long long a[510];
		for ( int i = 0; i < n; i++ ) scanf( "%lld", &a[i] );
		map<long long, int> m;
		int i, yes=0;
		long long s;
		for (i = 0; i < (1<<n); i++ )
		{
			s=0;
			for ( int j = 0; j < n; j++ )
			{
				if ( (1<<j)&i ) s += a[j];
			}
			if ( m[s] ) { yes=1; break; }
			else m[s]=i;
		}
		printf( "Case #%d:\n", _+1 );
		if ( !yes ) printf( "Impossible" );
		else
		{
			for ( int j = 0; j < n; j++ ) if ( (1<<j)&m[s] ) printf( "%lld ", a[j] ); printf( "\n" );
			m[s]=i;
			for ( int j = 0; j < n; j++ ) if ( (1<<j)&m[s] ) printf( "%lld ", a[j] ); printf( "\n" );
		}
	}

	return 0;
}
