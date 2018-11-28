#include <stdio.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("resultL.txt","w",stdout);
    int t , n , s , p , a , b , c , i , j , count , either , onlysurprise ;
    int diff ;
    int fs , fns;
    bool f , g ;
    scanf ( "%d" , &t ) ;
    for ( i = 1 ; i <= t ; i++ ) {
        scanf ( "%d %d %d" , &n , &s , &p) ;
        either = 0 ; onlysurprise = 0 ;
               
        for ( j = 0 ; j < n ; j++ ) {
            scanf ( "%d" , &a ) ;
            f = g = false ;
            diff = a - p ;
            
            if ( a >= 2  && a <= 28 ) {
               if ( 2*p-4==diff || 2*p-3==diff)
                  onlysurprise++;
               else if ( 2*p-2 <= diff )
                  either++;
            }
            else {
                 if ( ( a == 0 || a == 1 || a == 29 || a==30 ) && ( a >= p ) ) {
                    either++;
                 }
            }
        }
        
        if ( s <= onlysurprise )
           printf("Case #%d: %d\n" , i , either + s );
        else if ( s > onlysurprise )
           printf("Case #%d: %d\n" , i , either + onlysurprise) ;
    }
    return 0 ;
}
/*
if ( ( 2*p+2 == diff ) || ( 2*p+1 == diff ) || ( 2*p == diff ) || ( 2*p-1 == diff ) ||  ( 2*p-2 == diff ) || ( 2*p-3 == diff ) ||  ( 2*p-2 == diff ) || ( 2*p-4 == diff ) ) {
                  fs++; //fns++; 
               }
               
    /*fs[0] = false ; fs[1] = false ; fs[2] = false ;    // f surprise
    fns[0] = false ; fns[1] = false ; fns[2] = false ; // f not surprise*/
                /*if ( ( 2*p + 2 ) == diff || ( 2*p + 1 ) == diff || ( 2*p - 2 ) == diff || ( 2*p - 1 ) == diff || (2*p == diff) ) {
                  f = true ;
            }
            if ( ( 2*p == diff ) || ( 2*p-2 == diff ) || ( 2*p-3 == diff ) || ( 2*p-4 == diff ) ) {
                  g = true ;
            }
            if ( f && g )
                  either++ ;
            if ( f == false && g == true )
                  onlysurprise++;*/
