#include <stdio.h>
#include <stdlib.h>

#define MAX 1024

int x[MAX], y[MAX];
long long ans;

int sort_function(const void *a, const void *b) {
	if(*((int *)a) > *((int *)b))return 1;
	if(*((int *)a) < *((int *)b))return -1;
	return 0;
}

int main(int argc, char *argv[])
{
	int i, j;
	int t, c, n;

	scanf("%d", &t);
	for(c = 1; c <= t; c++) {
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%d", &x[i]);
		for(i = 0; i < n; i++)
			scanf("%d", &y[i]);
		qsort((void *)x, n, sizeof(x[0]), sort_function);
		qsort((void *)y, n, sizeof(y[0]), sort_function);

		ans = 0;
		for(i = 0, j = n - 1; i < n; i++, j--)
			ans += (long long)x[i] * (long long)y[j];

		printf("Case #%d: %lld\n", c, ans);
	}

	return 0;
}
