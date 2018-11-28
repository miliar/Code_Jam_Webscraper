#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

const int MAXC = 1011, MAXN = 1000111;
int l,n,c;
long long t;
int a[MAXC];
int d[MAXN];

void qsort( int l, int r ) {
	if ( l>=r ) return;

	int i = l,
		j = r,
		m = d[(l+r)/2];

	while ( i<j ) {
		while ( d[i]>m ) i++;
		while ( d[j]<m ) j--;
		if ( i<=j ) {
			swap( d[i], d[j] );
			i++;
			j--;
		}
	}
	
	qsort( i, r );
	qsort( l, j );
} 

void work() {
	// 预处理
	int cnt = -1;
	long long ans = 0;
	for ( int i=0; i<n; i++ ) {
		if ( ans+a[i%c]*2>t ) {
			cnt = i;
			break;
		}
		ans += a[i%c]*2; 
	}
	
	if ( cnt==-1 ) {
		cout << ans << endl;
		return;
	}
	
	int tot;
	
	// 对第cnt使用加速器
	long long ans1 = t+(a[cnt%c]-(t-ans)/2);
	if ( l>0 ) {
		tot = -1;
		for ( int i=cnt+1; i<n; i++ ) d[++tot] = a[i%c];
		qsort( 0, tot );
		for ( int i=0; i<l-1; i++ ) 
		if ( i<=tot ) ans1 += d[i];
		for ( int i=l-1; i<=tot; i++ ) ans1 += d[i]*2;
	}

	// 对第cnt不使用加速器
	long long ans2 = ans+a[cnt%c]*2;
	tot = -1;
	for ( int i=cnt+1; i<n; i++ ) d[++tot] = a[i%c];
	qsort( 0, tot );
	for ( int i=0; i<l; i++ ) 
	if ( i<=tot ) ans2 += d[i];
	for ( int i=l; i<=tot; i++ ) ans2 += d[i]*2;

	if ( ans1<ans2 && l>0 ) ans = ans1;
	else ans = ans2;

	cout << ans << endl;
}

int main() {
	freopen( "b.in", "r", stdin );
	freopen( "bb.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	for ( int i=1; i<=T; i++ ) {
		printf( "Case #%d: ", i );
		scanf( "%d%lld%d%d", &l, &t, &n, &c );
		for ( int j=0; j<c; j++ ) scanf( "%d", &a[j] );
		work();
	}
	
	return 0;
}
