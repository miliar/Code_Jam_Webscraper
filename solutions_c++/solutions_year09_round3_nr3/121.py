#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 105
#define inf 1000000000

priority_queue<int, vector<int>, greater<int> > q;

int i, j, k, n, m, T, t, x, y, z, res, mm;
int mn, nm;

int a[N], b[N];

int broot() {
	int c[10];
	int d[10005];
	memset(c, 0, sizeof(c));
	memset(d, 0, sizeof(d));
	int i, j, k, res, x, y, z;
	res = 1000000000;
	m = mm;
	for (i = 0 ;i < m; i ++) {
		c[i] = i;
	}
	do {
		for (i = 1; i <= n; i ++) {
			d[i] = 1;
		}
		y = 0;
		for (i = 0; i < m; i ++) {
			x = b[c[i]];
			z = 0;
			for (j = x; d[j] == 1; j ++) {
				y ++;
			}
			for (j = x; d[j] == 1; j --) {
				y ++;
			}
			y -= 2;
			d[x] = 0;
		}
		if (y < res) {
			res = y;
		}
	} while (next_permutation(c, c + m));
	return res;
}

int dp[N][N];

int dfs(int x, int y) {
	if (x == y) {
		return 0;
	}
/*	if (y == x + 1) {
		return dp[x][y] =  b[x] + b[y];
	}
*/
	if (dp[x][y] != -1) {
		return dp[x][y];
	}
	int i, j, k, mn, t, s;
	mn = inf;
	s = 0;
	for (i = x; i <= y; i ++) {
		s += a[i];
	}
	s += y - x;
	for (i = x; i < y; i ++) {
		t = dfs(x, i) + dfs(i + 1, y);
		if (t < mn) {
			mn = t;
		}
	}
	return dp[x][y] = mn + s - 1;
}
		

int main() {
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		memset(dp, -1, sizeof(dp));
		cin >> n >> m;

		mm = m;
		x = 0;
		for (i = 0; i < m; i ++) {
			cin >> y;
			a[i] = y - x - 1;
			b[i] = y;
			x = y;
		}
		a[m] = n - x;
		m ++;
		res = dfs(0, m - 1);


/*		while (m > 1) {
			mn = inf;
			for (i = 0; i < m - 1; i ++) {
				if (a[i] + a[i+1] < mn) {
					mn = a[i] + a[i+1];
					nm = i;
				}
			}
			res += mn;
			i = nm;
			a[i] = a[i] + a[i+1] + 1;
			for (j = i + 1; j < m - 1; j ++) {
				a[j] = a[j+1];
			}
			m --;
			a[m] = 0;
		}
*/
/*		x = broot();
		if (x != res) {
			cout << t << endl;
		}
*/
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}


