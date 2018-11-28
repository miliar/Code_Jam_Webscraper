// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

#define MAXN 200
#define MAXC 50

char invoke[ MAXN ], combine[ MAXC ][ 3 ], opposed[ MAXC ][ 2 ], list[ MAXN ];
int c, d, n, l;


void init(){
	int i;
	//cin >> c;
	scanf( "%d", &c );
	for ( i = 1; i <= c; i++ ){
		 scanf( "%s", combine[ i ] );
		 //cout << combine[ i ];
	}
	//cout << endl;
	//cin >> d;
	scanf( "%d", &d );
	for ( i = 1; i <= d; i ++ ){
		scanf( "%s", opposed[ i ] );
		//cout << opposed[ i ];
	}
	//cout << endl;
	//cin >> n;
	scanf( "%d", &n );
	scanf( "%s", invoke );
	//cout << invoke << endl;
}

bool opp( char c1, char c2 ){
	int i;
	char o1, o2;
	for ( i = 1; i <= d; i ++ ){
		o1 = opposed[ i ][ 0 ];
		o2 = opposed[ i ][ 1 ];
		if ( o1 == c1 && o2 == c2 || o1 == c2 && o2 == c1 )
			return true;
	}
	return false;
}

char com( char c1, char c2 ){
	int i;
	char o1, o2;
	for ( i = 1; i <= c; i ++ ){
		o1 = combine[ i ][ 0 ];
		o2 = combine[ i ][ 1 ];
		if ( o1 == c1 && o2 == c2 || o1 == c2 && o2 == c1 )
			return( combine[ i ][ 2 ] );
	}
	return 0;
}

void pro_list(){
	int i, j;
	char new_ch;
	bool change1, change2;
	l = 0;
	for ( i = 1; i <= n; i ++ ){
		list[ ++l ] = invoke[ i-1 ];
		change1 = false;
		change2 = true;

		//while ( l > 1 && change2 ){
		if ( l > 1 ){
			change2 = false;
			new_ch = com( list[ l ], list[ l-1 ] );
			if ( new_ch > 0 ){
				list[ --l ] = new_ch;
				change1 = true;
				change2 = true;
			}
		}
		if ( !change1 )
			for ( j = 1; j < l; j ++ )
				if ( opp( list[ l ], list[ j ] ) ){
					l = 0;
					break;
				}
	}
}

void print_(){
	int i;
	cout << "[";
	for ( i = 1; i <= l; i ++ ){
		if ( i > 1 ) cout << ", ";
		cout << list[ i ];
	}
	cout << "]" << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "B-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int i, t;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		init();
		pro_list();
		cout << "Case #" << i << ": ";
		print_();
	}
	return 0;
}

