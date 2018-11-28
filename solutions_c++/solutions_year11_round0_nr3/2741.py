#include <stdio.h>

int main()
{
	int T, N;
	unsigned long long selector, top;
	unsigned long long candies[2000];
	unsigned long long pileSum;

	scanf("%d", &T);

	for(int test = 1; test <= T; test++)
	{
		selector = 1;
		pileSum = 0;
		scanf("%d", &N);

		for(int i = 0; i < N; i++)
		{
			scanf("%I64d", &candies[i]);
		}

		top = (1 << N) - 1;

		while(selector < top)
		{
			unsigned long long sumS = 0;
			unsigned long long sumP = 0;
			unsigned long long realS = 0;
			unsigned long long realP = 0;

			for(int i = 0; i < N; i++)
			{
				if( ((selector >> i) & 1) )
				{
					sumS ^= candies[i];
					realS += candies[i];
				}
				else
				{
					sumP ^= candies[i];
					realP += candies[i];
				}
			}

			if( sumS == sumP )
			{
				selector++;
				unsigned long long candidate = realS >= realP ? realS : realP;
				pileSum = candidate > pileSum ? candidate : pileSum;
			}
			else
			{
				selector++;
			}

		}

		if(!pileSum)
		{
			printf("Case #%d: NO\n", test);
		}
		else
		{
			printf("Case #%d: %I64d\n", test, pileSum);
		}

	}

	return 0;
}