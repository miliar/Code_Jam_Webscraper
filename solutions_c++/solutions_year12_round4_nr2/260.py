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
int TestCase , N , W , L , RR[1111] ;
pair < int , int > R[1111] ;
int ansX[1111] , ansY[1111] ;

inline bool Check()
{
	for ( int i = 0 ; i < N ; i ++ ) {
		if ( ansX[i] < 0 || ansX[i] > W ) {
			printf( "%d %d\n" , W , L ) ;
			printf( "%d %d %d\n" , ansX[i] , ansY[i] , RR[i] ) ;
			return false ;
		}
		if ( ansY[i] < 0 || ansY[i] > L ) return false ;
		for ( int j = i + 1 ; j < N ; j ++ ) {
			long long DX = ansX[i] - ansX[j] ;
			long long DY = ansY[i] - ansY[j] ;
			long long DR = RR[i] + RR[j] ;
			if ( DX * DX + DY * DY < DR * DR ) {
				printf( "%d %d\n" , i , j ) ;
				printf( "%d %d %d\n" , ansX[i] , ansY[i] , RR[i] ) ;
				printf( "%d %d %d\n" , ansX[j] , ansY[j] , RR[j] ) ;
				return false ;
			}
		}
	}
	return true ;
}

int main( int argc, char *argv[] )
{
	freopen( "input.txt" , "r" , stdin ) ;
	freopen( "output.txt" , "w" , stdout ) ;
	scanf( "%d" , &TestCase ) ;
	for ( int Case = 1 ; Case <= TestCase ; Case ++ ) {
		scanf( "%d%d%d" , &N , &W , &L ) ;
		for ( int i = 0 ; i < N ; i ++ ) {
			scanf( "%d" , &R[i].first ) ;
			R[i].second = i ;
			RR[i] = R[i].first ;
		}
		sort( R , R + N ) ;
		reverse( R , R + N ) ;
		int X = -1000000000 , Y = 0 ;
		memset( ansX , -1 , sizeof( ansX ) ) ;
		for ( int i = 0 ; i < N ; ) {
			X = max( X + R[i].first , 0 ) ;
			ansX[R[i].second] = X ;
			ansY[R[i].second] = 0 ;
			int minX = X - R[i].first ;
			int maxX = X + R[i].first ;
			Y = R[i].first ;
			for ( i ++ ; i < N ; ) {
				if ( Y + R[i].first > L ) break ;
				int DY = R[i].first ;
				int x = minX ;
				for ( ; i < N ; i ++ ) {
					x = max( x + R[i].first , 0 ) ;
					if ( x + R[i].first > maxX ) break ;
					if ( x > W ) break ;
					ansX[R[i].second] = x ;
					ansY[R[i].second] = Y + R[i].first ;
					x += R[i].first ;
				}
				Y += 2 * DY ;
			}
			X = maxX ;
		}
		printf( "Case #%d:" , Case ) ;
		for ( int i = 0 ; i < N ; i ++ ) {
			printf( " %d %d" , ansX[i] , ansY[i] ) ;
		}
		printf( "\n" ) ;
		if ( !Check() ) {
			printf( "xxxxxxxxxxxxxxxxx\n" ) ;
		}
	}
	return 0;
}
