// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>

using namespace std;

#define MAXN 110

int num[ MAXN ];
int n, l, h;


bool ok( int p ){
	int i;
	for ( i = 1; i <= n; i ++ )
		if ( num[ i ] % p != 0 && p % num[ i ] != 0 )
			return false;
	return true;
}

int cal(){
	int i;
	for ( i = 1; i <= n; i ++ )
		cin >> num[ i ];

	for ( i = l; i <= h; i ++ )
		if ( ok( i ) )
			return i;
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i, p;
	cin >> t;
	for ( i = 1; i <= t ;i ++ ){
		cin >> n >> l >> h;
		cout << "Case #" << i << ": ";
		p = cal();
		if ( p == 0 )
			cout << "NO" << endl;
		else
			cout << p << endl;

	}

	return 0;
}

