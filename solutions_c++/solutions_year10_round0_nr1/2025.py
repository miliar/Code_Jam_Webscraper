#include <cstdio>

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ti++) {
		int n, k;
		scanf("%d%d", &n, &k);
		int rest = (1 << n);
		printf("Case #%d: ", ti + 1);
		if (k % rest == rest - 1) {
			printf("ON\n");
		}
		else {
			printf("OFF\n");
		}
	}
	return 0;
}
