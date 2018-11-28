#include <iostream>

using namespace std ;

int main(){
	int test ;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d" , &test ) ;
	int t = 1 ;
	while( test -- )
	{
		int n , m , a ;
		scanf("%d%d%d" , &n , &m , &a ) ;
		int x , y , x1 , y1 ;
		bool flag = false ;
		printf("Case #%d: " , t++ ) ;
		for( x = 0 ; x <= n ;  x ++ )
		{
			for( y = 0 ; y <= m ; y ++)
			{
				for( x1 = 0 ; x1 <= n ; x1 ++)
				{
					for( y1 = 0 ; y1 <= m ; y1 ++ )
					{
						if( x*y1 - x1*y == a )
						{
							flag = true ;
							printf("0 0 %d %d %d %d\n" , x , y , x1 , y1 ) ;
							break ;
						}
					}
					if( flag ) break ;
				}
				if(flag) break ;
			}
			if(flag) break ;
		}
		if(!flag)
			printf("IMPOSSIBLE\n") ;
	}
	return 0 ;
}