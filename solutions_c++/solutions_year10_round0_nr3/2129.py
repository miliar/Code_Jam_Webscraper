#include <stdio.h>
#include <string.h>

int main()
{
	int num, R, k, N, g[10000], i, f, c=0;
	scanf("%d", &num);
	while (num)
	{
		c++;
		num--;
		scanf("%d %d %d", &R, &k, &N);
		for (i = 0; i < N; i++)
		{
		  scanf("%d", &g[i]);
		}
		i = 0;
		int resp = 0;
		int j = N-1;
		while (i < R)
		{
			int res = 0;
			f = -1;
			while ((res + g[(j + 1)%N]) <= k && f != j)
			{
				if (res == 0)
					f = j;
				j = (j+1)%N;
				res += g[j];
				resp += g[j];
			}
			i++;
		}
		printf("Case #%d: %d\n", c, resp);
	}
	return 0;
}
