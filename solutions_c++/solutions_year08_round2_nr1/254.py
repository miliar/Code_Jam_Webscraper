#include <iostream>

using namespace std ;

struct node
{
	int x , y ;
};
node a[105] ;

int main(){
	int t ;
	freopen( "A-small-attempt2.in" , "r" , stdin ) ;
	freopen( "A-small-attempt2.out" , "w" , stdout ) ;
	scanf("%d" , &t ) ;
	int test = 1 ;
	while( t -- )
	{
		
		int i , j , k ;
		long long n , A , B , C , D , x , y , m ;
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld" , &n , &A , &B , &C , &D , &x , &y , &m ) ;
		a[0].x = x , a[0].y = y ;
		for( i = 1 ; i <= n -1 ; i ++ )
		{
			x = (A*x + B)%m ;
			y = (C*y + D)%m ; 
			a[i].x = x , a[i].y = y ;
		}

		long long cnt = 0 ;
		for( i = 0 ; i < n ; i ++ )
		{
			for( j = i + 1 ; j < n ; j ++ )
			{
				for( k = j + 1 ; k < n ; k ++ )
				{
					if( (a[i].x + a[j].x + a[k].x) % 3 == 0 && (a[i].y + a[j].y + a[k].y) % 3 == 0 )
						cnt ++ ;
				}
			}
		}

		printf("Case #%d: %lld\n" , test++ , cnt ) ;
	}
	return 0 ;
}