#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

#define modulo 10000

using namespace std ;

char p[ 30 ] = " welcome to code jam" , s[ 510 ] ;
int dp[ 500 ][ 30 ] ;

int main( )
{
    int Ncase ;
    //freopen( "in.txt" , "r" , stdin ) ;
    //freopen( "out.txt" , "w" , stdout ) ;
    scanf( "%d" , &Ncase ) ;
    gets( s ) ;
    for( int cnt = 1 ; cnt <= Ncase ; ++ cnt )
    {
        memset( dp , 0 , sizeof( dp ) ) ;
        dp[ 0 ][ 0 ] = 1 ;
        gets( s + 1 ) ;
        s[ 0 ] = p[ 0 ] = '@' ;
        int l = strlen( p ) , n = strlen( s ) ;
        for( int i = 1 ; i <= n ; i ++ )
             for( int j = 1 ; j <= l ; j ++ )
             {
                  if( s[ i ] == p[ j ] )
                  {
                     for( int k = 0 ; k < i ; k ++ )
                          if( s[ k ] == p[ j - 1 ] )
                              dp[ i ][ j ] = ( dp[ i ][ j ] + dp[ k ][ j - 1 ] ) % modulo ;
                  }
             }
        printf( "Case #%d: " , cnt ) ;
        if( dp[ n ][ l ] < 1000 ) printf( "0" ) ;
        if( dp[ n ][ l ] < 100 ) printf( "0" ) ;
        if( dp[ n ][ l ] < 10 ) printf( "0" ) ;
        printf( "%d\n" , dp[ n ][ l ] ) ;
    }
    
    return 0 ;
}
