#include <stdio.h>

int main(int argc, char *argv[]) {
	int t;
	int n, k;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++) {
		scanf("%d %d", &n, &k);
		int pow = 1<<n;
		if (k % pow == pow - 1) printf("Case #%d: ON\n", z);
		else printf("Case #%d: OFF\n", z);
	}
	return 0;
}
