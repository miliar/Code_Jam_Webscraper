#include <cstdio>
#include <cstdlib>

struct Pairs
{
	int x, y;
};

int cmp(const void* a, const void* b)
{
	return (*(Pairs*)a).x - (*(Pairs*)b).x;
}

int main ()
{
	int T, N;
	Pairs p[1010];
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	for (int c = 1; c <= T; c++)
	{
		scanf("%d", &N);
		int res = 0;
		for (int i = 0; i < N; i++)
			scanf("%d%d", &p[i].x, &p[i].y);

		qsort (p, N, sizeof(p[0]), cmp);
		for (int i = 0; i < N; i++)
		{
			for (int j = i + 1; j < N; j++)
			{
				if (p[i].y > p[j].y)
					res++;
			}
		}
		printf ("Case #%d: %d\n", c, res);
	}
}
