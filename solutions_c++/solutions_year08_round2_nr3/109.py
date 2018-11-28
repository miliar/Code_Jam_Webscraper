#include <stdio.h>

int main()
{
	freopen ( "C-small-attempt0.in" , "r" , stdin ) ;
	freopen ( "C-small-attempt0.out" , "w" , stdout ) ;
    int tn , n , st[5004] , lk[5004] , i , j , k , pn , prob = 0 , t ;
    for ( scanf ( "%d" , &tn ) ; tn -- ; )
    {
         scanf ( "%d" , &n ) ;
         for ( i = 1 ; i <= n ; i ++ ) lk[i] = i + 1 ;
         lk[n] = 1 ;
         for ( k = n , i = 1 ; i <= n ; i ++ )
         {
            for ( j = 1 ; j < i ; j ++ ) k = lk[k] ;			
            st[lk[k]] = i ; lk[k] = lk[lk[k]] ;            
         }
		 scanf ( "%d" , &pn ) ;
		 printf ( "Case #%d:" , ++prob ) ;
         for ( i = 1 ; i <= pn ; i ++ )
			 scanf ( "%d" , &t ) , printf ( " %d" , st[t] ) ;
         printf ( "\n" ) ;
    }
    return 0 ;
}
