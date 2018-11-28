#include <stdio.h>
#include <memory.h>

const int POWER [ 13 ] = { 1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512 , 1024 } ; 

int N ; 

int M [ 1033 ] ;

int data [ 13 ] [ 522 ] ; 

long long int D [ 1033 ] [ 1033 ] [ 13 ] ; 

inline long long  max ( long long  a , long long  b ) 
{
	if ( a < b ) return b ; 
	return a ; 
}

inline long long  min ( long long  a , long long  b ) 
{
	if ( a < b ) return a ; 
	return b ; 
}

void process ( ) 
{
	int i , j , k , t ; 

	int a [ 13 ] ; 
	int b [ 13 ] ; 

	memset ( D , 0 , sizeof ( D ) ) ; 

	for ( i = 1 ; i <= POWER [ N ] ; i ++ ) 
	{
		for ( j = 0 ; j <= M [ i ] ; j ++ ) 
		{
			D [ i ] [ i ] [ j ] = 0 ; 
		}
		for ( j = M [ i ] + 1 ; j <= 11 ; j ++ ) 
		{
			D [ i ] [ i ] [ j ] = 99999999 ; 
		}
	}

	for ( i = 1 ; i <= N ; i ++ ) 
	{
		for ( j = t = 1 ; j <= POWER [ N ] ; j += POWER [ i ] , t ++ )
		{
			for ( k = 10 ; k >= 0 ; k -- ) 
			{
				//D [ j ] [ j + POWER [ i ] - 1 ] [ k ] = min ( D [ j ] [ j + POWER [ i - 1 ] - 1 ] [ k ] + D [ j + POWER [ i - 1 ] ] [ j + POWER [ i ] - 1 ] [ 0 ] , D [ j ] [ j + POWER [ i - 1 ] - 1 ] [ 0 ] + D [ j + POWER [ i - 1 ] ] [ j + POWER [ i ] - 1 ] [ k ] ) + data [ i ] [ t ] ; 
				D [ j ] [ j + POWER [ i ] - 1 ] [ k ] = D [ j ] [ j + POWER [ i - 1 ] - 1 ] [ k ] + D [ j + POWER [ i - 1 ] ] [ j + POWER [ i ] - 1 ] [ k ] + data [ i ] [ t ] ; 
				//D [ j ] [ j + POWER [ i ] - 1 ] [ k ] = min ( D [ j ] [ j + POWER [ i ] - 1 ] [ k ] , min ( D [ j ] [ j + POWER [ i - 1 ] - 1 ] [ k + 1 ] + D [ j + POWER [ i - 1 ] ] [ j + POWER [ i ] - 1 ] [ 1 ] , D [ j ] [ j + POWER [ i - 1 ] - 1 ] [ 1 ] + D [ j + POWER [ i - 1 ] ] [ j + POWER [ i ] - 1 ] [ k + 1 ] ) ) ; 
				D [ j ] [ j + POWER [ i ] - 1 ] [ k ] = min ( D [ j ] [ j + POWER [ i ] - 1 ] [ k ] , D [ j ] [ j + POWER [ i - 1 ] - 1 ] [ k + 1 ] + D [ j + POWER [ i - 1 ] ] [ j + POWER [ i ] - 1 ] [ k + 1 ] ) ; 
			}
		}
	}
	printf ( "%lld\n" , D [ 1 ] [ POWER [ N ] ] [ 0 ] ) ; 
}

void input ( ) 
{
	FILE * fp = stdin ; 
	
	freopen ( "output.txt" , "w" , stdout ) ; 
	freopen ( "input.txt" , "r" , stdin ) ; 
	int T , i , j , t = 0 ; 

	fscanf ( fp , "%d" , &T ) ; 

	while ( T -- ) 
	{
		t ++ ; 
		fscanf ( fp , "%d" , &N ) ; 
		
		for ( i = 1 ; i <= POWER [ N ] ; i ++ ) fscanf ( fp , "%d" , &M [ i ] ) ; 
		for ( i = 1 ; i <= N ; i ++ ) 
		{
			for ( j = 1 ; j <= POWER [ N - i ] ; j ++ ) 
			{
				fscanf ( fp , "%d" , &data [ i ] [ j ] ) ; 
			}
		}
		printf ( "Case #%d: " , t ) ; 
		process ( ) ; 
	}

	fclose ( fp ) ; 
}

int main ( )
{
	input ( ) ; 
	return 0 ; 
}