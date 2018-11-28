#include <stdio.h>
#include <stdlib.h>

#define MAX 1024

int n, s, p, g[MAX], ans;

int sort_function(const void *a, const void *b) {
	return *((int *)b) - *((int *)a);
}

void action() {
	scanf("%d %d %d", &n, &s, &p);
	for(int i = 0; i < n; i++)
		scanf("%d", &g[i]);
	qsort((void *)g, n, sizeof(g[0]), sort_function);

	ans = 0;
	for(int i = 0; i < n; i++)
		if(g[i] / 3 + (g[i] % 3 > 0) >= p) {
			ans++;
		} else if(s > 0 && g[i] / 3 + (g[i] > 0) + (g[i] % 3 == 2) >= p) {
			ans++;
			s--;
		} else {
			break;
		}
	printf("%d", ans);
}

int main() {
	int t;
	scanf("%d ", &t);
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		action();
		printf("\n");
	}

	return 0;
}
