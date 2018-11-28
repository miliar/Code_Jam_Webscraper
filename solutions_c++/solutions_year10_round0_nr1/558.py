#include <cstdio>

int main() {
	int t, n, k, m;
	scanf("%d", &t);
	for (int z=1; z<=t; z++) {
		scanf("%d%d", &n, &k);
		m = (1<<n) - 1;
		printf("Case #%d: %s\n", z, (k&m)==m ? "ON" : "OFF");
	}
	return 0;
}
