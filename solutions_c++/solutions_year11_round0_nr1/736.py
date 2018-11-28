// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define MAXN 120

int opp[ MAXN ][ 2 ], p[ 2 ], oppi[ 2 ][ MAXN ], o[ 2 ];
int n;

void init(){
	int i, on;
	char ch;
	cin >> n;
	o[ 0 ] = o[ 1 ] = 0;
	for ( i = 1; i <= n; i ++ ){
		cin >> ch >> opp[ i ][ 1 ];
		if ( ch == 'O' )
			opp[ i ][ 0 ] = 0;
		else
			opp[ i ][ 0 ] = 1;
		on = opp[ i ][ 0 ];
		oppi[ on ][ ++o[ on ] ] = opp[ i ][ 1 ];
	}
	/*
	for ( i = 1; i <= n; i ++ )
		cout << opp[ i ][ 0 ] << opp[ i ][ 1 ] << endl;
	*/
}

void cal(){
	int i, ti, op_now[ 2 ], per, other, gt, t, dest;
	t = 0;
	p[ 0 ] = p[ 1 ] = 1;
	op_now[ 0 ] = op_now[ 1 ] = 0;
	
	for ( i = 1; i <= n; i ++ ){
		per = opp[ i ][ 0 ];
		gt = opp[ i ][ 1 ];
		op_now[ per ] ++;
		other = 1 - per;

		ti = abs( gt - p[ per ] )+1;
		if ( op_now[ other ]+1 <= o[ other ] ){
			dest = oppi[ other ][ op_now[ other ]+1 ];
			if ( p[ other ] < dest )
				if ( p[ other ] + ti <= dest )
					p[ other ] += ti;
				else
					p[ other ] = dest;
			else
				if ( p[ other ] - ti >= dest )
					p[ other ] -= ti;
				else
					p[ other ] = dest;
		}

		p[ per ] = gt;
		t += ti;
	}
	cout << t << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}

