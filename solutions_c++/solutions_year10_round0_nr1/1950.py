#include <cstdio>

int main() {
	int t, k, n;

	scanf("%d", &t);
	
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		
		scanf("%d %d", &n, &k);
		
		if (k % (1 << n) == (1 << n) - 1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
