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

struct Node {
	int x , y ;
} R[1111] , Ans[1111] ;

int T , N , W , L ;
bool v[1111] ;


bool cmp( const Node &a , const Node &b ) {
	return a.x > b.x ;
}

bool cmp1( const Node &a , const Node &b ) {
	return a.y < b.y ;
}



int main( int argc , char *argv[] )
{
	freopen( "B-large.in" , "r" , stdin ) ;
	freopen( "B-large.out" , "w" , stdout ) ;
	scanf( "%d" , &T ) ;
	for( int TE = 1 ; TE <= T ; TE++ ) {
		scanf( "%d%d%d" , &N , &W , &L ) ;
		for( int i = 0 ; i < N ; i++ ) {
			scanf( "%d" , &R[i].x ) ;
			R[i].y = i ;
		}
		sort( R , R + N , cmp ) ;
		bool flag = 0 ;
		if( W > L ) {
			swap( W , L ) ;
			flag = 1 ;
		}
		
		memset( v , 0 , sizeof( v ) ) ;
		int n = N ;
		int l = L , w = W ;
		int k = 0 ;
		int w1 = 0 ;
		while( n ) {
			for( int i = 0 ; i < N ; i++ )
			if( !v[R[i].y] && l >= R[i].x ) {
				if( l == L ) {
					if( k != 0 ) {
						w -= R[i].x ;
					}
					Ans[R[i].y].x = w ;
					Ans[R[i].y].y = L - l ;
					l -= R[i].x ;
					v[R[i].y] = 1 ;
					w1 = w - R[i].x ;
					n-- ;
				} else {
					if( l > ( R[i].x << 1 ) ) {
						n-- ;
						Ans[R[i].y].x = w ;
						Ans[R[i].y].y = L - l + R[i].x ;
						l -= R[i].x << 1 ;
						v[R[i].y] = 1 ;
					} else {
						n-- ;
						v[R[i].y] = 1 ;
						Ans[R[i].y].x = w ;
						Ans[R[i].y].y = L ;
						break ;
					}
				}
			}
			l = L ;
		 	w = w1 ;
		 	k = 1 ;
		}
		sort( R , R + N , cmp1 ) ;
		printf( "Case #%d: " , TE ) ;
		for( int i = 0 ; i < N ; i++ ) { 
			if( flag ) {
				swap( Ans[i].x , Ans[i].y ) ;
			}
			printf( "%d %d" , Ans[i].x , Ans[i].y ) ;
			if( i < N -1 ) {
				printf( " " ) ;
			} else {
				printf( "\n" ) ;
			}
		}
	}
			
						
					
				
		
	return 0;
}
