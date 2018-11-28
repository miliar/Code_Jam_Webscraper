#include <stdio.h>
#include <string.h>
#include <memory.h>

const char C [ 23 ] = { " welcome to code jam" } ; 

int N , L ; 

int D [ 23 ] ; 

void input ( ) 
{
	FILE *fp = fopen ( "input.txt" , "r" ) ; 

	char ch [ 503 ] ; 

	int i , j , k ; 

	fgets ( ch , 503 , fp ) ; 
	sscanf ( ch , "%d" , &N ) ; 

	for ( i = 1 ; i <= N ; i ++ ) 
	{
		fgets ( ch , 503 , fp ) ; 

		L = strlen ( ch ) ; 

		memset ( D , 0 , sizeof ( D ) ) ; 
		D [ 0 ] = 1 ; 

		for ( j = 0 ; j < L ; j ++ ) 
		{
			for ( k = 1 ; k < 20 ; k ++ ) 
			{
				if ( C [ k ] == ch [ j ] )
				{
					D [ k ] += D [ k - 1 ] ; 
					D [ k ] %= 1000 ; 
				}
			}
		}

		printf ( "Case #%d: %04d\n" , i , D [ 19 ] % 1000 ) ; 
	}
	fclose ( fp ) ; 
}

int main ( ) 
{
	freopen ( "output.txt" , "w" , stdout ) ; 
	input ( ) ; 
	return 0 ; 
}