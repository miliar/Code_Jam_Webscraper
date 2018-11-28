#include <stdio.h>

const int MAXM = 0xFFFFF, MAXN = 1000;

int n;
int f[2][MAXM];
int a[MAXN];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int k = 0; k < cases; ++k) {
		printf("Case #%d: ", k + 1);
		scanf("%d", &n);
		int xorall = 0;
		int sum = 0;
		int min = 0xFFFFF;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a[i]);
			xorall ^= a[i];
			sum += a[i];
			if (a[i] < min) min = a[i];
		}
		if (xorall != 0) {
			printf("NO\n");
		} else {
			printf("%d\n", sum - min);
		}
	}
	return 0;
}

