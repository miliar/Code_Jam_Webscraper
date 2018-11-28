#include <stdio.h>
#include <string.h>

char map[26] = { 'y', 'h', 'e', 's', 'o', 'c', 'v',
				'x', 'd', 'u', 'i', 'g', 'l', 'b', 
				'k', 'r', 'z', 't', 'n', 'w',
				'j', 'p', 'f', 'm', 'a', 'q' } ; 
				
char g[127] ;
int main()
{
	int t, i, tt ;
	char c ;
	scanf( "%d", &t ) ;
	for ( tt = 1 ; tt <= t ; ++tt )
	{
		printf( "Case #%d:", tt ) ;
		while ( 1 )
		{
			scanf( "%s", g ) ;
			for ( i = 0 ; g[i] ; ++i )
			{
				if ( g[i] == ' ' )
					continue ;
				g[i] = map[ g[i] - 'a' ] ;
			}
			printf( " %s", g ) ;
			
			scanf( "%c", &c ) ;
			if ( c == '\n' )
			{
				printf( "\n" ) ;
				break ;
			}
		}
	}
	return 0 ;
}


