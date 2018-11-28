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
const int MAXL = 505;
const int mod = 10000;
const int al = 19;
const char a[] = "welcome to code jam";

char s[MAXL];
int d[al + 1][MAXL];

void solve( )
{
	gets( s );
	int i, k, l = strlen( s );
	for ( i = 0; i < al; i++ )
	{
		d[i][0] = ( ( i == 0 && s[0] == a[i] ) ? 1 : 0 );
		for ( k = 1; k < l; k++ )
		{
			d[i][k] = d[i][k - 1];
			if ( s[k] == a[i] )
			{
				if ( i > 0 )
					( d[i][k] += d[i - 1][k - 1] ) %= mod;
				else
					( d[i][k] += 1 ) %= mod;
			}
		}
	}
	sprintf( s, "%d\0", d[al - 1][l - 1] + mod );
	puts( s + 1 );
}

int main( )
{
	prepare( );
	int n, i;
	scanf( "%d\n", &n );
	for ( i = 0; i < n; i++ )
	{
		printf( "Case #%d: ", i + 1 );
		solve( );
	}
	return 0;
}
