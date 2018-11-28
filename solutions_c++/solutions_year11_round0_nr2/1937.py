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

int g( char c )
{
	return c - 'A';
}

void out( char *s )
{
	putchar( '[' );
	for ( int i = 0; s[i] != 0; i++ )
	{
		if ( i > 0 )
			printf( ", " );
		putchar( s[i] );
	}
	putchar( ']' );
	putchar( '\n' );
}

void solve( )
{
	char s[111];
	char r[111];
	char a[27][27];
	bool b[27][27];
	memset( a, 0, sizeof( a ) );
	memset( b, false, sizeof( b ) );
	int n, i, k, m;
	{
		scanf( "%d", &n );
		for ( i = 0; i < n; i++ )
		{
			scanf( "%s", s );
			a[g(s[0])][g(s[1])] = s[2];
			a[g(s[1])][g(s[0])] = s[2];
		}
	}
	{
		scanf( "%d", &n );
		for ( i = 0; i < n; i++ )
		{
			scanf( "%s", s );
			b[g(s[0])][g(s[1])] = true;
			b[g(s[1])][g(s[0])] = true;
		}
	}
	{
		scanf( "%d", &n );
		scanf( "%s", s );
		//cout << "s=" << s << endl;
		for ( i = 0, m = 0; i < n; i++ )
		{
			r[m++] = s[i];
			if ( m > 0 )
			{
				if ( a[g(r[m - 2])][g(s[i])] != 0 )
				{
					r[m - 2] = a[g(r[m - 2])][g(s[i])];
					--m;
				}
				else
				{
					for ( k = 0; k + 1 < m; k++ )
						if ( b[g(r[k])][g(s[i])] )
							m = 0;
				}
			}
			//r[m] = 0;
			//cout << "cerr:";
			//out( r );
		}
		r[m] = 0;
		out( r );
	}
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












