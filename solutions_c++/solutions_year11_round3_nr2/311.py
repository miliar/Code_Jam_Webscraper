#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

double T;
int N, L;
double S[1000000];
double sum[1000001];
double sub[1000000];

double FindSub( int P ) {
	if( sum[P]*2 >= T ) return S[P];
	else if( sum[P+1]*2 <= T ) return 0.0;
	else return ( sum[P+1]*2 - T ) / 2.0;
}

int main() {
	freopen( "B_Large.in", "r", stdin );
	freopen( "B_Large.out", "w", stdout );

	int TC;
	scanf( "%d", &TC );
	
	for( int TCC=1; TCC<=TC; TCC++ ) {
		int C;
		scanf( "%d %lf %d %d", &L, &T, &N, &C );
		for( int i=0; i<C; i++ ) scanf( "%lf", &S[i] );
		for( int i=0; i<N; i++ ) S[i] = S[i%C];
		sum[0] = 0;
		for( int i=1; i<=N; i++ ) sum[i] = sum[i-1] + S[i-1];

		double ret = sum[N] * 2;
		for( int i=0; i<N; i++ ) sub[i] = FindSub( i );

		sort( sub, sub+N );
		for( int i=N-1; i>=N-L; i-- ) ret -= sub[i];

		printf( "Case #%d: %lld\n", TCC, (long long)ret );
	}
}