#include <cstdio>
#include <cstring>

#define maxn (1 << 17)

typedef long long int64;

int x[maxn], y[maxn], n;

int64 cnt[4][maxn][3][3];

int main() {
	int t, tc, i, j, a, b, c, d, m;
	scanf("%d", &tc);
	for(t = 1; t <= tc; t++) {
		scanf("%d%d%d%d%d%d%d%d", &n, &a, &b, &c, &d, x+0, y+0, &m);
		for(i = 1; i < n; i++) {
			x[i] = (int64(a)*x[i-1] + b) % m;
			y[i] = (int64(c)*y[i-1] + d) % m;
		}
//		for(i = 0; i < n; i++) printf("(%d, %d) ", x[i], y[i]); puts("");
		for(i = 0; i < n; i++) {
			x[i] %= 3;
			y[i] %= 3;
		}
		memset(cnt, 0, sizeof(cnt));
		for(i = 0; i < n; i++) cnt[0][i][0][0] = 1;
		for(j = 0; j < 3; j++)
			for(i = 0; i < n; i++) 
				for(int u = 0; u < 3; u++)
					for(int v = 0; v < 3; v++) {
						cnt[j+1][i+1][u][v] += cnt[j+1][i][u][v];
						cnt[j+1][i+1][(u+x[i])%3][(v+y[i])%3] += cnt[j][i][u][v];
					}
		printf("Case #%d: %Ld\n", t, cnt[3][n][0][0]);
	}
	return 0;
}
