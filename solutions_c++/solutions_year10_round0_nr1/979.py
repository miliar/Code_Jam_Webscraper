#include <stdio.h>
#include <string.h>
#include <algorithm>

int n, k;
bool on[256];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &k);
		memset(on, false, sizeof(on));

		bool ok = (k+1) % (1<<n) == 0;

		printf("Case #%d: %s\n", tt, (ok ? "ON" : "OFF"));
	}
	return 0;
}
