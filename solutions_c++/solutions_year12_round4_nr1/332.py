//------------------------------------------------------------------------------
//  Problem : 
//  User    : 
//  Date    : 
//------------------------------------------------------------------------------


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
using namespace std;


int D[11111] , L[11111] ;
int N , T ;
int F[11111] ;



int main( int argc , char *argv[] )
{
	freopen( "A-large.in" , "r" ,stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for( int TE = 1 ; TE <= T ; TE++ ) {
		scanf( "%d" , &N ) ;
		for( int i = 0 ; i < N ; i++ ) {
			scanf( "%d%d" , &D[i] , &L[i] ) ;
		}
		scanf( "%d" , &L[N] ) ;
		memset( F , 0 , sizeof( F ) ) ;
		F[0] = D[0] ;
		for( int i = 1 ; i < N ; i++ ) {
			for( int j = 0 ; j < i ; j++ )
			if( F[j] >= D[i] - D[j] ) {
				F[i] = max( F[i] , min( L[i] , D[i] - D[j] ) ) ;
			}
		}
		printf( "Case #%d: " , TE ) ;
		bool flag = 0 ;
		for( int i = 0 ; i < N ; i++ ) 
		if( F[i] >= L[N] - D[i] ) {
			printf( "YES\n" ) ;
			flag = 1 ;
			break ;
		} 
		if( !flag ) {
			printf( "NO\n" ) ;
		}
	}
	return 0;
}
