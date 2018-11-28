#include <stdio.h>

void solve() {
	int N, K;
	scanf("%d%d", &N, &K);
	int m = (1 << N) - 1;
	if ((K & m) == m) puts("ON"); else puts("OFF");
}

int main() {
	int n;
	scanf("%d", &n);
	for (int case_x = 1; case_x <= n; case_x++) {
		printf("Case #%d: ", case_x);
		solve();
	}
	return 0;
}
