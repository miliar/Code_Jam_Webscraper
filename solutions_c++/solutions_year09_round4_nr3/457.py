#include <algorithm>
#include <cstdio>
using namespace std;

const int MAXN = 128;
const int MAXK = 32;
int n, k, t;
int a[MAXN][MAXK];
bool c[MAXN][MAXN];
int nc[MAXN];
int set[MAXN];
int best;

void dfs(int dep, int b) {
	if (dep >= n) {
		best = min(best, b);
		return;
	}	
	if (b >= best) return;

	for (int i = 0; i < b+1; i++) {
		bool ok = true;
		set[dep] = i;
		for (int j = 0; j < dep; j++)
			if (c[dep][j] && i == set[j]) {
				ok = false;
				break;
			}
		if (ok)
			dfs(dep+1, max(b, i+1));
	}
}

int main() {
	scanf("%d", &t);
	for (int ti = 0; ti < t; ti++) {
		scanf("%d %d", &n, &k);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++)
				scanf("%d", &a[i][j]);
		memset(c, 0, sizeof(c));
		memset(nc, 0, sizeof(nc));

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				for (int m = 0; m < k-1; m++)
					if (i != j && a[i][m]<=a[j][m] && a[i][m+1] >= a[j][m+1]) {
						c[i][j] = c[j][i] = true;
						// printf("conflict %d %d\n", i, j);
					}
		best = n;
		dfs(0, 0);
		printf("Case #%d: %d\n", ti+1, best);
	}
}

