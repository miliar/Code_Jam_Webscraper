#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int T, n;
	int a[1006] = {0}, b[1006] = {0};
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	scanf("%d", &T);
	for (int C=1; C<=T; C++) {
		int count = 0;
		scanf("%d", &n);
		for (int i=0; i<n; i++)
			scanf("%d %d", &a[i], &b[i]);
		for (int i=0; i<n; i++) {
			for (int j=i+1; j<n; j++) {
				if (a[i] < a[j] && b[i] >= b[j]) count++;
				if (a[i] > a[j] && b[i] <= b[j]) count++;
			}
		}
		printf("Case #%d: %d\n", C, count);
	}
	return 0;
}
