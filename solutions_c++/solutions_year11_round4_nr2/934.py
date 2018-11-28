# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <set>
# include <map>
# include <algorithm>
# include <queue>
# include <stack>
# include <cassert>
# include <ctime>
# include <cstdlib>

# define EPS 1e-7

using namespace std;

int T;
int R, C, D;
char w[512][512];
int peso[512][512];

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main (void){
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d%d%d", &R, &C, &D);
		for(int i = 0 ; i < R; i++){
			scanf(" %s", w[i]);
		}
		
		for(int i = 0 ; i < R; i++){
			for(int j =  0; j < C; j++){
				peso[i][j] = D + (w[i][j] - '0');
			}
		}

		int M = min(R,C);
		int best = -1;
		for(int K = 3; K <= M; K++){
			for(int i = 0 ; i < R; i++){
				for(int j = 0 ; j < C; j++){
					if( i + K > R ) continue;
					if( j + K > C ) continue;

					int itemp = R - i;
					
					double cy = (double) itemp - ((double) K/2);
					
					double cx = (double) j + ((double) K/2);
					
					double sx = 0.0;
					double sy = 0.0;
					for(int i2 = i; i2 < i+K; i2++){
						for(int j2 = j; j2 < j+K; j2++){
							if( i2 == i and j2 == j ) continue;
							if( i2 == i and j2 == j+K-1) continue;
							if( j2 == j and i2 == i+K-1) continue;
							if( i2 == i+K-1 and j2 == j+K-1) continue;
							itemp = R - 1 - i2;
							sx += (j2 + 0.5 - cx) * peso[i2][j2];
							sy += (itemp + 0.5 - cy)* peso[i2][j2];
							// printf("%f %d\n", itemp + 0.5 - cy, peso[i2][j2]);
						}
					}
					
					/*if( sx == 0 && sy == 0 ){
						best = K;
					}*/
					
					if( cmp(sx,0) == 0 && cmp(sy,0) == 0 ){
						best = K;
					}
				}
			}
		}
		
		if( best == -1){
			printf("Case #%d: IMPOSSIBLE\n", tc);
		}
		else{
			printf("Case #%d: %d\n", tc, best);
		}
	}
	return 0;
}