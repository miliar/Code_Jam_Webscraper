/*
	Author: Ali-Amir Aldan
	Problem: Alien Language
	Contest: Google Code Jam Q.Round
*/
#include <cstdio>
#include <cstring>

int n, D, N, k, l, r, last, top;
int a[ 76000 ][ 30 ], Q[ 1000000 ], end[ 76000 ];
char s[ 76000 ];

int main()
{
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	scanf( "%d %d %d\n",&n,&D,&N );
	for( int i=0;i<D;i++ )
	{
		scanf( "%s\n",s );
		k=0;
		for( int j=0;j<n;j++ )
		{
			if( !a[ k ][ s[ j ] ] )
				a[ k ][ s[ j ] ]=++last;
			k=a[ k ][ s[ j ] ];
		}
		++end[ k ];
	}
	for( int sw=0;sw<N;sw++ )
	{
		scanf( "%s\n",s );
		l=0;r=1;Q[ 0 ]=0;
		for( int j=0;j<strlen( s );j++ )
		{
			top=r;
			if( s[ j ]=='(' )
			{
				j++;
				for( ;( j<strlen( s ) && s[ j ]!=')' );j++ )
					for( int i=l;i<r;i++ )
						if( a[ Q[ i ] ][ s[ j ] ] )
							Q[ top++ ]=a[ Q[ i ] ][ s[ j ] ];					
			}
			else
			{
				for( int i=l;i<r;i++ )
					if( a[ Q[ i ] ][ s[ j ] ] )
						Q[ top++ ]=a[ Q[ i ] ][ s[ j ] ];
			}
			l=r;
			r=top;
		}
		top=0;
		for( int i=l;i<r;i++ )
			top+=end[ Q[ i ] ];
		printf( "Case #%d: %d\n",sw+1,top );
	}
	return 0;
}
