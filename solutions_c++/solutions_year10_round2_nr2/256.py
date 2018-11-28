#include <stdio.h>
#include <algorithm>

using namespace std;

#define LL long long
#define inf 1000000000

int n, k, b, t;
LL x[55], v[55];
int dp[55][55][55];

int get_max(int i, int j) {
	if (i == n) return j;
	if (j == n) return i;
	return (b - x[i]) * v[j]  > (b - x[j]) * v[i] ? i : j;
}

void relax(int &a, int v) { if (a > v) a = v; }

bool ok(int i) { return i == n ? true : b - x[i] <= t * v[i]; }

int small() {
	int ret = inf;
	if (k == 0) return 0;
	if (k == 1) {
		for (int i = 0; i < n; ++i) {
			if (ok(i))
				relax(ret, n - i - 1);
		}
	}
	if (k == 2) {
		for (int i=  0; i < n; ++i) if (ok(i))
			for (int j = i+1; j < n; ++j) if (ok(j)) {
				relax(ret, n - i - 2 + n - j - 1);
			}
	}
	if (k == 3) {
		for (int i=  0; i < n; ++i) if (ok(i))
			for (int j = i+1; j < n; ++j) if (ok(j)) 
				for (int l = j+1; l < n; ++l) if (ok(l)) 
					relax(ret, n - i -3 + n - j - 2 + n - l - 1);
	}
	return ret;
}

void go() {
	scanf("%d%d%d%d", &n, &k, &b, &t);
	for (int i = 0; i < n; ++i)
		scanf("%lld", &x[i]);
	for (int i = 0; i < n; ++i)
		scanf("%lld", &v[i]);
	fill(dp[0][0], dp[55][0], inf);
	dp[0][0][n] = 0;
	int ret = inf;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= k; ++j) {
			for (int tm = 0; tm <= n; ++tm) if (dp[i][j][tm] < inf) {
				relax(dp[i+1][j][tm], dp[i][j][tm] + j);
				relax(dp[i+1][j+1][get_max(tm, i)], dp[i][j][tm]);
			}
		}
	}	
	for (int tm = 0; tm <= n; ++tm) if (dp[n][k][tm] < inf && ok(tm))
		relax(ret, dp[n][k][tm]);

	if (ret < inf)
		printf("%d\n", ret);
	else
		puts("IMPOSSIBLE");
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int c;
	scanf("%d", &c);
	for (int i = 0; i < c; ++i) {
		printf("Case #%d: ", i+1);
		go();
	}
}