#include<iostream>
#include<stdlib.h>
#include<vector>
#include<string.h>
#include<queue>
#define MAXSIZE 400
#include<stdio.h>

using namespace std ;
char s[MAXSIZE] , List[MAXSIZE] ;		
char Combine[MAXSIZE][4] , Oppose[MAXSIZE][4] ;	
int C  , O , N ;
void f(  )
{
	int i = 0 , j , k = 0 , co = 0 ; 
	char tra[MAXSIZE] = "" ;	
	for( i = strlen( List )-1 ; i >= 0 ; )
	{
		co = 0 ;
		for( j = 0 ; j < C ; j++ )
		{
			if( Combine[j][0] == List[i] && Combine[j][1] == List[i-1] )
			{
				tra[k++] = Combine[j][2] ;
				i -= 2 ;
				co = 1 ;
				break ;
			}
			if( Combine[j][1] == List[i] && Combine[j][0] == List[i-1] )
			{
				tra[k++] = Combine[j][2] ;
				i -= 2 ;
				co = 1 ;
				break ;
			}
		}
		if( co == 0 )
		{
			tra[k++] = List[i] ;
			i-- ;
		}
	}
	tra[k] = '\0' ;
	k = 0 ;
	for( i = strlen( tra )-1 ; i >= 0 ; i-- )
		List[k++] = tra[i] ;
	List[k] = '\0' ;	
}
void g(  )
{
	int i , j , k = 0 , l , co = 0 ; 
	for( i = strlen( List )-1 ; i >= 0 ; )
	{
		co = 0 ;
		for( j = 0 ; j < O ; j++ )
		{
			if( Oppose[j][0] == List[i] )
			{
				for( l = 0 ; l <= i-1 ; l++ )
					if( List[l] == Oppose[j][1] )
					{
						i = l-1 ;
						co = 1 ;
						List[0] = '\0' ;
						break ;
						
					}
			}
			if( Oppose[j][1] == List[i] )
			{
				for( l = 0 ; l <= i-1 ; l++ )
					if( List[l] == Oppose[j][0] )
					{
						co = 1 ;
						i = l-1 ;
						List[0] = '\0' ;
						break ;
					}	
			}
			if( co == 1 )
				break ;
		}
		if( co == 0 )
			i-- ;
		if( co == 1 )
			break ;
	}
}
int main( )
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );	
	int T , t , i , j , k , len ;
	scanf( "%d" , &T ) ;
	t = T ;
	while( t-- )
	{
		scanf("%d" , &C ) ;
		for( i = 0 ; i < C ; i++ )
			scanf( "%s" , &Combine[i] ) ;
		scanf( "%d" , &O ) ;
		for( i = 0 ; i < O ; i++ )
			scanf( "%s" , &Oppose[i] ) ;
		scanf( "%d" , &N ) ;
		scanf( "%s" , &s ) ;
		List[0] = '\0' ;
		j = k = 1 ;
		for( i = 0 ; i < N ; i++ )
		{
			len = strlen( List ) ;
			List[len] = s[i] ;
			List[len+1] = '\0' ;
			f( ) ;
			g( ) ;
		}
		printf( "Case #%d: " , T-t ) ;
		printf( "[" ) ;
		for( i = 0 ; i < strlen( List ) ; i++ )
		{
			if( i == strlen( List ) -1 )
				printf( "%c" , List[i] ) ; 
			else
				printf( "%c, " , List[i] ) ; 
		}
		printf( "]\n" ) ;
	}
	return 0 ;
}
