#include <cstdio>

int getArea(int x0, int y0, int x1, int y1, int x2, int y2)
{
	int d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0);

	if (d < 0)
		d = -d;

	return d;
}

void readAndSolve()
{
	int N;

	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		int N, M, A;

		scanf("%d %d %d", &N, &M, &A);

		for (int p0 = 0; p0 <= N; p0++)
			for (int p1 = 0; p1 <= M; p1++)
				for (int p2 = 0; p2 <= N; p2++)
					for (int p3 = 0; p3 <= M; p3++)
					{
						if (!p0 && !p1)
							continue;
						if (!p2 && !p3)
							continue;
						if (p0 == p2 && p1 == p3)
							continue;
						if (getArea(0, 0, p0, p1, p2, p3) == A)
						{
							printf("Case #%d: %d %d %d %d %d %d\n", i, 0, 0, p0, p1, p2, p3);
							goto c1;
						}
					}
		
		printf("Case #%d: IMPOSSIBLE\n", i);
c1:
		printf("");
	}
}

int main()
{	
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	readAndSolve();

	return 0;
}