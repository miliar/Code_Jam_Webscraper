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
int TestCase , Case , C , D , N , P , V ;
long long A[ 1111111 ] ;

inline bool Check( long long Ans )
{
	long long P = A[ 0 ] - Ans ;
	for ( int i = 1 ; i < N ; i ++ ) {
		P = max( P + D , A[ i ] - Ans ) ;
		if ( P > A[ i ] + Ans ) return false ;
	}
	return true ;
}

int main()
{
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;
	
	scanf( "%d" , &TestCase ) ;
	for ( ; TestCase -- ; ) {
		scanf( "%d%d" , &C , &D ) ;
		D <<= 1 ;
		N = 0 ;
		for ( ; C -- ; ) {
			scanf( "%d%d" , &P , &V ) ;
			P <<= 1 ;
			for ( ; V -- ; A[ N ++ ] = P ) ;
		}
		sort( A , A + N ) ;
		long long Left = -1 , Right = 10000000000000000LL ;
		for ( ; Left + 1 < Right ; ) {
			long long Mid = ( Left + Right ) / 2 ;
			if ( Check( Mid ) ) Right = Mid ;
				else Left = Mid ;
		}
		Check( 1 ) ;
		printf( "Case #%d: %.1lf\n" , ++ Case , Right / 2.0 ) ;
	}
	return 0 ;
}








