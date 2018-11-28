// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;


#define MAXN 1100
#define BEGIN_MIN 2000000

int c[ MAXN ];
bool f[ MAXN ];
int n, sum = 0;

void init(){
	int i, min = BEGIN_MIN, t = 0;
	long int sum = 0;
	cin >> n;
	for ( i = 1; i <= n; i ++ ){
		cin >> c[ i ];
		if ( c[ i ] < min )
			min = c[ i ];
		sum += c[ i ];
		t ^= c[ i ];
	}
	if ( t == 0 )
		cout << sum-min << endl;
	else
		cout << "NO" << endl;

	memset( f, 0, sizeof( f ) );
}


int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "C-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		cout << "Case #" << i << ": ";
		init();
	}
	return 0;
}

