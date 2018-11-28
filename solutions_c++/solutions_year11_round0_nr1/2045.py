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

int mabs( int a )
{
	return a < 0 ? -a : a;
}

void solve( )
{
	int n, i, p, t;
	char s[3];
	scanf( "%d", &n);
	int op = 1, bp = 1, r = 0, ot = 0, bt = 0;
	for ( i = 0; i < n; i++ )
	{
		//cerr << n << endl;
		scanf( "%s%d", s, &p );
		if ( s[0] == 'O' )
		{
			swap( op, bp );
			swap( ot, bt );
		}
		{
			//cerr << "p = " << p << "bp = " << bp << "r = " << r << "bt = " << bt << endl;
			t = mabs( p - bp ) - ( r - bt );
			if ( t < 0 )
				t = 0;
			r += t + 1;
			bt = r;
			bp = p;
			//cerr << "t = " << t << endl;
			//cerr << "r = " << r << endl;
		}
		if ( s[0] == 'O' )
		{
			swap( op, bp );
			swap( ot, bt );
		}
	}
	printf( "%d\n", r );
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












