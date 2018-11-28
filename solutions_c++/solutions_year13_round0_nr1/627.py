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
#define MAX_LENGTH 1010
#define INF ( 1 << 29 )

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

char arr[ MAX_LENGTH ][ MAX_LENGTH ] ;
char brr[ MAX_LENGTH ] ;

int main() {
    freopen( "al.in" , "r" , stdin ) ;
	freopen( "out.txt" , "w" , stdout ) ;
	int T , res , n , i , ind , j , z , b , c ;
	scanf( "%d" , &T ) ;
	fort( 1 , T ) {
        CLR( arr ) ;
        n = 4 ;
        fori( n ) {
            scanf( "%s" , &arr[ i ] ) ;
        }
        res = -1 ;
        if( res < 1 ) {
            fori( n ) {
                CLR( brr ) ;
                forj( n ) {
                    brr[ arr[ i ][ j ] ]++ ;
                }
                if( brr[ 'X' ] == 4 || ( brr[ 'X' ] == 3 && brr[ 'T' ] == 1 ) ) {
                    res = 1 ;
                    break ;
                }
                if( brr[ 'O' ] == 4 || ( brr[ 'O' ] == 3 && brr[ 'T' ] == 1 ) ) {
                    res = 2 ;
                    break ;
                }
                if( res >= 1 ) { break ; }
            }
        }
        if( res < 1 ) {
            forj( n ) {
                CLR( brr ) ;
                fori( n ) {
                    brr[ arr[ i ][ j ] ]++ ;
                }
                if( brr[ 'X' ] == 4 || ( brr[ 'X' ] == 3 && brr[ 'T' ] == 1 ) ) {
                    res = 1 ;
                    break ;
                }
                if( brr[ 'O' ] == 4 || ( brr[ 'O' ] == 3 && brr[ 'T' ] == 1 ) ) {
                    res = 2 ;
                    break ;
                }
                if( res >= 1 ) { break ; }
            }
        }
        if( res < 1 ) {
            CLR( brr ) ;
            fori( n ) {
                brr[ arr[ i ][ i ] ]++ ;
            }
            if( brr[ 'X' ] == 4 || ( brr[ 'X' ] == 3 && brr[ 'T' ] == 1 ) ) {
                res = 1 ;
            }
            if( brr[ 'O' ] == 4 || ( brr[ 'O' ] == 3 && brr[ 'T' ] == 1 ) ) {
                res = 2 ;
            }
        }
        if( res < 1 ) {
            CLR( brr ) ;
            fori( n ) {
                brr[ arr[ i ][ n - i - 1 ] ]++ ;
            }
            if( brr[ 'X' ] == 4 || ( brr[ 'X' ] == 3 && brr[ 'T' ] == 1 ) ) {
                res = 1 ;
            }
            if( brr[ 'O' ] == 4 || ( brr[ 'O' ] == 3 && brr[ 'T' ] == 1 ) ) {
                res = 2 ;
            }
        }
        if( res < 1 ) {
            CLR( brr ) ;
            fori( n ) {
                forj( n ) {
                    brr[ arr[ i ][ j ] ]++ ;
                }
            }
            if( brr[ '.' ] == 0 ) {
                res = 0 ;
            }
        }
        if( res == -1 ) {
            printf( "Case #%d: Game has not completed\n" , ind ) ;
        }
        else if( res == 0 ) {
            printf( "Case #%d: Draw\n" , ind ) ;
        }
        else if( res == 1 ) {
            printf( "Case #%d: X won\n" , ind ) ;
        }
        else {
            printf( "Case #%d: O won\n" , ind ) ;
        }
	}
	return 0 ;
}
