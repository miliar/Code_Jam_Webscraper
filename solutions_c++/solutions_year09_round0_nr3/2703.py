#include <iostream>

using namespace std;

const int Maxn = 501 ;

char data[ Maxn ] , a[ 20 ] = {' ','w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'} ;
int f[ Maxn ] [ 20 ] ;
int n , test ;

void Init() 
{
     char ch ;
     
     n = 0 ;
     scanf( "%c" , &ch ) ;
     while ( ch != '\n' ) 
     {
           data[ ++n ] = ch ;
           scanf( "%c" , &ch ) ;
     }
}

void Work() 
{
     int ans = 0 ;
     
     memset( f , 0 , sizeof( f ) ) ;
     f[ 0 ] [ 0 ] = 1 ;
     for ( int i = 1 ; i <= n ; i++ ) 
         for ( int j = 1 ; j <= 19 ; j++ ) 
             if ( data[ i ] == a[ j ] ) 
             {
                for ( int k = i - 1 ; k >= 0 ; k-- ) 
                    f[ i ] [ j ] = ( f[ i ] [ j ] + f[ k ] [ j - 1 ] ) % 10000 ;
             }
     for ( int i = 1 ; i <= n ; i ++ ) ans = ( ans + f[ i ] [ 19 ] ) % 10000 ;
     if ( ans < 1000 ) printf( "0" ) ;
     if ( ans < 100 ) printf( "0" ) ;
     if ( ans < 10 ) printf( "0" ) ;
     printf( "%d\n" , ans ) ;
}

int main()
{
    freopen( "C-small-attempt1.in" , "r" , stdin ) ;
    freopen( "C-small-attempt1.out" , "w" , stdout ) ;
    scanf( "%d\n" , &test ) ;
    for ( int t = 1 ; t <= test ; t ++ ) 
    {
        Init() ;
        printf( "Case #%d: " , t ) ;
        Work() ;
    }
    return 0 ;
}
