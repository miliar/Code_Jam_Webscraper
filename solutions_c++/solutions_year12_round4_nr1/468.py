#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

const double EPS = 1e-12;

int n;

void solve() {
	bool found = false;
	scanf("%d", &n);
	vector<pair<int, int> > a(n);
	for (int i = 0; i < n; ++i) {
		scanf("%d%d", &a[i].first, &a[i].second);
	}
	int d;
	scanf("%d", &d);
	vector<int> dp(n, -1);
	dp[0] = a[0].first;
	for (int i = 0; i < n; ++i) {
		if (a[i].first + dp[i] >= d) {
			found = true;
			break;
		}
		if (dp[i] > 0) {
			for (int j = i + 1; j < n; ++j) {
				if (a[j].first - a[i].first <= dp[i]) {
					dp[j] = max(dp[j], min(a[j].first - a[i].first, a[j].second));
				}
			}
		}
	}
	if (found) {
		printf("YES\n");
	} else {
		printf("NO\n");
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
