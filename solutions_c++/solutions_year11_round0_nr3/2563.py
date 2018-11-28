#include <stdio.h>

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		int n;
		scanf("%d", &n);
		int A[n];
		int menor = 2147483647, xort = 0, soma = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", A+i);
			if (A[i] < menor) {
				menor = A[i];
			}
			xort^= A[i];
			soma+= A[i];
		}
		printf("Case #%d: ", test);
		if (xort == 0) {
			printf("%d\n", soma - menor);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}

