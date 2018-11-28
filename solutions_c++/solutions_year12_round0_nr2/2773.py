#include <cstdio>

using namespace std;


int main () {
	int T, N, S, P, pts, mrg, res;
	
	scanf("%d", &T);
	for ( int tc = 0; tc < T; ++tc ) {
		res = 0;
	
		scanf("%d %d %d", &N, &S, &P);
		mrg = P + ( 2 * ( P - 1 ) );
		if ( mrg < 0 )
			mrg = 0;
			
		for ( int n = 0; n < N; ++n ) {
			scanf("%d", &pts);
			
			//printf("MRG:%d PTS:%d RES:%d", mrg, pts, res);
			
			if ( mrg <= pts ) {
				res += 1;
			}
			else if ( mrg - 1 <= pts && pts - P >= 1 && S > 0 ) {
				res += 1;
				S -= 1;
			}
			else if ( mrg - 2 <= pts && pts - P >= 2 && S > 0 ) {
				res += 1;
				S -= 1;
			}
			
			//printf("->%d\n", res);
			
		}
		
		printf("Case #%d: %d\n", tc+1, res);
	}
	
	return 0;
}
			
			
