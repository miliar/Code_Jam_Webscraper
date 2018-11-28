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
#define MAX_LENGTH 100100
#define INF ( 1 << 29 ) ;

#define CLR( a ) memset( a , NULL , sizeof( a ) )
#define MEM( a ) memset( a , -1 , sizeof( a ) )
#define fort( a , b ) for( ind = ( a ) ; ind <= ( b ) ; ind++ )
#define foriab( a , b ) for( i = ( a ) ; i < ( b ) ; i++ )
#define fori( a ) for( i = 0 ; i < ( a ) ; i++ )
#define forj( a ) for( j = 0 ; j < ( a ) ; j++ )
#define fork( a ) for( k = 0 ; k < ( a ) ; k++ )
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

bool possible( int tot , int p ) {
    int i , j , k , a , b , c , d , ma ;
    fori( 11 ) {
        forj( 11 ) {
            fork( 11 ) {
                a = i + j + k ;
                ma = MAX( i , MAX( j , k ) ) ;
                if( a == tot && ma >= p ) {
                    b = abs( i - j ) ;
                    c = abs( i - k ) ;
                    d = abs( j - k ) ;
                    if( b <= 2 && c <= 2 && d <= 2 ) {
                        return true ;
                    }
                }
            }
        }
    }
    return false ;
}

bool notsurp( int tot , int p ) {
    int i , j , k , a , b , c , d , ma ;
    fori( 11 ) {
        forj( 11 ) {
            fork( 11 ) {
                a = i + j + k ;
                ma = MAX( i , MAX( j , k ) ) ;
                if( a == tot && ma >= p ) {
                    b = abs( i - j ) ;
                    c = abs( i - k ) ;
                    d = abs( j - k ) ;
                    if( b <= 2 && c <= 2 && d <= 2 ) {
                        if( b == 2 || c == 2 || d == 2 ) { }
                        else {
                            return true ;
                        }
                    }
                }
            }
        }
    }
    return false ;
}

int main() {
    freopen( "BL.in" , "r" , stdin ) ;
	freopen( "B_large.ans" , "w" , stdout ) ;
	int T , res , n , i , ind , s , p ;
	scanf( "%d" , &T ) ;
	fort( 1 , T ) {
		scanf( "%d%d%d" , &n , &s , &p ) ;
        res = 0 ;
        fori( n ) {
            scanf( "%d" , &arr[ i ] ) ;
            if( possible( arr[ i ] , p ) && notsurp( arr[ i ] , p ) ) {
                res++ ;
            }
            else {
                if( s > 0 && possible( arr[ i ] , p ) ) {
                    res++ ;
                    s-- ;
                }
            }
        }
		printf( "Case #%d: %d\n" , ind , res ) ;
	}
	return 0 ;
}
