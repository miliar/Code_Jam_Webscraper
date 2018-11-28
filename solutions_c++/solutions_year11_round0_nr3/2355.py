#include <stdio.h>

int main()
{
	int Co[1100] = {0};
	int T, N, i, j, min;
	long long k, sum;
	bool isCrying = false;

	scanf(" %d", &T);

	for(i=0 ; i<T ; i++)
	{
		sum = 0;
		min = -1;
		k = 0;
		scanf(" %d", &N);
		for(j=0 ; j<N ; j++)
		{
			scanf(" %d", &Co[j]);
			if(min == -1)
			{
				min = Co[j];
			}
			if(Co[j] < min)
			{
				min = Co[j];
			}
			sum += Co[j];

			k ^= Co[j];
		}

		if(k != 0)
		{
			printf("Case #%d: NO\n", i+1);
		}
		else
		{
			printf("Case #%d: %d\n", i+1, sum - min);
		}
	}
	return 0;
}