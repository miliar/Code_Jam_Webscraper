#include <cstdio>
using namespace std;
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <iostream>

void solve() {
	long long n, k, b, t;
	cin >> n >> k >> b >> t;
	vector<long long> x(n);
	vector<long long> v(n);
	for (int i = 0; i < n; ++i) cin >> x[i];
	for (int i = 0; i < n; ++i) cin >> v[i];
	vector<bool> can(n);
	for (int i = 0; i < n; ++i)
		if ((b - x[i]) <= t * v[i])
			can[i] = true;
		else
			can[i] = false;
	vector<int> cost(n);
	for (int i = 0; i < n; ++i)
		if (can[i]) {
			cost[i] = 0;
			for (int j = n - 1; j > i; --j)
				if (!can[j]) {
					cost[i] = j - i;
					break;
				}
		}
		else
			cost[i] = 1000000;
	sort(cost.begin(), cost.end());
	int ans = 0;
	for (int i = 0; i < k; ++i)
		ans += cost[i];
	if (ans >= 1000000) {
		printf("IMPOSSIBLE");
	}
	else
		printf("%d", ans);
}

void true_solve() {
	long long n, k, b, t;
	cin >> n >> k >> b >> t;
	vector<long long> x(n);
	vector<long long> v(n);
	for (int i = 0; i < n; ++i) cin >> x[i];
	for (int i = 0; i < n; ++i) cin >> v[i];
	vector<bool> can(n);
	for (int i = 0; i < n; ++i)
		if ((b - x[i]) <= t * v[i])
			can[i] = true;
		else
			can[i] = false;
	int count_cool = 0;
	int ans = 0;
	for (int i = n - 1; i >= 0; --i)
		if (can[i])
			++count_cool;
	       	else {
	       		if (count_cool < k)
	       			ans += k - count_cool;
	       	}
	if (count_cool < k) {
		printf("IMPOSSIBLE");
	}
	else
		printf("%d", ans);
}


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d: ", i + 1);
		true_solve();
		printf("\n");
	}
	return 0;
}

