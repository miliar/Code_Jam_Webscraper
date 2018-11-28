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

#define file "in"

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
	int n, k;
	scanf( "%d%d", &n, &k );
	return ( ( k + 1 ) % ( 1 << n ) == 0 );
}

int main( )
{
	prepare( );
	int i, t;
	scanf( "%d", &t );
	for ( i = 0; i < t; i++ )
		if ( solve( ) )
			printf( "Case #%d: ON\n", i + 1 );
		else
			printf( "Case #%d: OFF\n", i + 1 );
	return 0;
}