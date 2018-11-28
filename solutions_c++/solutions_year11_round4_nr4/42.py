#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int TestCase , Case , N , M , D[ 444 ] , Q[ 444 ] , F[ 444 ][ 444 ] ;
bool G[ 444 ][ 444 ] ;

inline int Count( int u , int v  )
{
	int ret = 0 ;
	if ( v == 1 ) {
		for ( int i = 0 ; i < N ; i ++ )
		if ( u != i && v != i && D[ i ] == D[ v ] ) {
			if ( G[ u ][ i ] ) ret ++ ;
		}
	} else {
		for ( int i = 0 ; i < N ; i ++ )
		if ( u != i && v != i && D[ i ] == D[ v ] ) {
			if ( G[ u ][ i ] || G[ v ][ i ] ) ret ++ ;
		}
	}
	return ret ;
}

inline int Calc( int u , int v , int w )
{
	int ret = 0 ;
	if ( w == 1 ) {
		for ( int i = 0 ; i < N ; i ++ )
		if ( u != i && v != i && D[ i ] == D[ v ] ) {
			if ( G[ u ][ i ] || G[ v ][ i ] ) ret ++ ;
		}
	} else {
		for ( int i = 0 ; i < N ; i ++ )
		if ( u != i && v != i && D[ i ] == D[ v ] ) {
			if ( G[ u ][ i ] || G[ v ][ i ] || G[ w ][ i ] ) ret ++ ;
		}
	}
	return ret ;
}

int main()
{
	freopen( "D.in" , "r" , stdin ) ;
	freopen( "D.out" , "w" , stdout ) ;
	scanf( "%d" , &TestCase ) ;
	for ( ; TestCase -- ; ) {
		scanf( "%d%d" , &N , &M ) ;
		memset( G , 0 , sizeof( G ) ) ;
		for ( int i = 0 ; i < M ; i ++ ) {
			int x , y ;
			scanf( "%d,%d" , &x , &y ) ;
			G[ x ][ y ] = G[ y ][ x ] = true ;
		}
		memset( D , -1 , sizeof( D ) ) ;
		int Head = 0 , Tail = 1 ;
		Q[ 1 ] = 0 ; D[ 0 ] = 0 ;
		for ( ; Head ++ < Tail ; ) {
			int u = Q[ Head ] ;
			for ( int v = 0 ; v < N ; v ++ )
			if ( G[ u ][ v ] && D[ v ] == -1 ) {
				D[ v ] = D[ u ] + 1 ;
				Q[ ++ Tail ] = v ;
			}
		}
		printf( "Case #%d:" , ++ Case ) ;
		printf( " %d" , D[ 1 ] - 1 ) ;
		memset( F , -2 , sizeof( F ) ) ;
		for ( int i = 0 ; i < N ; i ++ )
		if ( G[ i ][ 1 ] && D[ i ] + 1 == D[ 1 ] )
			F[ i ][ 1 ] = Count( i , 1 ) + 1 ;
		for ( int i = Tail ; i >= 1 ; i -- ) {
			int v = Q[ i ] ;
			for ( int u = 0 ; u < N ; u ++ )
			if ( D[ u ] + 1 == D[ v ] && G[ u ][ v ] ) {
				for ( int w = 0 ; w < N ; w ++ )
				if ( F[ v ][ w ] >= 0 ) {
					F[ u ][ v ] >?= F[ v ][ w ] + Calc( u , v , w ) ;
				}
			}
		}
		int Ret = 0 ;
		for ( int i = 0 ; i < N ; i ++ )
		if ( F[ 0 ][ i ] >= 0 ) {
			int Tot = F[ 0 ][ i ] ;
			Tot += Count( i , 0 ) ;
			Ret >?= Tot ;
		}
		printf( " %d\n" , Ret ) ;
	}
	return 0 ;
}
