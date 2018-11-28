#include <cstdio>

int nCases;

int main() {
	freopen("q1.in", "r", stdin);
	scanf("%d", &nCases);

	for (int c = 0; c < nCases; c++) {
		int n, k;
		scanf("%d %d", &n, &k);
		k %= 1 << n;
		printf("Case #%d: %s\n", c+1, (k==(1<<n)-1)? "ON":"OFF");
	}

	return 0;
}
