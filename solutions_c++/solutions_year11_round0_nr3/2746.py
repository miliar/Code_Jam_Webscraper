#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

const int maxn = 1011;
int n, ans;
int a[maxn];
bool v;

void init() {
	v = false;
	ans = 0;
	
	scanf( "%d", &n );
	for ( int i=1; i<=n; i++ ) scanf( "%d", &a[i] );
}

void dfs( int now, int sa, int sb, int sc, int sd ) {
	//cout << now << " ==> " << sa << " " << sb << " " << sc << endl;
	if ( now>n ) {
		if ( sa==sb && sc>0 && sd>0 ) {
			v = true;
			if ( sc>ans ) ans = sc;
		}
		return;
	}
	
	dfs( now+1, sa, sb xor a[now], sc, sd+a[now] );
	dfs( now+1, sa xor a[now], sb, sc+a[now], sd );
}

void print( int t ) {
	printf( "Case #%d: ", t );
	if ( v ) cout << ans << endl;
	else cout << "NO" << endl;
}

int main() {
	freopen( "c.in", "r", stdin );
	freopen( "c.out", "w", stdout );
	
	int T;
	scanf( "%d", &T );
	
	for ( int i=1; i<=T; i++ ) {
		init();
		dfs( 1, 0, 0, 0, 0 );
		print( i );
	}
	
	return 0;
}
