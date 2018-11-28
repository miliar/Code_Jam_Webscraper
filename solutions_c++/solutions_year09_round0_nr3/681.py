#include <stdio.h>
#include <string.h>

#define MAX_STRING_LEN 			510
#define MOD						10000

char str[] = "welcome to code jam" ;
char buffer[MAX_STRING_LEN] ;
int count[MAX_STRING_LEN][19] ;

int main ()
{
	int i , j , k , t , len ;
	
	freopen( "C-large.in.txt" , "r" , stdin ) ;
	freopen( "C-large.out" , "w" , stdout ) ;
	scanf( "%d" , &t ) ; gets( buffer ) ;
	for ( k=1 ; k<=t ; ++k )
	{
		gets( buffer ) ;
		len = strlen( buffer ) ; 
		memset( count , 0 , sizeof(count) ) ;
		for ( i=1 ; i<=len ; ++i )
		{
			count[i][0] = count[i-1][0] ;
			if ( buffer[i-1] == 'w' ) count[i][0] = (count[i][0]+1) % MOD ; 
			for ( j=1 ; j<19 ; ++j ) 
			{
				count[i][j] = count[i-1][j] ;
				if ( buffer[i-1] == str[j] ) 
					count[i][j] = (count[i][j]+count[i-1][j-1]) % MOD ;
			} 
		}
		printf( "Case #%d: %04d\n" , k , count[len][18] ) ;
	}
	return 0 ;
}