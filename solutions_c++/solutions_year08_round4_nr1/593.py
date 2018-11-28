#include <cstdio>

#define MAXM 10011
#define INF 999999999
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int M, V, gate[MAXM], canChange[MAXM], minv[MAXM][2];

void readDataAndSolve()
{
	int N;

	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
		scanf("%d %d", &M, &V);

		for (int i = 1; i <= (M - 1) / 2; i++)
			scanf("%d %d", &gate[i], &canChange[i]);

		for (int i = (M - 1) / 2 + 1; i <= M; i++)
		{
			int value;
			scanf("%d", &value);
			minv[i][value] = 0, minv[i][!value] = INF;
		}

		for (int i = (M - 1) / 2; i > 0; i--)
		{
			int left = 2 * i, right = 2 * i + 1;

			minv[i][0] = minv[i][1] = INF;

			int cGate = gate[i], cost = 0;

			for (int p1 = 0; p1 <= 1; p1++)
				for (int p2 = 0; p2 <= 1; p2++)
				{
					int cval = (cGate == 1 ? (p1 && p2) : (p1 || p2));
					minv[i][cval] = MIN(minv[i][cval], minv[left][p1] + minv[right][p2] + cost);
				}

			if (canChange[i])
			{
				cGate = !gate[i], cost = 1;
				for (int p1 = 0; p1 <= 1; p1++)
					for (int p2 = 0; p2 <= 1; p2++)
					{
						int cval = (cGate == 1 ? (p1 && p2) : (p1 || p2));
						minv[i][cval] = MIN(minv[i][cval], minv[left][p1] + minv[right][p2] + cost);
					}
			}
		}

		if (minv[1][V] == INF)
			printf("Case #%d: IMPOSSIBLE\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, minv[1][V]);
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	readDataAndSolve();

	return 0;
}