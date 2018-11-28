#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define OUT(t) cerr<<#t" = "<<t<<" ";
#define OLN()  cerr<<endl;

int N, L, H;
int a[1000];

bool can( int x ) {
	int i;

	for( i=0 ; i<N ; i++ ) {
		if( !(a[i]%x==0 || x%a[i]==0) ) return false;
	}

	return true;
}

int main( ) {
	freopen( "D:\\GoogleCodeJam\\C\\C-small-attempt0.in", "r", stdin );
	freopen( "D:\\GoogleCodeJam\\C\\C-small-attempt0.out", "w", stdout );

	int re, ri = 1;
	int i, j;

	scanf( "%d", &re );
	while( re-- ) {
		scanf( "%d%d%d", &N, &L, &H );
		for( i=0 ; i<N ; i++ ) {
			scanf( "%d", &a[i] );
		}

		for( j=L ; j<=H ; j++ ) {
			if( can( j ) ) break;
		}

		printf( "Case #%d: ", ri++ );
		if( j<=H ) {
			printf( "%d\n", j );
		} else {
			puts( "NO" );
		}

	}

	return 0;
}
