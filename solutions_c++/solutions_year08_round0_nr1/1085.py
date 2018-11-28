#include <stdio.h>
#include <string>
#include <map>
using namespace std ;
map <string , int> match ;

int main()
{
	freopen ( "A-large.in" , "r" , stdin ) ;
	freopen ( "A-large.out" , "w" , stdout ) ;
	char s[112] ;
	int n , m , tn , i , t , ans , now , mark[112] , prob = 0;
	for ( scanf ( "%d" , &tn ) ; tn -- ; )
	{
		match.clear() ;
		scanf ( "%d" , &n ) , gets(s) ;
		for ( i = 1 ; i <= n ; i ++ )
			gets(s) , match[s] = i ;
		scanf ( "%d" , &m ) , gets(s) ;
		memset ( mark , 0 , sizeof(mark) ) ;
		ans = 1 , now = 0 ;
		while ( m -- )
		{
			gets(s) ;
			t = match[s] ;
			if ( mark[t] != ans )
			{				
				now ++ ;
				if ( now == n ) now = 1 , ans ++ ;
				mark[t] = ans ;
			}			
		}
		printf ( "Case #%d: %d\n" , ++prob , ans - 1 ) ;
	}
	return 0 ;
}
