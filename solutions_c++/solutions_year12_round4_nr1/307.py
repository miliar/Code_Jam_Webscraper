#include <map>
#include <set>
#include <list>
#include <ctime>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std ;
#define LS(t) ((t)<<1)
#define RS(t) (((t)<<1)+1)
#define MD(l,r) (((l)+(r))>>1)
#define PI 3.1415926535897932384626433832795
int N , M , F[11111] , D[11111] , L[11111] ;

int main( int argc, char *argv[] )
{
	freopen( "input.txt" , "r" , stdin ) ;
	freopen( "output.txt" , "w" , stdout ) ;
	int TestCase , nCase = 0 ;
	scanf( "%d" , &TestCase ) ;
	while ( TestCase -- ) {
		scanf( "%d" , &N ) ;
		for ( int i = 0 ; i < N ; i ++ ) {
			scanf( "%d%d" , &D[i] , &L[i] ) ;
		}
		scanf( "%d" , &M ) ;
		memset( F , -1 , sizeof( F ) ) ;
		F[0] = D[0] ;
		bool bRet = false ;
		for ( int i = 0 ; i < N ; i ++ ) {
			F[i] = min( F[i] , L[i] ) ;
			if ( D[i] + F[i] >= M ) bRet = true ;
			for ( int j = i + 1 ; j < N ; j ++ )
			if ( D[i] + F[i] >= D[j] ) {
				F[j] = max( F[j] , D[j] - D[i] ) ;
			}
		}
		printf( "Case #%d: " , ++ nCase ) ;
		if ( bRet ) {
			printf( "YES\n" ) ;
		} else {
			printf( "NO\n" ) ;
		}
	}
	return 0;
}
