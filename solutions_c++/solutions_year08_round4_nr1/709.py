
#include <stdio.h>

const int oo = 100000;

int nprob, prob;
int M, V;
int G[10010], C[10010];
int f[10010][2];


inline int imin(int a, int b) {
	return a < b ? a : b;
}

int dp(int v, int e) {
	if (f[v][e] >= 0)
		return f[v][e];
		
	if (C[v] == 2) {
		f[v][e] = (G[v] == e ? 0 : oo);
	} else {
		int d1 = oo, d2 = oo;
		
		if (G[v] == 1 || C[v] == 1) {		// and
			if (e == 0) {
				int v1 = dp(v*2, 0) + dp(v*2+1, 0);
				int v2 = dp(v*2, 0) + dp(v*2+1, 1);
				int v3 = dp(v*2, 1) + dp(v*2+1, 0);
				d1 = imin(v1, imin(v2, v3));
			} else {
				d1 = dp(v*2, 1) + dp(v*2+1, 1);
			}
			
			if (G[v] != 1) d1++;
		}
		
		if (G[v] != 1 || C[v] == 1) {		// or
			if (e == 0) {
				d2 = dp(v*2, 0) + dp(v*2+1, 0);
			} else {
				int v1 = dp(v*2, 1) + dp(v*2+1, 1);
				int v2 = dp(v*2, 1) + dp(v*2+1, 0);
				int v3 = dp(v*2, 0) + dp(v*2+1, 1);
				d2 = imin(v1, imin(v2, v3));
			}
			
			if (G[v] == 1) d2++;
		}
		
		f[v][e] = imin(d1, d2);
	}
	
	return f[v][e];
}

int main() {
//	freopen("a.in", "r", stdin);
//	freopen("a.out", "w", stdout);
	
	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d%d", &M, &V);
		for (int i = 1; i <= (M-1)/2; i++) {
			scanf("%d%d", &G[i], &C[i]);
			if (C[i] != 1) C[i] = 0;
		}
		for (int i = (M-1)/2+1; i <= M; i++) {
			scanf("%d", &G[i]); C[i] = 2;
		}
		
		for (int i = 1; i <= M; i++)
			f[i][0] = f[i][1] = -1;
		
		int ans = dp(1, V);
		if (ans >= oo) {
			printf("Case #%d: IMPOSSIBLE\n", prob);
		} else {
			printf("Case #%d: %d\n", prob, dp(1, V));
		}
	}
	
	return 0;
}
