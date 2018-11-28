#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int Maxn = 100 + 10 ;

int n , s , p ;
int score[ Maxn ] , f[ Maxn ] , g[ Maxn ] ;
int pla[ Maxn ] ;

bool cmp( int a , int b )
{
    return ( f[ a ] - g[ a ] ) > ( f[ b ] - g[ b ] ) ;
}

int main()
{
    freopen( "B-large.in" , "r" , stdin ) ;
    freopen( "B-large.out" , "w" , stdout ) ;
    int test , T = 0 ;
    for ( scanf( "%d" , &test ) ; test ; test -- )
    {
        scanf( "%d%d%d" , &n , &s , &p ) ;
        for ( int i = 0 ; i < n ; i ++ ) scanf( "%d" , &score[ i ] ) ;
        for ( int i = 0 ; i < n ; i ++ ) pla[ i ] = i ;

        for ( int i = 0 ; i < n ; i ++ )
        {
            if ( score[ i ] / 3 >= p ) f[ i ] = 1 ;
            else if ( score[ i ] / 3 + 2 < p ) f[ i ] = 0 ;
            else if ( score[ i ] / 3 + 2 == p )
            {
                if ( score[ i ] % 3 == 2 ) f[ i ] = 1 ;
                else f[ i ] = 0 ;
            }
            else if ( score[ i ] / 3 + 1 == p )
                if ( score[ i ] % 3 >= 1 ) f[ i ] = 1 ;
                else if ( score[ i ] / 3 >= 1 ) f[ i ] = 1 ;
                else f[ i ] = 0 ;
        }

        for ( int i = 0 ; i < n ; i ++ )
        {
            if ( score[ i ] / 3 >= p ) g[ i ] = 1 ;
            else if ( score[ i ] / 3 + 1 < p ) g[ i ] = 0 ;
            else if ( score[ i ] % 3 == 0 ) g[ i ] = 0 ; else g[ i ] = 1 ;
        }

        sort( pla , pla + n , cmp ) ;
        //for ( int i = 0 ; i < n ; i ++ ) cout << pla[ i ] << ' ' << f[ pla[ i ] ] << ' ' << g[ pla[ i ] ] << endl;
        int ans = 0 ;
        for ( int i = 0 ; i < n ; i ++ )
            if ( i < s ) ans += f[ pla[ i ] ] ; else ans += g[ pla[ i ] ] ;
        cout << "Case #" << ++ T << ": " << ans << endl;
    }
}
