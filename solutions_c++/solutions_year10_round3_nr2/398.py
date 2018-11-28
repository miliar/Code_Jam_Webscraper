#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int t , cas , i , j ; 
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "22.out" , "w" , stdout ) ;
	scanf( "%d" , &t ) ;
	double l , p , c , di , low ; 
	for( cas = 1 ; cas <= t ; cas++ )
	{
		scanf( "%lf %lf %lf" , &l , &p , &c ) ; 
		for( i = 0 ; ; i++ ) 
		{
			low = l * pow( c , pow( 2.0 , i ) ) ;
			if( low >= p )
				break ; 
		}
		printf( "Case #%d: %d\n" , cas , i  ) ;
	}
	return 0 ;
}