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
int TestCase , Case , M , Q[ 1111111 ] ;
long long N ;
bool P[ 1111111 ] ;

int main()
{
	freopen( "C.in" , "r" , stdin ) ;
	freopen( "C.out" , "w" , stdout ) ;
	memset( P , 1 , sizeof( P ) ) ;
	for ( int i = 2 ; i <= 1000000 ; i ++ )
	if ( P[ i ] ) {
		Q[ M ++ ] = i ;
		for ( int j = i + i ; j <= 1000000 ; j += i )
			P[ j ] = false ;
	}
	scanf( "%d" , &TestCase ) ;
	for ( ; TestCase -- ; ) {
		printf( "Case #%d:" , ++ Case ) ;
		scanf( "%lld" , &N ) ;
		int Ret = 0 ;
		for ( int i = 0 ; i < M ; i ++ ) {
			long long X = Q[ i ] ;
			long long Y = X * X ;
			for ( ; Y <= N ; Y *= X , Ret ++ ) ;
		}
		if ( N > 1 ) Ret ++ ;
		printf( " %d\n" , Ret ) ;
	}
	return 0 ;
}
