#include <stdio.h>

char tab[64];
int val[40];

int run()
{
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%s", tab);
		int j;
		for (j = 0; j < N; j++)
		{
			if (tab[N-1-j] != '0') break;
		}
		val[i] = j;
	}
	int ret = 0;
	for (int i = 0; i < N; i++)
	{
		int j;
		for (j = i; j < N; j++)
		{
			if (val[j] >= N-1-i)
			{
				break;
			}
		}
		while (j > i)
		{
			val[j] = val[j-1];
			++ret;
			--j;
		}
	}
	return ret;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int n = 1; n <= T; n++)
	{
		printf("Case #%d: %d\n", n, run());
	}
	return 0;
}