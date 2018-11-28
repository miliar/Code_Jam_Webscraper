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
int X , S , R , TM , N ;
struct Node {
	int b , e , w ;
}	a[2000] ;

bool cmp( const Node x , const Node y ) {
	return x.w < y.w ;
}

int main() {
	freopen( "A-large.in" , "r" , stdin ) ;
	freopen( "A-large.out" , "w" , stdout ) ;
	int TestCase ;
	scanf( "%d" , &TestCase ) ;
	for ( int t = 0 ; t < TestCase ; t++ ) {
		scanf( "%d%d%d%d%d" , &X , &S , &R , &TM , &N ) ;
		for ( int i = 0 ; i < N ; i ++ )	scanf( "%d%d%d" , &a[i].b , &a[i].e , &a[i].w ) ;
		sort( a , a + N , cmp ) ;
		int LX = 0 ;
		for ( int i = 0 ; i < N ; i ++ )	LX += a[i].e - a[i].b ;
		double tk = ( ( X - LX ) * 1.0 ) / R ;
		double tm = TM , tans = 0 ;
		if ( tm - tk > 1E-8 ){	tans = tans + tk ; tm = tm - tk ; }
		else { tans = tans + tm ; tm = 0 ; }
		double XX = X - tans * R ;
		int j ;
		for ( j = 0 ; j < N ; j++ ) {
			int L = a[j].e - a[j].b ;
			double tnow = ( L * 1.0 ) / ( a[j].w + R ) ;
			if ( tm - tnow > 1E-8 )	{
				tm =  tm - tnow ;
				tans = tans + tnow ;
			}
			else {
				tans = tans + tm ;
				tans = tans + ( L * 1.0 - tm * ( R + a[j].w ) ) / ( S + a[j].w ) ;
				break ;
			}
		}
		
		for ( int i = j + 1 ; i < N ; i++ ) {
			int L = a[i].e-a[i].b ;
			tans = tans + ( L * 1.0 ) / ( a[i].w + S ) ;
		}
		tans = tans + ( ( XX - LX ) * 1.0 ) / S ;
		printf( "Case #%d: %.6lf\n" , t + 1 , tans ) ;
	}
	return 0 ;				
}







