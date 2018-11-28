// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>

using namespace std;

#define MAXN 200
#define MAXP 200000

int n, c, k, max_=0;
long long prim[ MAXN ], pp[ MAXN ];
bool f[ MAXP ];

void init(){
	cin >> n;
	max_ = 0;
}

int gcd( long long  a, long long   b ){
	return ( b == 0 ) ? a: gcd( b, a%b );
}

int lcm( long long a, long long  b ){
	return( a*b/gcd(a,b) );
}

void prims(){
	int i, j;

	memset( f, true, sizeof( f ) );
	k = 0;

	for ( i = 2; i <= MAXP; i ++ )
		if ( f[ i ] ){
			prim[ ++k ] = i;
			j = i+i;
			if ( j > MAXP ) break;
			while ( j <= MAXP ){
				f[ j ] = false;
				j += i;
			}
		}
}

void solv( int ll ){
	long long  i;
	long long j;
	for ( i = 1; i <= k; i ++ ){
		j = prim[ i ];
		if ( ll % j == 0 ){
			c = 0;
			while ( ll % j == 0 ){
				ll /= j;
				c++;
			}
			if ( c > pp[ i ] )
				pp[ i ] = c;
		}
		if ( i > max_ )
			max_ = i;
		if ( ll == 1 )
			break;
	}
	//cout << c-t+1 << endl;
}


void cal(){
	/*
	ll = 1;
	long long  i;
	for ( i = 1; i <= n; i ++ )
		ll = lcm( ll, i );
	cout << n << " " << ll << " ";
	*/

	memset( pp, 0, sizeof( pp ) );
	int i, t=0, c=0 ;
	for ( i = 1; i <= n; i ++ )
		solv( i );

	for ( i = 1; i <= max_; i ++ )
		if ( pp[ i ] > 0 ){
			t ++;
			c += pp[ i ];
		}
	cout << c-t+1 << endl;

}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "C-small-attempt1.in", "r", stdin );
	freopen( "out.txt","w",stdout);
	int t, i;
	prims();
	cin >> t;
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		if ( n == 1 )
			cout << 0 << endl;
		else
			cal();
		//print_();
	}
	return 0;
}

