#include <cstdio>
#include <algorithm>
#define INF 0x3f3f3f3f

using namespace std;

char S[1024], t[1024];
int perm[6];

int k;

int main(){
	int tp; scanf( "%d", &tp );

	for( int tt = 1; tt <= tp; ++tt ){
		scanf( "%d", &k );
		scanf( "%s", S );
		int sol = INF;

		for( int i = 0; i < k; ++i ) perm[i] = i;

		do{
			for( int i = 0; S[i]; ++i ){
				t[i] = S[(i/k)*k + perm[i%k]];
			}
			int tsol = 1;
			for( int i = 0; S[i+1]; ++i ){
				if( t[i] != t[i+1] ) ++tsol;
			}
			sol = min( sol, tsol );
		}while( next_permutation( perm, perm+k ) );
		printf( "Case #%d: %d\n", tt, sol );
	}

	return 0;
}
