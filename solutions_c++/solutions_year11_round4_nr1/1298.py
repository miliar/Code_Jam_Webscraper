#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
using namespace std;

int N;
int X;
double S, R, T;
int B[1000001], E[1000001];
double W[10000001];		
double ret[1000001];

int main() {
	freopen( "A.in", "r", stdin );
	freopen( "A.out", "w", stdout );

	int TC;
	scanf( "%d", &TC );

	for( int TCC=1; TCC<=TC; TCC++ ) {
		scanf( "%d %lf %lf %lf %d", &X, &S, &R, &T, &N );
		for( int i=0; i<X; i++ ) ret[i] = 0.0;
		//memset( was_ret, false, sizeof was_ret );
		for( int i=0; i<N; i++ ) {
			scanf( "%d %d %lf", &B[i], &E[i], &W[i] );
			for( int j=B[i]; j<E[i]; j++ ) ret[j] = W[i];
		}

		sort( ret, ret+X );
		
		double result = 0.0;
		for( int i=0; i<X; i++ ) {
			//cerr << ret[i] << ' ';
			double can_time = 1.0 / ( ret[i] + R );
			if( T == 0.0 ) {
				result += 1.0 / ( ret[i] + S );
			}
			else if( can_time <= T ) {
				T -= can_time;
				result += 1.0 / ( ret[i] + R );
			}
			else {
				double dist = T * ( ret[i] + R );
				result += dist / ( ret[i] + R );
				result += ( 1.0 - dist ) / ( ret[i] + S );
				T = 0.0;
			}
		}
		//cerr << endl;

		printf( "Case #%d: %.9lf\n", TCC, result );

	}
}