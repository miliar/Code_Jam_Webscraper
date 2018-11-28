#include <stdio.h>
int dp[11111][2] ;
struct point { int g , c ; } p[11111] ;

int main()
{
    freopen ( "A-large.in" , "r" , stdin ) ;
    freopen ( "A-large.out" , "w" , stdout ) ;    
    int m , v , i , k ,  tn  , t , be0 , be1 , prob = 0 ;
    for ( scanf ( "%d" , &tn ) ; tn -- ; )
    {
        for ( i = 0 ; i < 11111 ; i ++ )
            dp[i][0] = dp[i][1] = 111111111 ;
        scanf ( "%d%d"  , &m , &v ) ;
        k = 0 ;
        for ( i = 1 ; i <= ( m - 1 ) / 2 ; i ++ )
        {
            k ++ ;
            scanf ( "%d%d" , &p[k].g , &p[k].c ) ;
        }
        t = k ;
        for ( i = 1 ; i <= ( m + 1 ) / 2 ; i ++ )
        {
            k ++ ;
            scanf ( "%d" , &p[k].g ) ;
            dp[k][p[k].g] = 0 ;
        }
        for ( i = t ; i >= 1 ; i -- )
        {
            if ( p[i].g == 0 ) be0 = 0 ;
            else if ( p[i].c ) be0 = 1 ;
            else be0 = 111111111 ;
            if ( p[i].g == 1 ) be1 = 0 ;
            else if ( p[i].c ) be1 = 1 ;
            else be1 = 111111111 ;
            if ( be0 + dp[i*2][0] + dp[i*2+1][0] < dp[i][0] )
               dp[i][0] = be0 + dp[i*2][0] + dp[i*2+1][0] ;
            if ( be1 + dp[i*2][0] + dp[i*2+1][0] < dp[i][0] )
               dp[i][0] = be1 + dp[i*2][0] + dp[i*2+1][0] ;
               
            if ( be0 + dp[i*2][0] + dp[i*2+1][1] < dp[i][1] )
               dp[i][1] = be0 + dp[i*2][0] + dp[i*2+1][1] ;
            if ( be1 + dp[i*2][0] + dp[i*2+1][1] < dp[i][0] )
               dp[i][0] = be1 + dp[i*2][0] + dp[i*2+1][1] ;
               
            if ( be0 + dp[i*2][1] + dp[i*2+1][0] < dp[i][1] )
               dp[i][1] = be0 + dp[i*2][1] + dp[i*2+1][0] ;
            if ( be1 + dp[i*2][1] + dp[i*2+1][0] < dp[i][0] )
               dp[i][0] = be1 + dp[i*2][1] + dp[i*2+1][0] ;  
               
            if ( be0 + dp[i*2][1] + dp[i*2+1][1] < dp[i][1] )
               dp[i][1] = be0 + dp[i*2][1] + dp[i*2+1][1] ;
            if ( be1 + dp[i*2][1] + dp[i*2+1][1] < dp[i][1] )
               dp[i][1] = be1 + dp[i*2][1] + dp[i*2+1][1] ;  
        }
        
        if ( dp[1][v] < 111111111 ) 
           printf ( "Case #%d: %d\n" , ++ prob , dp[1][v] ) ;
        else 
           printf ( "Case #%d: IMPOSSIBLE\n" , ++ prob ) ;
    }
    return 0 ;
}
