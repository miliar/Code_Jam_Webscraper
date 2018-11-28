#include <cstdio>

int main() {
	// freopen("input.txt", "r", stdin);
	
	// freopen("C-small-attempt0.in", "r", stdin);
	// freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int iTest = 0; iTest < t; ++iTest) {
		int n;
		scanf("%d", &n);
		int xor = 0;
		int min = 1234567890;
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			int num;
			scanf("%d", &num);
			xor = xor ^ num;
			if (num < min)
				min = num;
			sum += num;
		}
		printf("Case #%d: ", iTest + 1);
		if (0 == xor)
			printf("%d", sum - min);
		else
			printf("NO");
		printf("\n");
	}

	return 0;
}