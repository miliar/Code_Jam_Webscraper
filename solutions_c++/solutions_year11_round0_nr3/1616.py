#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

#define OUT(tp,t) printf( #t "=" tp " ", t  );

using namespace std;

int a[2000];

int main( ) {
	int re;
	int i, n;

	//freopen( "D:\\cc\\in.txt", "r", stdin );
	freopen( "D:\\cc\\C-small-attempt0.in", "r", stdin );
	freopen( "D:\\cc\\C-small-attempt0.out", "w", stdout );

	scanf( "%d", &re );
	int ri = 1;
	while( re-- ) {
		scanf( "%d", &n );
		int t = 0;
		int m = (1<<30);
		int s = 0;
		for( i=0 ; i<n ; i++ ) {
			scanf( "%d", &a[i] );
			t ^= a[i];
			if( a[i] < m ) {
				m = a[i];
			}
			s += a[i];
		}
		if( t ) {
			printf( "Case #%d: NO\n", ri++ );
		} else {
			printf( "Case #%d: %d\n", ri++, s-m );
		}

	}

	return 0;
}
