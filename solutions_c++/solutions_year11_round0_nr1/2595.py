#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int n , a[ 2 ][ 111 ] , na[ 2 ] , tn[ 111 ];

int solve(){
	
	na[ 0 ] = na[ 1 ] = 0;
	
	scanf( "%d" ,&n );
	for( int q = 0 ; q < n ; q++ ){
		char aa;
		int d;
		scanf( " %c%d" ,&aa ,&d );
		if( aa == 'O' ){
			a[ 0 ][ na[ 0 ] ++ ] = d;
			tn[ q ] = 0;
		}
		else{
			a[ 1 ][ na[ 1 ] ++ ] = d;
			tn[ q ] = 1;
		}
	}
	
	int ret = 0;
	
	for( int f = 0 ; f < 2 ; f++ ){
		for( int q = na[ f ] - 1 ; q > 0 ; q-- ){
			a[ f ][ q ] = abs( a[ f ][ q ] - a[ f ][ q - 1 ] );
		}
		a[ f ][ 0 ] --;
	}
	
	int pp = 0 , p[ 2 ];
	p[ 0 ] = p[ 1 ] = 0;
	
	while( p[ 0 ] < na[ 0 ] && p[ 1 ] < na[ 1 ] ){
		bool turn = tn[ pp ];
		if( a[ turn ][ p[ turn ] ] == 0 ){
			p[ turn ] ++;
			pp ++;
			ret ++;
			if( a[ !turn ][ p[ !turn ] ] ) a[ !turn ][ p[ !turn ] ] --;
			continue;
		}
		if( a[ !turn ][ p[ !turn ] ] == 0 ){
			ret += a[ turn ][ p[ turn ] ];
			a[ turn ][ p[ turn ] ] = 0;
			continue;
		}
		int move = min( a[ 0 ][ p[ 0 ] ] , a[ 1 ][ p[ 1 ] ] );
		ret += move;
		a[ 0 ][ p[ 0 ] ] -= move;
		a[ 1 ][ p[ 1 ] ] -= move;
	}
	
	for( int f = 0 ; f < 2 ; f++ ){
		if( p[ f ] < na[ f ] ){
			ret += na[ f ] - p[ f ];
			for( int q = p[ f ] ; q < na[ f ] ; q++ ){
				ret += a[ f ][ q ];
			}
		}
	}
	
	return ret;
}

int main(){
	
	int t;
	scanf( "%d" ,&t );
	
	for( int q = 1 ; q <= t ; q++ ){
		int ans = solve();
		printf( "Case #%d: %d\n" ,q ,ans );
	}
	
	return 0;
}

