#include <stdio.h>

void main() {
	freopen("C-large.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int num_cases;
	scanf("%d", &num_cases);

	for (int w=0; w<num_cases; w++) {
		int total = 0;
		int check = 0;

		int length;
		scanf("%d", &length);

		int smallest = 100000000;
		for (int k=0; k<length; k++) {
			int tmp;
			scanf("%d", &tmp);
			total += tmp;
			check ^= tmp;

			if (smallest > tmp)
				smallest = tmp;
		}

		printf("Case #%d: ", w+1);

		if (check != 0) {
			printf("NO\n");
		}
		else {
			printf("%d\n", total - smallest);
		}
	}
}