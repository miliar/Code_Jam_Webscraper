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
#define MAX_LENGTH 100
#define INF ( 1 << 29 ) ;

#define CLR( a ) memset( a , NULL , sizeof( a ) )
#define MEM( a ) memset( a , -1 , sizeof( a ) )
#define fort( a , b ) for( ind = ( a ) ; ind <= ( b ) ; ind++ )
#define foriab( a , b ) for( i = ( a ) ; i < ( b ) ; i++ )
#define fori( a ) for( i = 0 ; i < ( a ) ; i++ )
#define forj( a ) for( j = 0 ; j < ( a ) ; j++ )
#define print1( a ) printf( "%d ---\n" , ( a ) )
#define print2( a , b ) printf( "%d %d ---\n" , ( a ) , ( b ) )

typedef long long lll ;

int MIN( int a , int b ) { return a < b ? a : b ; }
int MAX( int a , int b ) { return a > b ? a : b ; }
int GCD( int a , int b ) { while( b ) b ^= a ^= b ^= a %= b ; return a ; }
int LCM( int a , int b ) { return a * ( b / GCD( a , b ) ) ; }
void SWAP( int &a , int &b ) { a = a ^ b ; b = a ^ b ; a = a ^ b ; }

const double PI = acos( -1 ) ;
const double EPS = 1e-11 ;

int arr[ MAX_LENGTH ] ;

int noofdigits( int n ) {
    int a , b ;
    a = 0 ;
    while( 1 ) {
        a++ ;
        n /= 10 ;
        if( n == 0 ) { break ; }
    }
    return a ;
}

int call( int n , int p ) {
    int a , b , cn , i ;
    cn = 0 ;
    CLR( arr ) ;
    while( 1 ) {
        arr[ cn ] = n % 10 ;
        cn++ ;
        n /= 10 ;
        if( n == 0 ) { break ; }
    }
    a = 1 ;
    b = 0 ;
    for( i = p ; i < cn ; i++ ) {
        b += ( arr[ i ] * a ) ;
        a *= 10 ;
    }
    fori( p ) {
        b += ( arr[ i ] * a ) ;
        a *= 10 ;
    }
    return b ;
}

int main() {
    freopen( "C_small.in" , "r" , stdin ) ;
	freopen( "C_small.ans" , "w" , stdout ) ;
	int T , res , n , i , ind , a , b , nod , j , x , y ;
	double cl = clock() ;
	scanf( "%d" , &T ) ;
	fort( 1 , T ) {
	    map< pair< int , int > , int > M ;
	    pair< int , int > P ;
	    int m_cnt = 1 ;
		scanf( "%d%d" , &a , &b ) ;
		int lim = ( a + b ) / 2 ;
		for( i = a ; i <= b ; i++ ) {
		    nod = noofdigits( i ) ;
		    if( nod > 1 ) {
		        int num = i ;
                for( j = 1 ; j < nod ; j++ ) {
                    x = i ;
                    y = call( num , j ) ;
                    int nod_y = noofdigits( y ) ;
                    if( nod_y == nod && x != y ) {
                        P.first = MIN( x , y ) ;
                        P.second = MAX( x , y ) ;
                        if( x >= a && x <= b && y >= a && y <= b && M.find( P ) == M.end() ) {
                            M[ P ] = m_cnt ;
                            m_cnt++ ;
                        }
                    }
                }
		    }
		}
        res = m_cnt - 1 ;
		printf( "Case #%d: %d\n" , ind , res ) ;
	}
	cl = clock() - cl ;
	//printf( "Total Execution Time: %.5lf\n" , cl / CLOCKS_PER_SEC ) ;
	return 0 ;
}
