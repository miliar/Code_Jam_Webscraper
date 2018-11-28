#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <math.h>
#include <memory.h>
using namespace std;

#define file "input"

void prepare( )
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
}

char s[33];

void solve( int t )
{
	if ( t == 45 )
		memset( s, 0, sizeof( s ) );
	memset( s, 0, sizeof( s ) );
	gets( s + 1 );
	s[0] = '0';
	int l = strlen( s + 1 ) + 1, i, k;
	s[l] = 0;
	for ( i = l - 1; i > 0; --i )
		if ( s[i] > s[i - 1] )
			break;
	for ( k = l - 1; k > i; --k )
		if ( s[i - 1] < s[k] )
			break;
	swap( s[i - 1], s[k] );
	sort( s + i, s + l );
	i = ( s[0] == '0' ? 1 : 0 );
	printf( "Case #%d: %s\n", t, s + i );
	return;
}

int main( )
{
	prepare( );
	int t, i;
	scanf( "%d\n", &t );
	for ( i = 0; i < t; i++ )
		solve( i + 1 );
	return 0;
}