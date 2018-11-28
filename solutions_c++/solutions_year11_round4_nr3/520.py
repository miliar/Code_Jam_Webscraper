#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define OUT(t) cerr<<#t" = "<<t<<" ";
#define OLN()  cerr<<endl;

typedef long long INT;

bool prime( int n ) {
	if( n==1 ) return false;
	if( n==2 ) return true;

	int t = (int)sqrt( (double)n );
	for( int i=2 ; i<=t ; i++ ) {
		if( n%i==0 ) return false;
	}
	return true;
}

INT gcd( INT a, INT b ) {
	return b==0 ? a : gcd( b, a%b );
}

INT lcm( INT a, INT b ) {
	return a/gcd(a,b)*b;
}

int prm[2000];
bool isPrm[2000];
int pCnt;

int main( ) {
	freopen( "D:\\GoogleCodeJam\\C\\C-small-attempt1.in", "r", stdin );
	freopen( "D:\\GoogleCodeJam\\C\\C-small-attempt1.out", "w", stdout );


	int re, ri = 1;
	int n, i;

	pCnt = 0;
	for( i=1 ; i<=1000 ; i++ ) {
		if( isPrm[i] = prime(i) ) {
			prm[pCnt++] = i;
		}
	}

	scanf( "%d", &re );
	while( re-- ) {
		scanf( "%d", &n );

		int minCnt = 0;
		for( i=1 ; i<=n ; i++ ) {
			if( isPrm[i] ) minCnt ++;
		}

		int cnt[2000];
		memset( cnt, 0, sizeof(cnt) );


		int maxCnt = 1;
		for( i=2 ; i<=n ; i++ ) {
			bool flag = false;
			int t = i;
			for( int j=0 ; j<pCnt ; j++ ) {
				int c = 0;
				while( t%prm[j] == 0 ) {
					t /= prm[j]; c++;
				}
				if( c > cnt[j] ) {
					flag = true;
					cnt[j] = c;
				}
			}
			if( flag ) maxCnt ++;
		}


		//int maxCnt = 1;
		/*INT lastLcm = 1;
		for( i=2 ; i<=n ; i++ ) {
			INT t = 1;
			for( int j=1 ; j<=i ; j++ ) {
				t = lcm( t, j );
			}
			if( t!=lastLcm ) {
				maxCnt ++;
				lastLcm = t;
			}
			OUT( lastLcm ); OLN();
		}
		*/


		//OUT( maxCnt );
		//OUT( minCnt );
		//OLN();
		if( n==1 ) minCnt = 1;
		printf( "Case #%d: %d\n", ri++, maxCnt-minCnt );
	}

	return 0;
}
