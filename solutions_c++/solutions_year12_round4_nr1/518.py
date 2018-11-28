// C.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAXN 10010
#define MAXL 1e9+1

int n;
int d[ MAXN ], l[ MAXN ];
int f[ MAXN ];

void init(){
	cin >> n;
	int i;
	for ( i = 0; i < n; i ++ ){
		scanf( "%d %d", &d[i], &l[i] );
	}
	cin >> d[n];
	l[n] = MAXL;
}

void bfs( int k ){
	if ( f[n] > 0 )
		return;
	int i ,c;
	for ( i = 0; i <= n; i ++ ){
		if ( i > k && d[k]+f[k] >= d[i] || i < k && d[k]-f[k] <= d[i] ){
			c = min( l[i], abs(d[k]-d[i]) );
			if ( f[i] < c )
				if ( i < n ){
					f[i] = c;
					bfs( i );
				}
				else{
					f[i] = 1;
					return;
				}
		}
	}
}

void cal(){
	memset( f, 0, sizeof( f ) );
	f[0] = d[0];
	bfs(0);
	if ( f[n] > 0 )
		cout << "YES";
	else
		cout << "NO";
	cout << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen( "A-large.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int t, i;
	scanf( "%d\n", &t );
	for ( i = 1; i <= t; i ++ ){
		init();
		cout << "Case #" << i << ": ";
		cal();
	}
	return 0;
}

