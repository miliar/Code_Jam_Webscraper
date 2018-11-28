#include <stdio.h>
int x0 , y0 , flag  , a , n , m , prob = 0 ;

void tryit()
{
     int x , y , xx , x1 , y1 , x2 , y2 , t ;
     if ( flag ) return ;
     for ( x = 0 ; x <= n ; x ++ ) 
     for ( y = 0 ; y <= m ; y ++ )
     {
         x1 = x - x0 , y1 = y - y0 ;         
         for ( xx = 0 ; xx <= n ; xx ++ )
         {
             x2 = xx - x0 ;
             t = a + x1 * y0 + x2 * y1 ;
             if ( x1 == 0 ) continue ;
             if ( t % x1 == 0 )
             {
                  y2 = t / x1 ;
                  if ( y2 >= 0 && y2 <= m )
                  {
                       flag = 1 ;
                       printf ( "Case #%d: %d %d %d %d %d %d\n" , 
                                ++prob , x0,y0,x,y,xx,y2);
                       return ;
                  }
             }
             t = -a + x1 * y0 + x2 * y1 ;
             if ( t % x1 == 0 )
             {
                  y2 = t / x1 ;
                  if ( y2 >= 0 && y2 <= m )
                  {
                       flag = 1 ;
                       printf ( "Case #%d: %d %d %d %d %d %d\n" , 
                                ++prob , x0,y0,x,y,xx,y2);
                       return ;
                  }
             }             
         }
     }
}

int main()
{
    freopen ( "B-small-attempt1.in",  "r" , stdin ) ;
    freopen ( "B-small-attempt1.out" , "w" , stdout ) ;    
    int tn ;
    for ( scanf ( "%d" , &tn ) ; tn -- ; )
    {
        flag = 0 ;
        scanf ( "%d%d%d" , &n , &m , &a ) ;
        x0 = y0 = 0 ;
        tryit() ;
        x0 = n , y0 = 0 ;
        tryit() ;
        x0 = 0 , y0 = m ;
        tryit() ;
        x0 = n , y0 = m ;
        tryit() ;
        if ( !flag ) printf ( "Case #%d: IMPOSSIBLE\n" , ++prob ) ;
    }
    return 0 ;
}
