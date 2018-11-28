#include <cstdio>
#include <cstring>

int main() {
	int test, n, x;
	scanf("%d", &test);
	for (int i = 0; i < test; i++) {
		scanf("%d", &n);
		int now = 0, tot = 0, m = 10000000;
		for (int j = 0; j < n; j++) {
			scanf("%d", &x);
			now ^= x;
			tot += x;
			m = x < m ? x : m;
		}
		printf("Case #%d: ", i + 1);
		if (now) {
			puts("NO");
		} else {
			printf("%d\n", tot - m);
		}
	}

	return 0;
}
