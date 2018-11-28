// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>

using namespace std;

#define MAXN 2000
#define MAXN 2000
#define MAXL 20

long long dis[ MAXN ], dc[ MAXN ], use[ MAXL ];
long long l, n, c, t, min_t = 0;

void init(){
	cin >> l >> t >> n >> c;
	int i;
	for ( i = 1; i <= c; i ++ )
		cin >> dc[ i ];
	
	dis[ 0 ] = 0;
	for ( i = 1; i <= n; i ++ ){
		dis[ i ] = dis[ i-1 ] + dc[ (i-1)%c+1 ];
		//cout << dis[ i ] << " ";
	}
	//cout << endl;

	use[ 0 ] = -1;
	min_t = 0;
}

void cal(){
	int i;
	long long p, time = 0, time_d = 0;
	for ( i = 1; i <= l; i ++ ){
		p = use[ i ];
		time = dis[ p ]*2-time_d;
		if ( t <= time )
			time_d += dis[ p+1 ]-dis[ p ];
		if ( t > time && t < dis[ p+1 ]*2-time_d )
			time_d += dis[ p+1 ]- dis[ p ] - ( t-time )/2;
	}

	time = dis[ n ]*2 - time_d;
	if ( min_t == 0 || time < min_t )
		min_t = time;
}


void try_( int k ){
	int i;
	for ( i = use[ k-1 ]+1; i < n; i ++ ){
		use[ k ] = i;
		if ( k < l )
			try_( k + 1 );
		else
			cal();
	}
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		if ( l == 0 )
			cout << dis[ n ] * 2 << endl;
		else{
			try_( 1 );
			cout << min_t << endl;
		}
	}
	return 0;
}

