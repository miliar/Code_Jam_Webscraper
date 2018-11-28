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

bool solve( )
{
	int i;
	lint p, c, l;
	cin >> l >> p >> c;
	i = 0;
	while ( l < p )
	{
		i++;
		l *= c;
	}
	p = i;
	l = 1;
	i = 0;
	c = 2;
	while ( l < p )
	{
		i++;
		l *= c;
	}
	printf( "%d\n", i );
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
