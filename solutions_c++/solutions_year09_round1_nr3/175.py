#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <map>


int t, n, m;

double DP[ 50 ];

long long C[ 50 ][ 50 ];

int primes[ 12 ] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
int cnt[ 12 ];


void change( int p , int chg)
{
    for( int i = 0; i < 12 ; ++i )
    {
        while( p % primes[ i ] == 0 )
        {
            cnt[ i ] += chg;
            p /= primes[ i ];
        }
    }
}

void change_1( int p , int chg)
{
    for( int i= 2; i<=p ;++i)
        change( i , chg);
}

double ppb( int n , int m , int mam , int chce)
{   
    if( mam + chce < m ) return 0.0;
    for( int j = 0; j< 12 ;++j ) cnt[ j ] = 0;

    change_1( n - mam , 1);
    change_1( chce , -1);
    change_1( n - mam - chce , -1);

    change_1( mam , 1);
    change_1( m - chce , -1);
    change_1( mam - m + chce , -1);

    change_1( n , -1);
    change_1( m , 1);
    change_1( n - m , 1);

    double ret = 1.0;

    for( int i = 0 ; i < 12; ++i)
    {
        while( cnt[ i ] > 0 )
        {
            cnt[ i ]--;
            ret *= primes[i];
        }
        while( cnt[ i ] < 0 )
        {
            cnt[ i ]++;
            ret /= primes[i];
        }
    }

    return ret;
}

int main( )
{
    C[ 0 ][ 0 ] = C[ 1 ][ 0 ] = C[ 1 ][ 1 ] = 1;
    
    for( int i = 2 ; i <= 40 ; ++i )
    {
        C[ i ][ 0 ] = C[ i ][ i ] = 1;
        for( int j = 1 ; j < i ; ++j )
            C[ i ][ j ] = C[ i - 1 ][ j ] + C[ i - 1 ][ j - 1 ];
    }
   
    scanf( "%d", &t);
    for( int test = 1 ; test <= t ; ++test )
    {
        scanf( "%d %d", &n , &m);
        
        for( int j = 0 ; j <= n ; ++j ) DP[ j ] = 0.0;
        DP[ 0 ] = 0.0;
        
        for( int i = 1 ; i <= n ; ++i )
        {
            double q = 0.0;
            double p = ppb( n , m , n - i , 0 );
            for( int j = 1; j <= std::min( i , m ) ; ++j )
                q += ppb( n , m , n - i, j ) * DP[ i - j ];
            DP[ i ] = (q) / (1.0 - p) + (1.0 - p )/ (( 1.0 - p ) * ( 1.0 - p ));
        }
        printf( "Case #%d: %.7lf\n", test, DP[ n ] );              
    }
    
    return 0;
}