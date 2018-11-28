#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

int n,m,d;
int a[20][20];

void init() {
	scanf( "%d%d%d\n", &n, &m, &d );
	for ( int i=1; i<=n; i++ ) {
		for ( int j=1; j<=m; j++ ) {
			char c;
			scanf( "%c", &c );
			a[i][j] = c-'0';
		}
		scanf( "\n" );
	}

}

void work() {
	int ans = 0;
	for ( int size=3; size<=min(n,m); size++ )
	for ( int i=1; i<=n; i++ )
	for ( int j=1; j<=m; j++ ) {
	
		if ( i+size-1>n || j+size-1>m ) continue;
		//if ( size%2!=1 ) continue;
		
		double tot = 0;
		double cx = i+(double)((size-1)*1.0)/2,
			   cy = j+(double)((size-1)*1.0)/2;
			   
		for ( int ii=i; ii<=i+size-1; ii++ )
		for ( int jj=j; jj<=j+size-1; jj++ ) {
			if ( ii==i && jj==j ) continue;
			if ( ii==i && jj==j+size-1 ) continue;
			if ( ii==i+size-1 && jj==j ) continue;
			if ( ii==i+size-1 && jj==j+size-1 ) continue;
			tot += (double)(sqrt((ii*1.0-cx)*(ii*1.0-cx)+(ii*1.0-cy)*(ii*1.0-cy)))*a[i][j];
		}
		
		if ( fabs(tot)<10e-6 && size>ans ) ans = size;
	}
	
	if ( ans!=0 ) printf( "%d\n", ans );
	else printf( "IMPOSSIBLE\n" );
}

int main() {
	freopen( "b.in", "r", stdin );
	freopen( "b.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	for ( int i=1; i<=T; i++ ) {
		printf( "Case #%d: ", i );
		init();
		work();
	}
	
	return 0;
}
