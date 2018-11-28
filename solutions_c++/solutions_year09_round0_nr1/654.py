#include <stdio.h>
#include <string.h>

#define MAX_WORDS				5010
#define MAX_WORD_LEN			20

char dic[MAX_WORDS][MAX_WORD_LEN] ;
char buffer[1000] ;

bool compWord( char *str , char *other )
{
	while ( *str )
	{
		bool ok = 0 ;
		if ( *other == '(' ) 
		{
			++other ;
			while ( *other != ')' )
			{
				if ( *other == *str ) ok = 1 ;
				++other ;
			}
		}
		else
		{
			if ( *other == *str ) ok = 1 ;
		}
		if ( !ok ) return 0 ;
		++str ;	++other ;
	}
	return 1 ;
}

int main () 
{
	int i , j , l , d , n ;

	freopen( "A-large.in" , "r" , stdin );
	freopen( "A-large.out" , "w" , stdout ) ;

	scanf( "%d%d%d" , &l , &d , &n ) ; gets( buffer ) ;
	for ( i=0 ; i<d ; ++i )
		gets( dic[i] ) ;
	for ( i=1 ; i<=n ; ++i )
	{
		gets( buffer ) ;
		int cnt = 0 ;
		for ( j=0 ; j<d ; ++j )
			if ( compWord( dic[j] , buffer ) ) ++cnt ;
		printf( "Case #%d: %d\n" , i , cnt ) ;
	}

	return 0 ;
}