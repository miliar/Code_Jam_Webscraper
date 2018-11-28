#include <iostream>
#include <string>
#include <vector>
using namespace std ;


int main()
{
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);	

	int n;
	scanf("%d", &n) ;
	char ss[105][105] , qq[1010][105] ;
	int i , j; 
	for( int kase = 1 ; kase <= n ; kase++ )
	{ 
		int s , q ;
		scanf("%d\n", &s) ;
		for( i = 0 ; i < s ; i ++ )
			gets( ss[i] );
		scanf("%d\n", &q) ;
		for( i = 0 ; i < q ; i ++ )
			gets( qq[i]) ;
			
		int ans = 0 ;
		int left = s ;
		bool flag[105] ;
		memset( flag , 0 , sizeof(flag)) ;
		for( i = 0 ; i < q ; i ++ )
		{
			for( j = 0 ; j < s ; j ++ )
			{
				if( strcmp(ss[j], qq[i]) == 0)
				{
					if( flag[j] == 0 )
					{
						left -- ;
						flag[j] = 1 ;	
					}	
				
					if( left == 0 )
					{
						left = s -1 ;
						memset( flag , 0 , sizeof(flag)) ;
						flag[j] = 1 ;
						ans ++ ;	
					}	
					break;
				}	
			}
			
		}
		printf("Case #%d: %d\n",kase,ans);
	}
//    system("pause");
    return 0 ;
}
