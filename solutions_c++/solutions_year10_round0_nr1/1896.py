#include <cstdio>

int main() {
	int t, n, k, m;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
		m = (1<<n)-1;
		if ((k & m) == m)
			printf("Case #%d: ON\n", i);
		else
			printf("Case #%d: OFF\n", i);
	}
	return 0;
}
