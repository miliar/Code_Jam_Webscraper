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
int a[ 2000 ] ;

int main(){
	freopen( "C-large.in" , "r" , stdin ) ;
	freopen( "C-large.out" , "w" , stdout ) ;
	int tt ;
	scanf( "%d" , &tt ) ;
	int n ;
	for ( int t = 0 ; t < tt ; t ++ ){
		scanf( "%d" , &n ) ;
		memset( a , 0 , sizeof( a ) ) ;
		for ( int j = 0 ; j < n ; j ++ )	scanf( "%d" , &a[ j ] ) ;
		int s = 0 , sum = 0 , mini = 10000000 ;
		for ( int j = 0 ; j < n ; j ++ )	{ s = s^a[ j ] ; sum += a[ j ] ; mini = min( mini , a[ j ] ) ;}
		if ( s != 0 )
			printf( "Case #%d: NO\n" , t + 1 ) ;
		else	printf( "Case #%d: %d\n" , t + 1 , sum - mini ) ;
	}
	return 0 ;
			 
		
}







