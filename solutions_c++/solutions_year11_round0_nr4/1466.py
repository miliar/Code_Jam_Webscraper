#include <cstdio>
#include <cstring>

int main() {
	int test, n, x, res;
	scanf("%d", &test);
	for (int i = 0; i < test; i++) {
		scanf("%d", &n);
		res = 0;
		for (int j = 0; j < n; j++) {
			scanf("%d", &x);
			if (x - 1 != j) {
				res++;
			}
		}
		printf("Case #%d: %.6lf\n", i + 1, (double)res);
	}
	return 0;
}
