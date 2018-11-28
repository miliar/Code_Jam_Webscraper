#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_N 128

int g[MAX_N][MAX_N];
int sy[MAX_N];
int cx[MAX_N];
int cy[MAX_N];
int nx, ny, m;


void input() {
	int n, m;
	int v[MAX_N][MAX_N];
	scanf("%d%d", &n, &m);
	for (int i = 1; i<=n; ++i)
		for (int j=1; j<=m; ++j)
			scanf("%d", &v[i][j]);
	memset(g, false, sizeof(g));
	for (int i=1; i<=n; ++i)
		for (int j=1; j <=n; ++j) {
			int k;
			for (k=1; k<=m; k++)
				if (v[i][k] >= v[j][k]){
					//g[i][j] = false;
				//	g[j][i] = false;
					break;	
				}	
			if (k == m+1)
				g[i][j] = true;		
		}
	nx = n;
	ny = n;
}

int path(int u) {
	for (int v=1; v<=ny; v++)
		if (g[u][v] && !sy[v]) {
			sy[v] = 1;
			if (!cy[v] || path(cy[v])) {
				cx[u] = v;
				cy[v] = u;
				return 1;	
			}	
		}	
	return 0;
}

int maxmatch() {
	int i;
	int ret = 0;
	memset(cx, 0, sizeof(cx));
	memset(cy, 0, sizeof(cy));
	for (i=1; i<=nx; ++i)
		if (!cx[i]) {
			memset(sy, 0, sizeof(sy));
			ret += path(i);	
		}	
	return ret;
}
int main(int argc, char* argv[]) {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int cases;
	scanf("%d", &cases);
	
	for (int cas=1; cas <= cases; ++cas) {
		input();	
		int res = nx-maxmatch();
		printf("Case #%d: %d\n", cas, res);
	}	
	return 0;
}
