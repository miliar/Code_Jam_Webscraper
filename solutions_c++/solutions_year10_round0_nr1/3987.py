#include <stdio.h>

void solve() {
	int n, k;
	scanf("%d%d", &n, &k);
	int m = 1 << n;
	printf(!(k % m - m + 1) ? "ON" : "OFF");
}

int main() {
	int caseCnt;
	scanf("%d", &caseCnt);
	for (int i = 1; i <= caseCnt; i++) {
		printf("Case #%d: ", i);
		solve();
		printf("\n");
	}
}
