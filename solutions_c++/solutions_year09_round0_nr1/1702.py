#include <iostream>
#include <string>
#include <set>
#include <algorithm>
using namespace std ; 
#define MAXN 5005
string mat[MAXN] ;
char str[100000] ;
set<char> se[505][20] ;
int list[505] ;

int main()
{
	freopen("A-large.in" , "r" , stdin) ;
	freopen("A-large.in.out" , "w" , stdout) ;
	int L , D , N ;
	int i , j , t ;
	while( 3 == scanf("%d%d%d" ,&L , &D , &N) )
	{
		for(i = 0 ; i < D ; i++)
			cin>>mat[i] ;
		for(i = 0 ; i < N; i++)
		{
			scanf("%s" , str) ;
			t = -1 ;
			bool flag = false ;
			for(j = 0 ; str[j] != '\0' ; j++)
			{
				if( str[j] == '(' )
				{
					t++ ;
					se[i][t].clear() ;
					flag = true ;
				}
				else if( str[j] == ')' ) 
				{
					flag = false ;
				}
				else 
				{
					if( !flag ) t++ ;
					se[i][t].insert( str[j] ) ;			
				}
			}
		}
		sort( mat , mat+D ) ;
		memset(list , 0 , sizeof(list)) ;
		for(j = 0 ; j < N ; j++)
		{
			for(i = 0 ; i < D ; i++)
			{
				for(t = 0 ; t < L ; t++)
					if( se[j][t].find( mat[i][t] ) == se[j][t].end() )
						break ;
				if(t == L) list[j]++ ;
			}
		}
		for(i = 0 ; i < N; i++)
			printf("Case #%d: %d\n" , i+1 , list[i]) ;
		
	}
	return 0 ;
}