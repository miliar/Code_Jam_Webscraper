/*
	Author: Ali-Amir Aldan
	Problem: Next_number
	Contest: Google Code Jam Round 1
*/
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int T, k, res, n;
char s[ 100 ];

int main()
{
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	scanf( "%d\n",&T );
	for( int sw=0;sw<T;sw++ )
	{
		scanf( "%s\n",s );
		n=strlen( s );
		for( k=1; ( k<n ) && ( s[ n-k ]<=s[ n-k-1 ] );k++ );
		printf( "Case #%d: ", sw+1 );
		if( k==n )
		{
			sort( s,s+n );
			for( k=0;s[ k ]=='0' && k<n ;k++ );
			printf( "%c",s[ k ] );
			for( int i=0;i<k+1;i++ )
				printf( "0" );
			for( int i=k+1;i<n;i++ )
				printf( "%c",s[ i ] );
		}
		else
		{
			for( int i=n-1;i>n-k-1;i-- )
				if( s[ i ]>s[ n-k-1 ] )
				{
					swap( s[ i ], s[ n-k-1 ] );
					break;
				}
			sort( s+n-k,s+n );
			for( int i=0;i<n;i++ )
				printf( "%c",s[ i ] );
		}
		printf( "\n" );
	}
	return 0;
}
