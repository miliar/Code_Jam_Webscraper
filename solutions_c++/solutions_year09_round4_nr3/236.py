#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;

#define N 205

vector<vector<int> > v;

int k;
int a[N][N];
int b[N][N], bg, en, n;
int u[N];

int dfs(int cur) {
	int i, j, t;
	if (cur == en) {
		return 1;
	}
	u[cur] = 1;
	for (i= 0; i < n; i ++) {
		if (b[cur][i] == 1 && u[i] == 0) {
			t = dfs(i);
			if (t == 1) {
				b[cur][i] = 0;
				b[i][cur] = 1;
				return 1;
			}
		}
	}
	return 0;
}


int i, j, m, x, y, z, t, T, res, l, nn;


int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		cin >> n >> k;
		v.clear();
		v.resize(n);
		nn = n;
		for (i = 0; i < n; i ++) {
			v[i].resize(k);
		}
		for ( i= 0; i < n; i ++) {
			for (j = 0; j < k; j ++) {
				cin >> v[i][j];
			}
		}
		memset(a,0, sizeof(a));
		memset(b,0, sizeof(b));
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j ++) {
				for (l = 0; l < k; l ++) {
					if (v[j][l] >= v[i][l]) {
						break;
					}
				}
				if (l == k) {
					a[i][j] = 1;
				}
			}
		}

		bg = n + n;
		en = bg + 1;
		for (i = 0; i < n; i ++) {
			b[bg][i] = 1;
			for (j = 0; j < n; j ++) {
				if (a[i][j] == 1) {
					b[i][j+n] = 1;
				}
			}
			b[i+n][en] = 1;
		}

		n = en + 1;
		res = 0;
		while (1) {
			memset(u, 0 ,sizeof(u));
			x = dfs(bg);
			if (x == 0) {
				break;
			}
			res += x;
		}
		res = nn - res;
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}



