#include <stdio.h>

int N ; 

long long int S [ 503 ] ; 

long long int B [ 503 ] [ 503 ] ; 
long long int D [ 503 ] [ 503 ] ; 

// Dij = i번 숫자가 Subset S에서 j번 위치에 있을때의 경우의 수

void input ( ) 
{
	FILE *fp = stdin ;

	int T , a ; 

	fscanf ( fp , "%d" , &T ) ; 

	for ( int i = 1 ; i <= T ; i ++ ) 
	{
		fscanf ( fp , "%d" , &a ) ; 
		printf ( "Case #%d: %lld\n" , i , S [ a ] ) ;
	}

	fclose ( fp ) ; 
}

void init ( ) 
{
	int i , j ; 

	B [ 0 ] [ 0 ] = 1 ; 
	for ( i = 1 ; i <= 500 ; i ++ ) 
	{
		for ( j = 0 ; j <= i ; j ++ ) 
		{
			B [ i ] [ j ] = B [ i - 1 ] [ j ] ;
			if ( j ) B [ i ] [ j ] += B [ i - 1 ] [ j - 1 ] ; 
			if ( B [ i ] [ j ] >= 100003 ) B [ i ] [ j ] -= 100003 ; 
		}
	}
}

void dynamic ( ) 
{
	int i , j , k ; 

	D [ 1 ] [ 0 ] = 1 ;
	for ( i = 2 ; i <= 500 ; i ++ ) 
	{
		for ( j = 1 ; j < i ; j ++ ) 
		{
			for ( k = 1 ; k <= j && k <= i - j ; k ++ ) 
			{
				D [ i ] [ j ] += D [ j ] [ j - k ] * B [ i - j - 1 ] [ k - 1 ] ; 
				if ( D [ i ] [ j ] >= 100003 ) D [ i ] [ j ] %= 100003 ; 
			}
			
			S [ i ] += D [ i ] [ j ] ; 
			if ( S [ i ] >= 100003 ) 
				S [ i ] -= 100003 ; 
		}
	}
}

int main ( ) 
{
	freopen ( "C.in" , "r" , stdin ) ; 
	freopen ( "C.out" , "w" , stdout ) ; 
	init ( ) ; 
	dynamic ( ) ; 
	input ( ) ; 
	return 0 ; 
}