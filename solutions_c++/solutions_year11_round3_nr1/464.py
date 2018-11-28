// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

#define MAXL 100

char map[ MAXL ][ MAXL ];
int n, m;

void init(){
	scanf( "%d%d\n", &n, &m );
	int i;
	for ( i = 0; i < n; i ++ ){
		gets( map[ i ] );
		//puts( map[ i ] );
	}
}

void print_(){
	int i;
	for ( i = 0; i < n; i ++ )
		puts( map[ i ] );
}

bool solv( int x, int y ){
	if ( x+1 >= n || y+1 >= m ) return false;
	if ( map[ x ][ y+1 ] != '#' || map[ x+1 ][ y ] != '#' || map[ x+1 ][ y+1 ] != '#' )
		return false;

	map[ x ][ y ] = '/';
	map[ x ][ y+1 ] = '\\';
	map[ x+1 ][ y ] = '\\';
	map[ x+1 ][ y+1 ] = '/';
	
	//print_();
	return true;
}

bool find(){
	int i, j;
	for ( i = 0; i < n; i ++ )
		for ( j = 0; j < m; j ++ )
			if ( map[ i ][ j ] == '#' )
				if ( !solv( i,j ) )
					return false;
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
		if ( !find() )
			cout << "Impossible" << endl;
		else
			print_();
	}

	return 0;
}

