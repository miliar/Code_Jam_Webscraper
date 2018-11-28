#include <cstdio>

#define CODE A-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

bool solve() {
	int n, k;
	scanf("%d %d\n", &n, &k);
	int m = (1 << n) - 1;
	return (k & m) == m;
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: %s\n", i, solve() ? "ON" : "OFF");
	}
	return 0;
}
