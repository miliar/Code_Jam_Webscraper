// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>

using namespace std;

long long n;
int pd, pg, d, g;

int gcd( int a, int b ){
	return ( ( b == 0 ) ? a : gcd( b, a%b ) );
}

bool check(){
	//cin >> n >> pd >> pg;
	cin >> n;
	scanf( "%d%d" , &pd, &pg );
	if ( pd < 100 && pg == 100 ) return false;
	if ( pd > 0 && pg  == 0 ) return false;

	d = 100 / gcd( 100, pd );
	if ( d > n )
		return false;
	//cout << d << " ";
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		cout << "Case #" << i << ": ";
		if ( check() )
			cout << "Possible" << endl;
		else
			cout << "Broken" << endl;
	}
	return 0;
}

