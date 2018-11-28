#include<iostream>
#include<string>
using namespace std;

int State[33] ; 
int main()
{
	int t , i , j , cas ;
	int n , k ; 
	freopen( "A-large.in" , "r" , stdin ) ; 
	freopen( "A.out" , "w" , stdout ) ;
	scanf( "%d" , &t ) ;
	for( cas = 1 ; cas <= t ; cas++ )
	{
		scanf( "%d %d" , &n , &k ) ; 
		memset( State , 0 , sizeof( State ) ) ;
		i = 1 ;
		while( k )
		{
			State[i] = k % 2 ;
			k /= 2  ;
			i++ ; 
		}
		for( i = 1 ; i <= n ; i++ )
			if( State[i] == 0 )
				break ; 
		printf( "Case #%d: "  , cas ) ;
		if( i > n )
			printf( "ON\n" ) ;
		else
			printf( "OFF\n" ) ;
	}
	return 0 ;
}