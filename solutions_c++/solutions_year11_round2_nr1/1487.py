// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>

using namespace std;

#define MAXN 120

int map[ MAXN ][ MAXN ];
double p1[ MAXN ], p2[ MAXN ], p3[ MAXN ], rpi[ MAXN ];
int n;
char s[ MAXN ];

void init(){
	int i, j;
	//cin >> n;
	scanf( "%d\n", &n );
	for ( i = 1; i <= n; i ++ ){
		gets( s );
		for ( j = 0; j < n; j ++ ){
			if ( s[j] == '0' ) 
				map[i][j+1] = 0;
			if ( s[j] == '1' )
				map[i][j+1] = 1;
			if ( s[j] == '.' )
				map[i][j+1] = 2;
		}
	}
	/*
	for ( i = 1; i <= n; i ++ ){
		for ( j = 1; j <= n; j ++ )
			cout << map[i][j];
		cout << endl;
	}
	*/
}

void cal_1( int k ){
	int i, a = 0, b = 0;
	for ( i = 1; i <= n; i ++ ){
		if ( map[ k ][ i ] < 2 )
			b ++;
		if ( map[ k ][ i ] == 1 )
			a ++;
	}
	p1[ k ] = a*1.0/b;
}

void cal_2( int k ){
	int i, j, a, b, c = 0;
	p2[ k ] = 0;
	for ( i = 1; i <= n; i ++ ){
		if ( map[ k ][ i ] < 2 ){
			a = 0;
			b = 0;
			c++;
			for ( j = 1; j <= n; j ++ )
				if ( j !=  k ){
					if ( map[ i ][ j ] < 2 )
						b++;
					if ( map[ i ][ j ] == 1 )
						a++;
				}
			p2[ k ] += a*1.0/b;
		}
	}
	p2[ k ] /= c*1.0;
}

void cal_3( int k ){
	int i, c = 0;
	p3[ k ] = 0;
	for ( i = 1; i <= n; i ++ )
		if ( map[ k ][ i ] < 2 ){
			c++;
			p3[ k ] += p2[ i ];
		}
	p3[ k ] /= c;
}


void cal(){
	for ( int i = 1; i <= n; i ++ ){
		cal_1( i );
		cal_2( i );
	}
	for ( int i = 1; i <= n; i ++ ){
		cal_3( i );
		rpi[ i ] = 0.25 * p1[ i ] + 0.5 * p2[ i ] + 0.25 * p3[ i ];
		// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
		//printf( "%.12lf %.12lf %.12lf ", p1[ i ], p2[ i ], p3[ i ] );
		printf( "%.12lf\n", rpi[ i ] );
	}
}
	

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ":" << endl;
		cal();
	}
	return 0;
}

