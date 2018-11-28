#pragma comment(linker, "/STACK:16777216")
#pragma warning(disable:4786)

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <stack>
#include <queue>
#include <deque>
#include <ctime>
#include <bitset>
#include <vector>
#include <cstdio>
#include <cctype>
#include <string>
#include <utility>
#include <cstring>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <numeric>
#include <iterator>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define MAX_SIZE 100100
#define MAX_LENGTH 200
#define INF ( 1 << 29 ) ;

#define CLR( a ) memset( a , 0 , sizeof( a ) )
#define MEM( a ) memset( a , -1 , sizeof( a ) )
#define fort( a , b ) for( ind = ( a ) ; ind <= ( b ) ; ind++ )
#define foriab( a , b ) for( i = ( a ) ; i < ( b ) ; i++ )
#define fori( a ) for( i = 0 ; i < ( a ) ; i++ )
#define forj( a ) for( j = 0 ; j < ( a ) ; j++ )
#define print1( a ) printf( "%lld ---\n" , ( a ) )
#define print2( a , b ) printf( "%lld %lld ---\n" , ( a ) , ( b ) )

typedef long long lll ;

lll MIN( lll a , lll b ) { return a < b ? a : b ; }
lll MAX( lll a , lll b ) { return a > b ? a : b ; }
int GCD( int a , int b ) { while( b ) b ^= a ^= b ^= a %= b ; return a ; }
int LCM( int a , int b ) { return a * ( b / GCD( a , b ) ) ; }
void SWAP( int &a , int &b ) { a = a ^ b ; b = a ^ b ; a = a ^ b ; }

const double PI = acos( -1 ) ;
const double EPS = 1e-11 ;

struct st {
    lll x , y ;
} arr[ MAX_LENGTH ] , brr[ MAX_LENGTH ] ;

lll memo[ MAX_LENGTH ][ MAX_LENGTH ] , N , M ;
lll crr[ MAX_LENGTH ][ MAX_LENGTH ] , drr[ MAX_LENGTH ][ MAX_LENGTH ] , cn1[ MAX_LENGTH ] , cn2[ MAX_LENGTH ] ;

lll dp( lll i , lll j ) {
    if( i >= N || j >= M ) {
        return 0 ;
    }
    //print2( i , j  ) ;
    lll &ret = memo[ i ][ j ] ;
    if( ret != -1 ) {
        return ret ;
    }
    lll res , r1 , k , l ;
    res = 0 ;
    if( arr[ i ].y == brr[ j ].y ) {
        if( arr[ i ].x != brr[ j ].x ) {
            lll x = lower_bound( crr[ arr[ i ].y ] , crr[ arr[ i ].y ] + cn1[ arr[ i ].y ] , i ) - crr[ arr[ i ].y ] ;
            lll y = lower_bound( drr[ brr[ j ].y ] , drr[ brr[ j ].y ] + cn2[ brr[ j ].y ] , j ) - drr[ brr[ j ].y ] ;
            lll sx , sy ;
            sx = sy = 0 ;
            for( k = x ; k < cn1[ arr[ i ].y ] ; k++ ) {
                lll in1 = crr[ arr[ i ].y ][ k ] ;
                sx += arr[ in1 ].x ;
                sy = 0 ;
                for( l = y ; l < cn2[ brr[ j ].y ] ; l++ ) {
                    lll in2 = drr[ brr[ j ].y ][ l ] ;
                    sy += brr[ in2 ].x ;
                    r1 = dp( in1 + 1 , in2 + 1 ) + MIN( sx , sy ) ;
                    res = MAX( res , r1 ) ;
                }
            }
        }
        r1 = dp( i + 1 , j + 1 ) + MIN( arr[ i ].x , brr[ j ].x ) ;
        res = MAX( res , r1 ) ;
    }
    r1 = dp( i + 1 , j ) ;
    res = MAX( res , r1 ) ;
    r1 = dp( i , j + 1 ) ;
    res = MAX( res , r1 ) ;
    return ret = res ;
}
int main() {
    freopen( "cl.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	lll T , res , n , i , ind , m ;
	scanf( "%lld" , &T ) ;
	fort( 1 , T ) {
        CLR( arr ) ;
        CLR( brr ) ;
        CLR( crr ) ;
        CLR( drr ) ;
        CLR( cn1 ) ;
        CLR( cn2 ) ;
        MEM( memo ) ;
		scanf( "%lld" , &n ) ;
		scanf( "%lld" , &m ) ;
		N = n ;
		fori( n ) {
		    scanf( "%lld%lld" , &arr[ i ].x , &arr[ i ].y ) ;
		    crr[ arr[ i ].y ][ cn1[ arr[ i ].y ] ] = i ;
		    cn1[ arr[ i ].y ]++ ;
		}
		M = m ;
		fori( m ) {
		    scanf( "%lld%lld" , &brr[ i ].x , &brr[ i ].y ) ;
		    drr[ brr[ i ].y ][ cn2[ brr[ i ].y ] ] = i ;
		    cn2[ brr[ i ].y ]++ ;
		}
        res = dp( 0 , 0 ) ;
		printf( "Case #%lld: %lld\n" , ind , res ) ;
	}
	return 0 ;
}
