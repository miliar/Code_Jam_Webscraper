#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int p, q, cell[120];
int dp[120][120];

int bribe(int last, int next)
{
	if (dp[last][next] == -1) {
		int c = -1, x;
		for (int i = last + 1; i < next; i++) {
			x = 0;
			x += cell[next] - cell[i] - 1;
			x += cell[i] - cell[last] - 1;
			x += bribe(last, i);
			x += bribe(i, next);
			//printf("i = %d (%d), last = %d (%d), next = %d (%d), bribe = %d\n", i, cell[i], last, cell[last], next, cell[next], x);
			if (x < c || c < 0) c = x;
		}
		if (c == -1) c = 0;
		dp[last][next] = c;
	}
	//printf("bribe %d %d = %d\n", last, next, dp[last][next]);
	return dp[last][next];
}

int cmp(const void *a, const void *b)
{
	return *(int *) a - *(int *) b;
}

int main()
{
	int cas, cases, i;
	scanf("%d", &cases);
	for (cas = 1; cas <= cases; cas++) {
		scanf("%d%d", &p, &q);
		for (i = 0; i < q; i++) scanf("%d", &cell[i]);
		cell[q] = 0; cell[q + 1] = p + 1;
		qsort(cell, q + 2, sizeof(int), cmp);
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", cas, bribe(0, q + 1));
	}
	return 0;
}
