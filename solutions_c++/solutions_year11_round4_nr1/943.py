#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define M 1010
#define eps 1e-8

struct Data {
	int b, e, w;
	friend bool operator < ( const Data& a, const Data& b ) {
		return a.w < b.w;
	}
} data[ M ];

int main ( void ) {
	freopen ( "A-large.in", "r", stdin );
	freopen ( "A-large.out", "w", stdout );
	double L, S, R, T;
	int N, t;
	scanf ( "%d", &t );
	for ( int cas = 1 ; cas <= t ; ++cas ) {
		scanf ( "%lf%lf%lf%lf%d", &L, &S, &R, &T, &N );
		for ( int i = 0 ; i < N ; ++i ) {
			scanf ( "%d%d%d", &data[ i ].b, &data[ i ].e, &data[ i ].w );
			L -= data[ i ].e - data[ i ].b;
		}
		if ( L ) {
			data[ N ].w = 0;
			data[ N ].b = 0;
			data[ N++ ].e = L;
		}
		sort ( data, data + N );
		double ans = 0;
		for ( int i = 0 ; i < N ; ++i ) {
			double tmp = ( data[ i ].e - data[ i ].b ) / ( R + data[ i ].w );
			if ( tmp <= T ) {
				T -= tmp;
				ans += tmp;
				continue;
			}
			if ( T > eps ) {
				double x = ( data[ i ].e - data[ i ].b ) - ( R + data[ i ].w ) * T;
				ans += T;
				T = 0;
				ans += x / ( data[ i ].w + S );
				continue;
			}
			ans += ( data[ i ].e - data[ i ].b ) / ( S + data[ i ].w );
		}
		printf ( "Case #%d: %.8lf\n", cas, ans );
	}
	return 0;
}
