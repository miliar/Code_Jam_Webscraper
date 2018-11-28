#include <cstring>
#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std ;
int ans[503][30] ; 
char str[30] = {"welcome to code jam"};
char text[503] ;
int main()
{
	freopen("C-small-attempt0.in","r",stdin) ;
	freopen("C-small-attempt0.out","w",stdout) ; 
	int T , Case = 1 ;
	while ( 1 == scanf("%d",&T))
	{
		gets(text) ; 
 		while ( T -- )
		{
			int i , j , len ; 
			memset(ans , 0 , sizeof(ans)) ; 
			gets(text) ; 
			len = strlen(text) ; 
			for ( i = 0 ; i < len ; i ++)
			{
				if( text[i] == 'w')
				{
					ans[i][0] ++ ;
				}
				else
				{
					if( i )
						for ( j = 1 ; j < 19 ; j ++)
						{
							if(text[i] == str[j] && ans[i-1][j-1] )
							{
								ans[i][j] += ans[i-1][j-1] ;
								if( ans[i][j] > 10000) 
									ans[i][j] -= 10000 ; 
							}
						}
				}
				if( i )
					for ( j = 0 ; j < 19 ; j ++)
					{
						ans[i][j] += ans[i-1][j] ; 
						if( ans[i][j] > 10000) 
								ans[i][j] -= 10000 ; 
					}
			}
			int res = ans[len-1][18] ;
			printf("Case #%d: %d%d%d%d\n" ,Case++, res / 1000 , res /100%10 , res /10%10 , res%10) ; 
		}
	}
	return 0 ; 
}