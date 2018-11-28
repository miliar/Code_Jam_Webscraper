#include <stdio.h>
#include <limits.h>

int main() {
	int t;
	scanf("%d", &t);
	int i, j;
	for(i = 1; i <= t; i++) {
		int n;
		scanf("%d", &n);
		int sum = 0;
		int smallest = INT_MAX;
		int total = 0;
		for(j = 0; j < n; j++) {
			int v;
			scanf("%d", &v);
			if (v < smallest) smallest = v;
			sum ^= v;
			total += v;
		}
		printf("Case #%d: ", i);
		if (sum != 0) {
			printf("NO");
		} else {
			printf("%d", total - smallest);
		}
		putchar('\n');
	}
}
	
