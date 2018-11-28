#include <stdio.h>
#include <string.h>
char s[1111] , k , mark[7] , chg[1111] ;
int st[6] , ans ;

void judge()
{
     int i , now , l = strlen(s) , j ;
     for ( i = 0 ; i < l / k ; i ++ )
         for ( j = 0 ; j < k ; j ++ )
             chg[i*k+st[j]] = s[i*k+j] ;
     for ( now = i = 1 ; i < l ; i ++ )
         if ( chg[i] != chg[i-1] ) now ++ ;
     if ( now < ans ) ans = now ;
}

void dfs ( int d )
{
     int i ;
     if ( d == k )
     {
        judge() ;
        return ;
     }
     for ( i = 0 ; i < k ; i ++ )
         if ( !mark[i] ) 
         {
              mark[i] = 1 ;
              st[d] = i ;
              dfs ( d + 1 ) ;
              mark[i] = 0 ;
         }
}

int main()
{
    freopen ( "D-small-attempt0.in" , "r" , stdin ) ;
    freopen ( "D-small-attempt0.out" , "w" , stdout ) ;    
    int tn , prob = 0 ;
    for ( scanf ( "%d" , &tn ) ; tn -- ; )
    {
        scanf ( "%d%s" , &k , s ) ;
        memset ( mark , 0 , sizeof(mark) ) ;
        ans = 111111111 ;
        dfs ( 0 ) ;
        printf ( "Case #%d: %d\n" , ++prob , ans ) ;
    }
    return 0 ;
}
