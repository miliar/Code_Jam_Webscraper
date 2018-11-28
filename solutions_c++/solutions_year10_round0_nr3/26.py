
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int T, c;

	int prec_cnt[1001];
	int prec_grp[1001];
	int *size_grp = new int[10000001];

	scanf("%d", &T);

	for (int c = 1; c <= T; c++)
	{
		printf("Case #%d: ", c);

		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);
		for (int i = 0; i < N; i++) scanf("%d", &size_grp[i]);

		// precompute
		for (int i = 0; i < N; i++)
		{
			if (size_grp[i] > k)
			{
				prec_cnt[i] = 0;
				prec_grp[i] = i;
			} else
			{
				int sum = size_grp[i];
				int pos = (i+1)%N;
				while (pos != i && sum + size_grp[pos] <= k)
				{
					sum += size_grp[pos];
					pos = (pos + 1)%N;
				}
				prec_cnt[i] = sum;
				prec_grp[i] = pos;
			}
		}

		int pos = 0;
		long long totalsum = 0;
		for (int i = 0; i < R; i++)
		{
			totalsum += prec_cnt[pos];
			pos = prec_grp[pos];
		}

		printf("%lld\n", totalsum);
	}
}

