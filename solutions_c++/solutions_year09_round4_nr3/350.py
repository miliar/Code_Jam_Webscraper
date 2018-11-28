#include <stdio.h>
#include <string.h>
#include <algorithm>
int g[101][101];
int a[101][101];
int n, m;
int check(int x, int y) {
	int i, j;
	if (a[x][0] > a[y][0]) {
		std::swap(x, y);
	}
	for (i=0;i<m;++i) {
		if (a[x][i] >= a[y][i]) return 0;
	}
	return 1;
}

int best, cur[101][101], cn[101] ;
void dfs(int dep, int cost) {
	if (cost >=best) return;
	if (dep>=n) {
		best = cost;
	}
	int i, j;
	for (i=0;i<cost;++i) {
		for (j=0;j<cn[i];++j) {
			if (!g[dep][cur[i][j]]) break;
		}
		if (j<cn[i]) continue;
		cur[i][cn[i]++] = dep;
		dfs(dep+1, cost);
		--cn[i];
	}
	cur[cost][cn[cost]++] = dep;
	dfs(dep+1, cost+1);
	--cn[cost];
}

int main() {
	int ca, cases = 0, i, j;
	scanf("%d", &ca);
	while (ca--) {
		scanf("%d%d", &n, &m);
		for (i=0;i<n;++i) {
			for (j=0;j<m;++j) {
				scanf("%d", &a[i][j]);
			}
		}
		for (i=0;i<n;++i) {
			g[i][i] = 0;
			for (j=i+1;j<n;++j) {
				g[i][j] = g[j][i] = check(i,j);
			}
		}
/*
		for (i=0;i<n;++i) {
			for (j=0;j<n;++j) {
				printf("%d ", g[i][j]);
			}
			printf("\n");
		}*/
		
		
		memset(cn, 0, sizeof(cn));
		best = 0x3fffff;
		dfs(0, 0);
		printf("Case #%d: %d\n", ++cases, best);
	}
	
	return 0;
}
