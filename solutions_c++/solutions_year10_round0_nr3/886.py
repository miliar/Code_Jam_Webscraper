#include <cstdio>
#include <iostream>
using namespace std;
#include <vector>

void doit() {
	int r, k, n;
	scanf("%d%d%d", &r, &k, &n);
	vector<long long> a, where, cost;
	a.resize(n);
	where.resize(n);
	cost.resize(n);
	long long sum = 0;
	for (int i = 0; i < n; ++i) {
		cin >> a[i];
		sum += a[i];
	}
	if (sum <= k) {
		cout << sum * r;
		return;
	}
	for (int i = 0; i < n; ++i) {
		long long p = 0;
		int j = i;
		while (p + a[j] <= k) {
			p += a[j];
			j = (j + 1) % n;
		}
		where[i] = j;
		cost[i] = p;
	}
	long long ans = 0;
	int cur = 0;
	for (int i = 0; i < r; ++i) {
		ans += cost[cur];
		cur = where[cur];
	}
	cout << ans;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		doit();
		printf("\n");
		cerr << i << " " << t << endl;
	}
	return 0;
}
