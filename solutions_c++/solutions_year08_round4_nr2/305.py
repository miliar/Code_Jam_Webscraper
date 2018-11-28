#include <cstdio>
#include <cstdlib>

typedef struct point point;
struct point {
	int x, y;
} u, pts[52*52];

int Cprod(point a, point b, point c) {
	return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y);
}

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, j, k, f, T, test, Q, N, M, A;
	
	scanf("%d", &T);
	
	for (test=1; test<=T; test++) {
		Q = 0;
		f = 0;
		
		scanf("%d %d %d", &N, &M, &A);
		
		for (i=0; i<=N; i++) {
			for (j=0; j<=M; j++) {
				u.x = i;
				u.y = j;
				
				pts[++Q] = u;
			}
		}
		
		for (j=2; j<=Q; j++) {
			for (k=j+1; k<=Q; k++) {
				if ( abs(Cprod(pts[1], pts[j], pts[k])) == A ) { f = 1; break; }
			}
			
			if ( f ) break;
		}
		
		printf("Case #%d: ", test);
		
		if ( !f ) {
			printf("IMPOSSIBLE\n");
		}
		else {
			printf("0 0 %d %d %d %d\n", pts[j].x, pts[j].y, pts[k].x, pts[k].y);
		}
	}
	
	return 0;
}
