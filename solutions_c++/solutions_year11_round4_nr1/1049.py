#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

const int maxn = 1011;
int x,s,r,t,n,tot;
int b[maxn], e[maxn], w[maxn], bb[maxn*10],ee[maxn*10],ww[maxn*10];

void init() {
	scanf( "%d%d%d%d%d", &x, &s, &r, &t, &n );
	for ( int i=1; i<=n; i++ ) scanf( "%d%d%d", &b[i], &e[i], &w[i] );
	for ( int i=1; i<=n-1; i++ )
	for ( int j=i+1; j<=n; j++ ) 
	if ( b[i]>b[j] ) {
		swap( b[i], b[j] );
		swap( e[i], e[j] );
		swap( w[i], w[j] );
	}
}

void work() {
	tot = 1;
	bb[tot] = 0;
	ee[tot] = b[1];
	ww[tot] = s;
	for ( int i=1; i<=n; i++ ) {
		tot++;
		bb[tot] = b[i];
		ee[tot] = e[i];
		ww[tot] = s+w[i];
		if ( i<n ) {
			tot++;
			bb[tot] = e[i];
			ee[tot] = b[i+1];
			ww[tot] = s;
		} else {
			tot++;
			bb[tot] = e[i];
			ee[tot] = x;
			ww[tot] = s;
		}
	}
	
	for ( int i=1; i<=tot-1; i++ )
	for ( int j=i+1; j<=tot; j++ )
	if ( ww[i]>ww[j] ) {
		swap( bb[i], bb[j] );
		swap( ee[i], ee[j] );
		swap( ww[i], ww[j] );
	}

	double tt = t,
		   ans = 0;
	for ( int i=1; i<=tot; i++ ) {
		if ( (double)((double)(ee[i]-bb[i])*1.0/(double)(ww[i]-s+r)*1.0)<=tt ) {
			tt -= (double)((double)(ee[i]-bb[i])*1.0/(double)(ww[i]-s+r)*1.0);
			ans += (double)((double)(ee[i]-bb[i])*1.0/(double)(ww[i]-s+r)*1.0);
		} else 
		if ( tt>0 ) {
			ans += tt;
			ans += (double)((double)(ee[i]-bb[i]-1.0*(ww[i]-s+r)*tt*1.0)*1.0/(double)(ww[i])*1.0);
			tt = 0;
		} else {
			ans += (double)((double)(ee[i]-bb[i])*1.0/(double)(ww[i])*1.0);
		}
	}
	
	printf( "%.9f\n", ans );
}

int main() {
	freopen( "a.in", "r", stdin );
	freopen( "a.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	for ( int i=1; i<=T; i++ ) {
		printf( "Case #%d: ", i );
		init();
		if ( s>r ) cout << 123 << "---" << endl;
		work();
	}
	
	return 0;
}
