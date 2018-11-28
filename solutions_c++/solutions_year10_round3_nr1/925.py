#include <stdio.h>
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf(" %d", &t);
	for (int i = 1; i <= t; i++) {
		int a[1010], b[1010], n, c = 0;
		scanf(" %d", &n);
		for (int j = 0; j < n; j++)
			scanf(" %d %d", &a[j], &b[j]);
		for (int j = 0; j < n; j++)
			for (int k = j + 1; k < n; k++)
				if ((a[j] > a[k] && b[j] < b[k]) || (a[j] < a[k] && b[j] > b[k]))
					c++;
		printf("Case #%d: %d\n", i, c);
	}
	return 0;
}