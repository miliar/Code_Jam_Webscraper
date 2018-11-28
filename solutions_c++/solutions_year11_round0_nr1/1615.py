#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

#define OUT(tp,t) printf( #t "=" tp " ", t  );

using namespace std;

int R[1000];
vector<int> P[2];
int N;

int step( int a, int b ) {
	if( a==b ) return 0;
	if( a<b ) return -1;
	return 1;
}

int getAns( ) {
	int cnt = 0;
	int x[2]={1,1}, xi[2] = {0,0};
	int i = 0;

	for( i=0 ; i<N ; i++ ) {
		while( x[R[i]] != P[R[i]][xi[R[i]]] ) {
			x[R[i]^0] += step( P[R[i]^0][xi[R[i]^0]], x[R[i]^0] );
			x[R[i]^1] += step( P[R[i]^1][xi[R[i]^1]], x[R[i]^1] );
			cnt ++;
		}
		x[R[i]^1] += step( P[R[i]^1][xi[R[i]^1]], x[R[i]^1] );
		cnt++;

		xi[R[i]] ++;
	}

	return cnt;
}

int main( ) {
	int re;
	int i, a;
	char s[10];

	freopen( "D:\\a\\in.txt", "r", stdin );
	freopen( "D:\\a\\A-small-attempt0.out", "w", stdout );

	scanf( "%d", &re );
	int ri = 1;
	while( re-- ) {
		scanf( "%d", &N );
		P[0].clear();
		P[1].clear();
		for( i=0 ; i<N ; i++ ) {
			scanf( "%s%d", s, &a );
			R[i] = s[0]=='O' ? 0 : 1;
			P[R[i]].push_back( a );
		}
		printf( "Case #%d: %d\n", ri++, getAns() );
	}

	return 0;
}
