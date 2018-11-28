#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

const int maxn=100;
int t,n;
int tot[2],w[2],cur[2],a[2][maxn],b[2][maxn];

int main() {
	freopen( "a.in", "r", stdin );
	freopen( "a.out", "w", stdout );

	scanf( "%d", &t );
	for ( int i=1; i<=t; i++ ) {
		tot[0] = 0;
		tot[1] = 0;
		w[0] = 1;
		w[1] = 1;
		cur[0] = 1;
		cur[1] = 1;
	
		// read
		scanf( "%d ", &n );
		for ( int j=1; j<=n; j++ ) {
			char c;
			int d;
			scanf( "%c %d ", &c, &d );
			
			int p=0;
			if ( c=='B' ) p=1;
			
			tot[p]++;
			a[p][tot[p]] = d;
			b[p][tot[p]] = j;
		}
		
		// work
		int now = 1;
		int sum = 0;
		while ( now<=n ) {
			sum++;
			
			int tnow = now;
			for ( int j=0; j<=1; j++ ) {
				if ( cur[j]>tot[j] ) continue;
				if ( w[j]<a[j][cur[j]] ) w[j]++; else
				if ( w[j]>a[j][cur[j]] ) w[j]--; else {
					if ( now==b[j][cur[j]] ) {
						tnow++;
						cur[j]++;
					}
				}
			}
			now = tnow;

		}
		
		printf( "Case #%d: %d\n", i, sum );
	}

	return 0;
}
