#include <stdio.h>

bool go(int n, int k) {
	int t = (1 << n) - 1;
	return (t&k) == t;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int n, k;
		scanf("%d%d", &n, &k);
		printf("Case #%d: %s\n", i, go(n, k) ? "ON" : "OFF");
	}
}