#include <stdio.h>

int nprob, prob;
int M, N;
char mat[10][16];
int f[11][1024];

int dp(int, int);

int getb(int s, int i) {
	if (i < 0 || i >= M) return 0;
	return (s >> i) & 1;
}

void dfs(int i, int s, int tot, int j, int b, int *f) {
	if (i == M) {
		int d = dp(j+1, s) + tot;
		if (d > *f) *f = d;
		return;
	}
	
	if (mat[i][j] == '.' && !getb(b, i) && !getb(b, i-1) && !getb(b, i+1)) {
		dfs(i+1, s | (1 << i), tot + 1, j, b, f);
	}
	
	dfs(i+1, s, tot, j, b, f);
}

int dp(int j, int s) {
	if (j == N) {
		return 0;
	}
	
	if (f[j][s] >= 0)
		return f[j][s];
	
	f[j][s] = 0;
	dfs(0, 0, 0, j, s, &f[j][s]);
	
	return f[j][s];
}

int main() {
//	freopen("c.in", "r", stdin);
//	freopen("c.out", "w", stdout);
	
	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d%d", &M, &N);
		for (int i = 0; i < M; i++) {
			scanf("%s", mat[i]);
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = (1<<M)-1; j >= 0; j--)
				f[i][j] = -1;
		}
		
		printf("Case #%d: %d\n", prob, dp(0, 0));
	}
	
	return 0;
}

