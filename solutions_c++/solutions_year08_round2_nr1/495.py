// Jacek Migdal 2008 Google code jam
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

long long possible( long long n ) {
	if( n<3 )
		return 0;
	else
		return n*(n-1)*(n-2)/6;
}

void doIt() {
	long long n, A, B, C, D, x0, y0, M;
	scanf( "%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M );

	static int cache[3][3];
	for( int i = 0 ; i<3 ; i++ )
		for( int j = 0 ; j<3 ; j++ )
			cache[i][j] = 0;

	long long x =x0, y = y0;
	cache[x%3][y%3]++;
	for( int i = 1 ; i<n ; i++ ) {
		x = (A*x+B)%M;
		y = (C*y+D)%M;
		cache[x%3][y%3]++;
	}

	//for( int i = 0 ; i<3 ; i++ )
	//	for( int j = 0 ; j<3 ; j++ )
	//		printf( "D: %d %d %d\n", i, j, cache[i][j]);

	long long result = 0;
	for( int i = 0 ; i<3 ; i++ ) {
		result += possible(cache[i][0]);
		result += possible(cache[i][1]);
		result += possible(cache[i][2]);
		result += cache[i][0]*cache[i][1]*cache[i][2];
		result += cache[0][i]*cache[1][i]*cache[2][i];

		result += cache[i][0]*cache[(i+1)%3][1]*cache[(i+2)%3][2];
		result += cache[i][0]*cache[(i+2)%3][1]*cache[(i+1)%3][2];
	}
	printf( "%lld\n", result );
}

int main() {
	int nTests;
	scanf( "%d", &nTests);
	for( int i = 0 ; i<nTests ; i++ ) {
		printf("Case  #%d: ", i+1);
		doIt();
	}
	return 0;
}
