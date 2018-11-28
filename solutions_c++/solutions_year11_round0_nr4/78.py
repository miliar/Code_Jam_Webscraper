#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 100000;

int next[maxn];

void solve() {
	int n, ans = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &next[i]);
		next[i]--;
		if (next[i] != i) ans++;
	}
	printf("%d.000000\n", ans);
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}