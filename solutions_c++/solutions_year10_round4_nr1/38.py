#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 128;

int n;

char a[maxn][maxn];
int ans = 1000000000;

int solve() {
	int k;
	ans = 1000000000;
	scanf("%d", &k);
	memset(a, 0, sizeof(a));
	n = 2*k-1;
	for (int i = 0; i < n; ++i) {
		int t = min(i+1, n-i);
		int x = k-t;
		for (int j = 0; j < t; ++j) {
			int k;
			scanf("%d", &k);
			a[i][j*2+x] = k+48;
		}
	}
	int mi = k-1;
	int mj = k-1;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			int m = 0;
			
			bool flag = true;
			for (int x = 0; x < n; ++x)
				if (flag)
				for (int y = 0; y < n; ++y)
					if (a[x][y]) {
						int tx = 2 * i - x;
						if (tx >= 0 && tx < n && a[tx][y] && a[tx][y]!=a[x][y]) {
							flag = false;
							break;
						}
						int ty = 2 * j - y;
						if (ty >= 0 && ty < n && a[x][ty] && a[x][ty]!=a[x][y]) {
							flag=false;
							break;
						}
						int tt = abs(i-x) + abs(j-y);
						if (tt > m) {
							m = tt;
						}
					}

			m = (m+1)*(m+1)-k*k;
			if (flag && m < ans)
				ans = m;
		}
	}
	return ans;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T -- ) {
		int ans = solve();
		printf("Case #%d: %d\n", ++tc, ans);
		fprintf(stderr, "%d\n", tc);
	}
	return 0;
}
