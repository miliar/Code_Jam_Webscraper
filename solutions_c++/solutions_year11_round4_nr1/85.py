#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

pair< double, double > a[1100];

main(){
	int t, tt = 0;
	double W, R, X, T;
	double B, E, w, res;
	int i, N;
	
	freopen( "AL.in", "r", stdin );
	freopen( "AL.out", "w", stdout );
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%lf %lf %lf %lf %d", &X, &W, &R, &T, &N );
		for ( i = 0; i < N; i ++ ){
			scanf ( "%lf %lf %lf", &B, &E, &w );
			a[i] = make_pair( w, E - B );
		}
		for ( i = 0; i < N; i ++ )
			X -= a[i].second;
		a[N] = make_pair( 0, X );
		sort ( a, a + N + 1 );
		res = 0;
		for ( i = 0; i <= N; i ++ ){
			if ( T * ( R + a[i].first ) <= a[i].second ){
				a[i].second -= T * ( R + a[i].first );
				res += T;
				T = 0;
				res += a[i].second / ( W + a[i].first );
			}
			else{
				res += a[i].second / ( R + a[i].first );
				T -= a[i].second / ( R + a[i].first );
			}
//			cout << res << endl;
		}
		
		printf( "Case #%d: %.10lf\n", ++ tt, res );
	}
	
	return 0;
}
