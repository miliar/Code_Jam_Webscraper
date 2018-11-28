#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int t, n, c[1024];

void solve();

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		solve();
	return 0;
}

void solve() {
	scanf("%d", &n);
	int k = 0, sum = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%d", &c[i]);
		k ^= c[i];
		sum += c[i];
	}
	sort(c, c + n);
	if (k != 0)
		printf("Case #%d: NO\n", ++t);
	else
		printf("Case #%d: %d\n", ++t, sum - c[0]);
}
