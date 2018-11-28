/*
ID: summerd1
PROG:
LANG: C++
*/
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
int mp[510][510] , mm[510][510] ;
struct Node{ 
	double x , y ;
}	v[510][510] , v1[510][510] ;

double half( int x ) {
	return ( 2 * x + 1 ) * 1.0 / 2 ;
}

int R , C , D ; 

bool check( int x , int y , int k ) {
	if ( x + k > R ) return false ;
	if ( y + k > C ) return false ;
	
	return true ;
}

int main() {
	freopen( "B-small-attempt0.in" , "r" , stdin ) ;
	freopen( "B-small-attempt0.out" , "w" , stdout ) ;
	int TestCase ;
	scanf( "%d" , &TestCase ) ;
	for ( int tt = 0 ; tt < TestCase ; tt++ ) {
		scanf( "%d%d%d" , &R , &C , &D ) ;
		char a[600] ;
		gets( a ) ;
		memset( v , 0 , sizeof( v ) ) ;
		for ( int i = 1 ; i <= R ; i++ ) {
			gets( a ) ;
			for ( int j = 1 ; j <= C ; j++ ) {
				int xx = a[j-1] - '0' ;
				mp[i][j] = xx ;
				mp[i][j] += D ;
				mm[i][j] = mp[i][j] ;
				v[i][j].x = mp[i][j] * half( i ) ;
				v[i][j].y = mp[i][j] * half( j ) ;
				v1[i][j].x = mp[i][j] * half( i ) ;
				v1[i][j].y = mp[i][j] * half( j ) ;
			
			}
		}
			
		
		for ( int i = 1 ; i <= R ; i++ )
		for ( int j = 1 ; j <= C ; j++ ) {
			v[i][j].x += v[i-1][j].x + v[i][j-1].x - v[i-1][j-1].x ;
			v[i][j].y += v[i-1][j].y + v[i][j-1].y - v[i-1][j-1].y ;
			mp[i][j] += mp[i-1][j] + mp[i][j-1] - mp[i-1][j-1] ;
		}
		int P = min( R , C ) ;
		bool flag = true ;
		for ( int k = P ; k >= 1 ; k-- )
		for ( int i = 1 ; i <= R ; i++ ) {
			if ( !flag ) break ;
			for ( int j = 1 ; j <= C ; j++ ) {
				if ( !flag ) break ;
				
				if ( check( i , j , k ) ) {
					int M = mp[i+k][j+k] - mp[i+k][j-1] - mp[i-1][j+k] + mp[i-1][j-1] 
							- mm[i+k][j+k] - mm[i+k][j] - mm[i][j+k] - mm[i][j] ;
					double VX = v[i+k][j+k].x - v[i+k][j-1].x - v[i-1][j+k].x + v[i-1][j-1].x 
								- v1[i+k][j+k].x - v1[i+k][j].x - v1[i][j+k].x - v1[i][j].x ;
					double VY = v[i+k][j+k].y - v[i+k][j-1].y - v[i-1][j+k].y + v[i-1][j-1].y 
								- v1[i+k][j+k].y - v1[i+k][j].y - v1[i][j+k].y - v1[i][j].y ;
					VX = VX / M ;
					VY = VY / M ;
					double CX = ( 2 * i + k + 1 ) * 1.0 / 2 ;
					double CY = ( 2 * j + k + 1 ) * 1.0 / 2 ;
					
					if ( fabs( VX - CX ) < 1E-8 && fabs( VY - CY ) < 1E-8 ) {
						printf( "Case #%d: %d\n" , tt + 1 , k + 1 ) ;
						flag = false ;
						break ;
					}
				}
			}
		}
		if ( flag ) printf( "Case #%d: IMPOSSIBLE\n" , tt + 1 ) ;
	}
	return 0 ; 
}







