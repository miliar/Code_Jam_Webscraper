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

char arr[ MAX_LENGTH ] ;
char brr[ MAX_LENGTH ] ;
char res[ MAX_LENGTH ] ;

int main() {
    freopen( "A_small.in" , "r" , stdin ) ;
	freopen( "A_small.ans" , "w" , stdout ) ;
	int T , n , i , ind , a , len ;
	CLR( brr ) ;
	char crr[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi" ;
	char drr[] = "our language is impossible to understand" ;
	len = strlen( crr ) ;
	fori( len ) {
	    if( crr[ i ] != ' ' ) {
	        brr[ crr[ i ] ] = drr[ i ] ;
	    }
	}
	char err[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" ;
	char frr[] = "there are twenty six factorial possibilities" ;
	len = strlen( err ) ;
	fori( len ) {
	    if( err[ i ] != ' ' ) {
	        brr[ err[ i ] ] = frr[ i ] ;
	    }
	}
	char grr[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv" ;
	char hrr[] = "so it is okay if you want to just give up" ;
	len = strlen( grr ) ;
	fori( len ) {
	    if( grr[ i ] != ' ' ) {
	        brr[ grr[ i ] ] = hrr[ i ] ;
	    }
	}
	brr[ 'a' + 17 - 1 ] = 'a' + 26 - 1 ;
	brr[ 'a' + 26 - 1 ] = 'a' + 17 - 1 ;
	scanf( "%d" , &T ) ;
	getchar() ;
	fort( 1 , T ) {
        CLR( arr ) ;
        CLR( res ) ;
		gets( arr ) ;
		int len = strlen( arr ) ;
		printf( "Case #%d: " , ind ) ;
		fori( len ) {
		    if( arr[ i ] == ' ' ) {
		        printf( "%c" , arr[ i ] ) ;
		    }
		    else {
		        res[ i ] = brr[ arr[ i ] ] ;
		        printf( "%c" , res[ i ] ) ;
		    }
		}
		printf( "\n" ) ;
	}
	for( i = 'a' ; i <= 'z' ; i++ ) {
	    if( brr[ i ] == 0 ) {
	        //print1( i ) ;
	    }
	}
	return 0 ;
}
