#include <cstdio>

using namespace std;

const int inf = 0x7fffffff;

void solve() {
	int sum = 0, xx = 0, mm = inf, n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int x;
		scanf("%d", &x);
		if (x < mm) mm = x;
		sum += x;
		xx ^= x;
	}
	if (xx) printf("NO\n");
	else printf("%d\n", sum - mm);
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