#include<iostream>
using namespace std;

struct pp
{
	int x , y ;  
}BB[2005] ; 
int main()
{
	int n , t , i , j , cas , ans ; 
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "11.out" , "w" , stdout ) ;
	scanf( "%d" , &t ) ;
	ans = 0 ;
	for( cas = 1 ; cas <= t ; cas++ )
	{
		scanf( "%d" , &n ) ;
		ans = 0 ;
		for( i = 0 ; i < n ; i++ )
		{
			scanf( "%d %d" , &BB[i].x , &BB[i].y ) ;
			for( j = 0 ; j < i ; j++ )
			{
				if( BB[j].x > BB[i].x && BB[j].y < BB[i].y ) 
					ans++ ; 
				else
					if( BB[j].x < BB[i].x && BB[j].y > BB[i].y ) 
						ans++ ; 
			}
		}
		printf( "Case #%d: "  , cas ) ;
		printf( "%d\n" , ans ) ;
 	}
	return 0 ;
}