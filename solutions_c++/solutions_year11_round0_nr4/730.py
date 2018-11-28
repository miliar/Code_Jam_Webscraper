// D.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>

using namespace std;

#define MAXN 1100

int p[ MAXN ];

void cal(){
	int n, i, sum;
	cin >> n;
	sum = n;
	for ( i = 1; i <= n; i ++ ){
		cin >> p[ i ];
		if ( p[ i ] == i ) 
			sum --;
	}
	cout << sum << ".000000" << endl;
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "D-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}

