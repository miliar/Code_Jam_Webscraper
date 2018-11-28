#include <stdio.h>
#include <string.h>

struct LIST
{
	LIST * next [ 103 ] ; 
	char * next_C [ 103 ] ; 

	int c ; 
} * root ; 

int N , M , T , L , res , K ; 

char A [ 103 ] ; 
char temp [ 103 ] ; 

void back ( int pos , LIST * now ) 
{
	if ( pos >= L ) return ; 
	int l = 0 , i ; 
	pos ++ ; 
	for ( ; pos < L ; pos ++ ) 
	{
		if ( A [ pos ] == '/' ) break ; 
		temp [ l ] = A [ pos ] ; 
		l ++ ; 
	}
	temp [ l ] = 0 ; 
	for ( i = 0 ; i < now -> c ; i ++ ) 
	{
		if ( strcmp ( now -> next_C [ i ] , temp ) == 0 ) 
		{
			back ( pos , now -> next [ i ] ) ; 
			return ; 
		}
	}
	if ( i == now -> c ) 
	{
		now -> next_C [ now -> c ] = new char [ l + 3 ] ; 
		strcpy ( now -> next_C [ now -> c ] , temp ) ; 
		now -> next [ now -> c ] = new LIST ; 
		now -> next [ now -> c ] -> c = 0 ; 
		now -> c ++ ; 
		res += K ; 
		back ( pos , now -> next [ i ] ) ; 
	}
}

void input ( ) 
{
	FILE *fp = stdin ; 
	

	fscanf ( fp , "%d" , &T ) ;
	for ( int i = 1 ; i <= T ; i ++ ) 
	{
		root = new LIST ; 
		root -> c = 0 ; 
		printf ( "Case #%d: " , i ) ; 
		fscanf ( fp , "%d %d" , &N , &M ) ; 

		K = 0 ; 
		while ( N -- ) 
		{
			fscanf ( fp , "%s" , A ) ; 
			L = strlen ( A ) ; 
			back ( 0 , root ) ;
		}
		K = 1 ; 
		while ( M -- ) 
		{
			fscanf ( fp , "%s" , A ) ; 
			L = strlen ( A ) ; 
			back ( 0 , root ) ;
		}
		printf ( "%d\n" , res ) ; 
		res = 0 ; 

	}
	fclose ( fp ) ; 
}

int main ( ) 
{
	freopen ( "A.in" , "r" , stdin ) ; 
	freopen ( "A.out" , "w" , stdout ) ; 
	input ( ) ;
	return 0 ; 
}
