#include <stdio.h>
#include <memory.h>

#define __DEBUG__ 0

int T , N ; 

bool data [ 103 ] [ 103 ] ; 
bool after [ 103 ] [ 103 ] ; 

int main ( ) 
{
	int x1 , y1 , x2 , y2 , i , j , res , t = 0 ; 

	freopen ( "output.txt" , "w" , stdout ) ; 
	freopen ( "input.in" , "r" , stdin ) ; 

	bool check ; 

	scanf ( "%d" , &T ) ; 
	while ( T-- ) 
	{
		t++;
		scanf ( "%d" , &N ) ; 
		while ( N -- ) 
		{
			scanf ( "%d %d %d %d" , &x1 , &y1 , &x2 , &y2 ) ; 
			for ( i = x1 ; i <= x2 ; i ++ ) 
			{
				for ( j = y1 ; j <= y2 ; j ++ )
				{
					data [ i ] [ j ] = true ; 
				}
			}
		}
		
		res = 0 ; 
		while ( 1 ) 
		{
			check = false ; 
			for ( i = 1 ; i <= 100 ; i ++ ) 
			{
				for ( j = 1 ; j <= 100 ; j ++ ) 
				{
					if ( data [ i ] [ j ] == 0 && data [ i - 1 ] [ j ] && data [ i ] [ j - 1 ] ) after [ i ] [ j ] = true ; 
					else if ( data [ i ] [ j ] && ( data [ i - 1 ] [ j ] == 0 && data [ i ] [ j - 1 ] == 0 ) ) after [ i ] [ j ] = false ; 
					else after [ i ] [ j ] = data [ i ] [ j ] ; 
					if ( data [ i ] [ j ] ) check = true ; 
				}
			}
			if ( check ) res ++ ;
			else break; 

			if ( __DEBUG__ )
			{
				for ( i = 1 ; i <= 10 ; i ++ ) 
				{
					for ( j = 1 ; j <= 10 ; j ++ ) 
					{
						printf ( "%d" , ( data [ i ] [ j ] ? 1 : 0 ) ) ; 
					}
					printf ( "\n" ) ; 
				}
				printf ( "\n" ) ; 
			}
 
			memcpy ( data , after , sizeof ( data ) ) ; 
			memset ( after , 0 , sizeof ( after ) ) ; 
		}
		printf ( "Case #%d: %d\n" , t ,res ) ; 
	}
	return 0 ; 
}