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
bool b[ 2000 ] ;
int a[ 2000 ] ;

void sch( int i , int &c ){
	if ( i == a[ i ] || b[ i ]) return ;
	b[ i ] = true ;
	c ++ ;
	sch( a[ i ] , c ) ;
}

int main(){
	freopen( "D-large.in" , "r" , stdin ) ;
	freopen( "D-large.out" , "w" , stdout ) ;
	
	int tt ;
	scanf( "%d" , &tt ) ;
	for ( int t = 1 ; t <= tt ; t ++ ){
		int n ;
		scanf( "%d" , &n ) ;
		memset( a , 0 , sizeof( a ) ) ;
		memset( b , 0 , sizeof( b ) ) ;
		int sum = 0 ;
		for ( int i = 1 ; i <= n ; i ++ ) scanf( "%d" , &a[ i ] ) ;
		for ( int i = 1 ; i <= n ; i ++ )
			if ( !b[ i ] ){
				int c = 0 ;
				sch( a[ i ] , c ) ;
				if ( c != 1 ) sum += c ;
			}
		printf( "Case #%d: %d.000000\n" , t , sum ) ;
	}
	return 0 ;
}







