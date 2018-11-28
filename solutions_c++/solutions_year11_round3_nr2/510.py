#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define OUT(t) cerr<<#t" = "<<t<<" ";
#define OLN()  cerr<<endl;

int L, T, N, C;
int a[2000000];
int s[2000000];

int t[2000000];

bool cmp( int a, int b ) {
	return a>b;
}


int main( ) {
	freopen( "D:\\GoogleCodeJam\\B\\B-small-attempt0.in", "r", stdin );
	freopen( "D:\\GoogleCodeJam\\B\\B-small-attempt0.out", "w", stdout );

	int re, ri = 1;
	int i, j;

	scanf( "%d", &re );
	while( re-- ) {
		scanf( "%d%d%d%d", &L, &T, &N, &C );
		for( i=0 ; i<C ; i++ ) {
			scanf( "%d", &a[i] );
		}
		int total = 0;

		s[0] = 0;
		int cnt = 0;
		for( i=0 ; i<N ; i++ ) {
			a[i] = a[i%C];
			s[i] = (i==0 ? 0 : s[i-1] + a[i-1] * 2);

			if( s[i] + a[i]*2 > T ) {
				if( s[i] >= T ) {
					t[cnt++] = a[i];
				} else {
					t[cnt++] = a[i]*2 - (T-s[i] + a[i] - (T-s[i])/2);
					//OUT( a[i] ); OUT( s[i] ); OLN();
					//OUT( t[cnt-1] ); OLN();
				}
			}
			total += a[i] * 2;
		}

		// OUT( cnt ); OLN();

		sort( t, t+cnt, cmp );
		if( cnt > L ) {
			cnt = L;
		}

		for( i=0 ; i<cnt ; i++ ) {
			total -= t[i];
		}


		printf( "Case #%d: ", ri++ );
		printf( "%d\n", total );

	}

	return 0;
}
