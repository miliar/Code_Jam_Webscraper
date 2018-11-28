#include <stdlib.h>
#include <stdio.h>
int main()
{
	FILE *in = fopen("A-large.in", "r");
	FILE *out = fopen("out.txt", "w");
	int ts, tc, n, k, dp[33];
	for (dp[1] = 1, n = 2; n <= 30; ++n)
		dp[n] = dp[n - 1] + (1 << (n - 1));
	fscanf(in, "%d", &ts); fgetc(in);
	for (tc = 1; tc <= ts; ++tc)
	{
		fscanf(in, "%d %d", &n, &k);
		if (k % (dp[n] + 1) == dp[n])
			fprintf(out, "Case #%d: ON\n", tc);
		else
			fprintf(out, "Case #%d: OFF\n", tc);
	}
	return 0;
}
