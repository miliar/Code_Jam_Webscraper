#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int m;
vector<int> a;

void solve()
{
	scanf("%d", &m);
	a.resize(m);
	for (int i = 0; i < m; ++i) {
		scanf("%d", &a[i]);
	}
	int x = 0;
	for (int i = 0; i < m; ++i) {
		x ^= a[i];
	}
	if (x != 0) {
		printf("NO\n");
	} else {
		sort(a.begin(), a.end());
		int ans = 0;
		for (int i = 1; i < m; ++i) {
			ans += a[i];
		}
		printf("%d\n", ans);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
