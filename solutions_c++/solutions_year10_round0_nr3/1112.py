#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1000
int r, k, n, g[N];

int main( ){
	int t, ca, i, j, ans;
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "C-small-attempt0.out", "w", stdout );
	scanf( "%d", &t );
	for ( ca = 1; ca <= t; ca++ ){
		scanf( "%d%d%d", &r, &k, &n );
		for ( i = 0; i < n; i++ ) scanf( "%d", g+i );
		int head, tail, s;
		ans = 0;
		head = 0;
		while ( r-- ){
			s = g[head];
			for ( tail = (head+1)%n; tail != head; tail = (tail+1)%n ){
				if ( s+g[tail] > k ) break;
				s += g[tail];
			}
			head = tail;
			ans += s;
		}
		printf( "Case #%d: %d\n", ca, ans );
	}
}
