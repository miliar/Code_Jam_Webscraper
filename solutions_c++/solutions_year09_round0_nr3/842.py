/*
	Author: Ali-Amir Aldan
	Problem: Welcome to Code Jam
	Contest: Google Code Jam Q.Round
*/
#include <cstdio>
#include <iostream>

const char s[]="welcome to code jam";

int N, a[ 20 ], b[ 20 ];
char c;

int main()
{
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	scanf( "%d\n",&N );
	for( int sw=0;sw<N;sw++ )
	{
		memset( a,0,sizeof( a ) );
		scanf( "%c",&c );
		while( c!='\n' )
		{
			if( c=='w' )
				b[ 0 ]++;
			else
				for( int i=0;i<19;i++ )
					if( s[ i ]==c )
						b[ i ]+=a[ i-1 ];
			for( int i=0;i<19;i++ )
			{
				a[ i ]=( a[ i ]+b[ i ] )%10000;
				b[ i ]=0;
			}
			scanf( "%c",&c );
		}
		printf( "Case #%d: %04d\n",sw+1,a[ 18 ] );
	}
	return 0;
}
