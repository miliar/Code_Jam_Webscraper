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
#define MAX_LENGTH 110
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

int arr[ MAX_LENGTH ][ MAX_LENGTH ] , brr[ MAX_LENGTH ] , crr[ MAX_LENGTH ][ MAX_LENGTH ] , drr[ MAX_LENGTH ][ MAX_LENGTH ] , err[ MAX_LENGTH ] , frr[ MAX_LENGTH ] , cap[ MAX_LENGTH ][ MAX_LENGTH ] ;
vector< int > adj_list[ MAX_LENGTH ] ;

int dinic( int n , int source , int sink ) {
    int prev[ MAX_LENGTH ] , que[ MAX_LENGTH ] , head , tail , i , u , v , z , flow , mflow ;
    mflow = 0 ;
    while( 1 ){
        MEM( prev ) ;
        head = tail = 0 ;
        prev[ source ] = -2 ;
        que[ tail ] = source ;
        tail += 1 ;
        while( tail !=  head && prev[ sink ] == -1 ) {
           u = que[ head ] ;
           head += 1 ;
           fori( adj_list[ u ].size() ) {
               v = adj_list[ u ][ i ] ;
               if( prev[ v ] == -1 && cap[ u ][ v ] ) {
                   prev[ v ] = u ;
                   que[ tail ] = v ;
                   tail += 1 ;
               }
           }
        }
        if( prev[ sink ] == -1 ) { break ; }
        for( z = 0 ; z < n ; z++ ) {
            if( prev[ z ] != -1 && cap[ z ][ sink ] ) {
                flow = cap[ z ][ sink ] ;
                for( v = z , u = prev[ v ] ; u >= 0 ; v = u , u = prev[ v ] ) {
                    flow = MIN( flow , cap[ u ][ v ] ) ;
                }
                if( flow == 0 ) { continue ; }
                cap[ z ][ sink ] -= flow ;
                cap[ sink ][ z ] += flow ;
                for( v = z , u = prev[ v ] ; u >= 0 ; v = u , u = prev[ v ] ) {
                    cap[ u ][ v ] -= flow ;
                    cap[ v ][ u ] += flow ;
                }
                mflow += flow ;
            }
        }
    }
    return mflow ;
}

void make( int u , int v , int c ) {
    adj_list[ u ].push_back( v ) ;
    adj_list[ v ].push_back( u ) ;
    cap[ u ][ v ] = c ;
    cap[ v ][ u ] = 0 ;
}

int main() {
    freopen( "aas.in" , "r" , stdin ) ;
	freopen( "dout.txt" , "w" , stdout ) ;
	int T , res , n , i , ind , j , m , u , v ;
	scanf( "%d" , &T ) ;
	fort( 1 , T ) {
		scanf( "%d" , &n ) ;
		CLR( arr ) ;
		fori( n ) {
		    scanf( "%d" , &m ) ;
		    forj( m ) {
		        scanf( "%d" , &v ) ;
		        u = i + 1 ;
		        arr[ u ][ v ] = 1 ;
		    }
		}
		bool fl =  0 ;
		fori( n ) {
		    forj( n ) {
		        int k , l ;
		        for( k = 0 ; k < MAX_LENGTH ; k++ ) { adj_list[ k ].clear() ; }
		        CLR( cap ) ;
		        for( k = 0 ; k < n ; k++ ) {
		            for( l = 0 ; l < n ; l++ ) {
		                if( k != l ) {
		                    if( arr[ k + 1 ][ l + 1 ] == 1 ) {
		                        //print2( k + 1 , l + 1 ) ;
		                        make( k + 1 , l + 1 , 1 ) ;
		                    }
		                }
		            }
		        }
		        if( i != j ) {
		            int source = 0 ;
		            int sink = n + 1 ;
		            int N = n + 5 ;
		            make( source , i + 1 , 2 ) ;
		            make( j + 1 , sink , 2 ) ;
                    res = dinic( N , source , sink ) ;
                    //print1( res ) ;
                    if( res >= 2 ) {
                        fl = 1 ;
                        break ;
                    }
		        }
		    }
		    if( fl == 1 ) {
		        break ;
		    }
		}
        if( fl == 1 ) {
		    printf( "Case #%d: Yes\n" , ind ) ;
		}
		else {
		    printf( "Case #%d: No\n" , ind ) ;
		}
	}
	return 0 ;
}
