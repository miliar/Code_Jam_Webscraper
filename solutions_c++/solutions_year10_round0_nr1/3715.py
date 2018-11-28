#include <stdio.h>

const char in_file [ 33 ] = { "A-Large.in" } ; 
const char out_file [ 33 ] = { "A-Large.out" } ; 

int N , K ; 

int main ( ) 
{
	freopen ( out_file , "w" , stdout ) ; 
	FILE *fp = fopen ( in_file , "r" ) ; 

	int T , a , i ; 
	fscanf ( fp , "%d" , &T ) ; 

	for ( i = 1 ; i <= T ; i ++ ) 
	{
		fscanf ( fp , "%d %d" , &N , &K ) ; 

		a = ( 1 << N ) ; 

		printf ( "Case #%d: " , i ) ; 
		if ( K % a == a - 1 ) printf ( "ON\n" ) ; 
		else printf ( "OFF\n" ) ; 
	}
	fclose ( fp ) ; 

	return 0 ; 
}