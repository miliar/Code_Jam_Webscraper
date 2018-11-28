#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std ;
int TestCase , Case , N , M , U[ 10 ] , V[ 10 ] , Stack[ 10 ]  ;
int ret , res[ 10 ] , c[ 10 ] ;
vector < int > C[ 1111111 ] , E[ 10 ] ;

inline void FindCircle( int u , int d , int p )
{
	if ( V[ u ] ) {
		for ( int i = V[ u ] ; i < d ; i ++ )
			C[ M ].push_back( Stack[ i ] ) ;
		M ++ ;
	} else {
		V[ u ] = d ;
		Stack[ d ] = u ;
		for ( int i = 0 ; i < E[ u ].size() ; i ++ )
		if ( E[ u ][ i ] != p ) FindCircle( E[ u ][ i ] , d + 1 , u ) ;
		V[ u ] = 0 ;
	}
}

inline bool Check( int k )
{
	for ( int i = 0 ; i < M ; i ++ ) {
		memset( V , 0 , sizeof( V ) ) ;
		for ( int j = 0 ; j < C[ i ].size() ; j ++ )
			V[ c[ C[ i ][ j ] ] ] ++ ;
		for ( int j = 1 ; j <= k ; j ++ )
		if ( !V[ j ] ) return false ;
	}
	return true ;
}

inline void Search( int u , int k )
{
	if ( k > 5 ) return ;
	if ( u == N + 1 ) {
		if ( k > ret && Check( k ) ) {
			ret = k ;
			memcpy( res , c , sizeof( c ) ) ;
		}
	} else {
		for ( int i = 1 ; i <= k + 1 ; i ++ ) {
			c[ u ] = i ;
			Search( u + 1 , max( k , i ) ) ;
		}
	}
}

int main()
{
	freopen( "C-small-attempt0.in" , "r" , stdin ) ;
	freopen( "C-small-attempt0.out" , "w" , stdout ) ;
	
	scanf( "%d" , &TestCase ) ;
	for ( ; TestCase -- ; ) {
		scanf( "%d%d" , &N , &M ) ;
		for ( int i = 1 ; i <= N ; i ++ )
			E[ i ].clear() ;
		for ( int i = 1 ; i <= N ; i ++ )
			E[ i ].push_back( i % N + 1 ) ;
		for ( int i = 0 ; i < M ; i ++ )
			scanf( "%d" , &U[ i ] ) ;
		for ( int i = 0 ; i < M ; i ++ )
			scanf( "%d" , &V[ i ] ) ;
		for ( int i = 0 ; i < M ; i ++ ) {
			E[ U[ i ] ].push_back( V[ i ] ) ;
			E[ V[ i ] ].push_back( U[ i ] ) ;
		}
		M = 0 ;
		memset( V , 0 , sizeof( V ) ) ;
		FindCircle( 1 , 1 , 0 ) ;
		ret = 0 ;
		Search( 1 , 0 ) ;
		printf( "Case #%d: %d\n" , ++ Case , ret ) ;
		for ( int i = 1 ; i < N ; i ++ )
			printf( "%d " , res[ i ] );
		printf( "%d\n" , res[ N ] ) ;
		for ( int i = 0 ; i < M ; i ++ )
			C[ i ].clear() ;
	}
	return 0 ;
}








