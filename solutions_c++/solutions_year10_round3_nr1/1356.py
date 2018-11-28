#include <cstdio>

int a[1000];
int b[1000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; z++)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d %d", &a[i], &b[i]);
		}
		int inter = 0;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (j == i) continue;
				if ((a[j] > a[i] && b[j] < b[i]) ||
					(a[j] < a[i] && b[j] > b[i]))
				{
					//printf("Found intersection: %d %d, %d %d\n", a[i], b[i], a[j], b[j]);
					inter++;
				}
			}
		}
		inter /= 2;
		printf("Case #%d: %d\n", z, inter);
	}
	return 0;
}
