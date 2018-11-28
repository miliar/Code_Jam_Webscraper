#include <cstdio>
#define MAXN 1000

int n, m, r;
bool a[MAXN][MAXN];
int rez[MAXN][MAXN];

int main(){
	freopen("knight.in", "rt", stdin);
	freopen("knight.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		scanf("%d%d%d", &n, &m, &r);
		for (int i = 0; i < MAXN; i++) for (int j = 0; j < MAXN; j++) a[i][j] = rez[i][j] = 0;
		while (r--){
			int p, q;
			scanf("%d%d", &p, &q);
			a[p-1][q-1] = true;
		}
		rez[0][0] = 1;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (!a[i][j]){
					rez[i][j] %= 10007;
					rez[i+1][j+2] += rez[i][j];
					rez[i+2][j+1] += rez[i][j];
				}
		printf("Case #%d: %d\n", t, rez[n-1][m-1]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
