#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char g[60][60];

int n, m;

bool solve() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (g[i][j] == '#') {
				if (i + 1 < n && j + 1 < m && g[i + 1][j] == '#' && g[i + 1][j
						+ 1] == '#' && g[i][j + 1] == '#') {
					g[i][j] = '/';
					g[i][j + 1] = '\\';
					g[i + 1][j] = '\\';
					g[i + 1][j + 1] = '/';
				} else {
					return false;
				}
			}
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (g[i][j] != '.' && g[i][j] != '/' && g[i][j] != '\\') {
				return false;
			}
		}
	}
	return true;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("alarge.out", "w", stdout);
	int nca;
	scanf("%d", &nca);
	for (int ii = 1; ii <= nca; ii++) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++) {
			scanf("%s", g[i]);
		}
		printf("Case #%d:\n", ii);
		if (solve()) {
			for (int i = 0; i < n; i++) {
				puts(g[i]);
			}
		} else {
			puts("Impossible");
		}
	}
	return 0;
}
