#include <cstdio>

int main() {
//	freopen("A-small.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i + 1);
		int a, b;
		scanf("%d %d", &a, &b);
		if (b % (1 << a) == ((1 << a) - 1)) {
			printf("ON");
		} else {
			printf("OFF");
		}
		printf("\n");
	}

	return 0;
}
