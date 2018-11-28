#include <cstdio>

long long N, M, A;
int tt;

inline long long abs( long long x ){ return x < 0? -x: x; }

long long P( long long ax, long long ay, long long bx, long long by, long long cx, long long cy ){
	return abs(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by));
}

bool solve(){
	for( long long c = 0; c <= M && c <= 500; ++c ){
		long long nA = A+c;
		for( long long a = 1; a <= M; ++a ){
			if( nA % a == 0 && nA/a <= N ){
				printf( "Case #%d: 0 0 1 %lld %lld %lld\n", tt, a, nA/a, c );
				return true;
			}
		}
	}
	return false;
}

int main(){
	int tp; scanf( "%d", &tp );

	for( tt = 1; tt <= tp; ++tt ){
		scanf( "%lld%lld%lld", &N, &M, &A );
		if( !solve() ) printf( "Case #%d: IMPOSSIBLE\n", tt );
	}

	return 0;
}
