#include <iostream>
using namespace std;

#define inf 1000000

int i, j, k, n, m, res, d, x, y;
int t, T;

int v[50000], c[50000], tp[50000];

int miin(int x, int y) {
	return x < y ? x : y;
}

int dp[50000][3];

int dfs(int cur, int cost, int tg) {
	int mn = inf;
	int t, t1, t2;
	if (tp[cur] == 0) {
		if (v[cur] != tg) {
			return inf;
		}
		return 0;
	}
	if (dp[cur][tg] != -1) {
		return dp[cur][tg];
	}
	if (c[cur] == 0) {
		if (tp[cur] == 1) { // or
			if (tg == 0) {
				t1 = dfs(cur + cur, cost, 0);
				t2 = dfs(cur + cur + 1, cost, 0);
				mn = miin(mn, t1 + t2);
			} else {
				t1 = dfs(cur+cur, cost, 1);
				t2 = miin(dfs(cur + cur + 1, cost, 0), dfs(cur + cur + 1, cost, 1));
				mn = miin(mn, t1 + t2);
				t1 = dfs(cur+cur+1, cost, 1);
				t2 = miin(dfs(cur + cur, cost, 0), dfs(cur + cur, cost, 1));
				mn = miin(mn, t1 + t2);
			}
		} else { // and
			if (tg == 1) {
				t1 = dfs(cur + cur, cost, 1);
				t2 = dfs(cur + cur + 1, cost, 1);
				mn = miin(mn, t1 + t2);
			} else {
				t1 = dfs(cur+cur, cost, 0);
				t2 = miin(dfs(cur + cur + 1, cost, 0), dfs(cur + cur + 1, cost, 1));
				mn = miin(mn, t1 + t2);
				t1 = dfs(cur+cur+1, cost, 0);
				t2 = miin(dfs(cur + cur, cost, 0), dfs(cur + cur, cost, 1));
				mn = miin(mn, t1 + t2);
			}
		}
	} else {
		if (tp[cur] == 1) { // or
			if (tg == 0) {
				t1 = dfs(cur + cur, cost, 0);
				t2 = dfs(cur + cur + 1, cost, 0);
				mn = miin(mn, t1 + t2);
			} else {
				t1 = dfs(cur+cur, cost, 1);
				t2 = miin(dfs(cur + cur + 1, cost, 0), dfs(cur + cur + 1, cost, 1));
				mn = miin(mn, t1 + t2);
				t1 = dfs(cur+cur+1, cost, 1);
				t2 = miin(dfs(cur + cur, cost, 0), dfs(cur + cur, cost, 1));
				mn = miin(mn, t1 + t2);
			}
			if (tg == 1) {
				t1 = dfs(cur + cur, cost, 1);
				t2 = dfs(cur + cur + 1, cost, 1);
				mn = miin(mn, t1 + t2 + 1);
			} else {
				t1 = dfs(cur+cur, cost, 0);
				t2 = miin(dfs(cur + cur + 1, cost, 0), dfs(cur + cur + 1, cost, 1));
				mn = miin(mn, t1 + t2 + 1);
				t1 = dfs(cur+cur+1, cost, 0);
				t2 = miin(dfs(cur + cur, cost, 0), dfs(cur + cur, cost, 1));
				mn = miin(mn, t1 + t2 + 1);
			}
		} else { // and
			if (tg == 1) {
				t1 = dfs(cur + cur, cost, 1);
				t2 = dfs(cur + cur + 1, cost, 1);
				mn = miin(mn, t1 + t2);
			} else {
				t1 = dfs(cur+cur, cost, 0);
				t2 = miin(dfs(cur + cur + 1, cost, 0), dfs(cur + cur + 1, cost, 1));
				mn = miin(mn, t1 + t2);
				t1 = dfs(cur+cur+1, cost, 0);
				t2 = miin(dfs(cur + cur, cost, 0), dfs(cur + cur, cost, 1));
				mn = miin(mn, t1 + t2);
			}
			if (tg == 0) {
				t1 = dfs(cur + cur, cost, 0);
				t2 = dfs(cur + cur + 1, cost, 0);
				mn = miin(mn, t1 + t2 + 1);
			} else {
				t1 = dfs(cur+cur, cost, 1);
				t2 = miin(dfs(cur + cur + 1, cost, 0), dfs(cur + cur + 1, cost, 1));
				mn = miin(mn, t1 + t2 + 1);
				t1 = dfs(cur+cur+1, cost, 1);
				t2 = miin(dfs(cur + cur, cost, 0), dfs(cur + cur, cost, 1));
				mn = miin(mn, t1 + t2 + 1);
			}
		}
	}
	return dp[cur][tg] = mn;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (t = 1; t <= T; t ++) {
		memset(v, 0, sizeof(v));
		memset(c, 0, sizeof(c));
		memset(tp, 0, sizeof(tp));
		memset(dp, -1, sizeof(dp));

		cin >> n >> d;
		// 2 = and   1 = or
		for (i = 1; i <= n / 2; i ++) {
			cin >> x >> y;
			c[i] = y;
			tp[i] = x + 1;
		}

		for (; i <= n; i ++) {
			cin >> x;
			v[i] = x;
		}

		res = dfs(1, 0, d);
		cout << "Case #" << t << ": ";
		if (res >= inf) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << res << endl;
		}
	}
	return 0;
}
