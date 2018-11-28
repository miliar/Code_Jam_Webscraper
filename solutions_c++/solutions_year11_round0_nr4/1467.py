#include <cstdio>

const int MAXX = 1000;
int array[MAXX+1];

int main()
{
	int T, N;
	int i = 0;
	int j = 0;
	double result = 0;
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);
    while (scanf("%d", &T) != EOF)
	{
		for (i=0; i<T; i++)
		{
			scanf("%d", &N);
			result = 0;
			for (j=0; j<N; j++)
			{
				scanf("%d", &array[j]);
				if (array[j] != j+1)
					result = result + 1;
			}
			printf("Case #%d: %.6f\n", i+1, result);
		}
	}
	return 0;
}
