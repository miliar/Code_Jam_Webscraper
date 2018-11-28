#include <stdio.h>

int N, K, B, T;
int X[55], V[55];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int C;
	scanf("%d", &C);

	for (int cas = 0; cas < C; ++cas)
	{
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &X[i]);
		}
		int total = 0;
		for (int i = 0; i < N; ++i)
		{
			scanf("%d", &V[i]);
			if (X[i] + V[i] * T >= B) ++total;
		}
		printf("Case #%d: ", cas + 1);
		if (total < K)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			int swap[55];
			int ans = 0;
			for (int i = N - 1; K > 0 && i >= 0; --i)
			{
				if (X[i] + V[i] * T >= B)
				{
					--K;
					swap[i] = 0;
					for (int j = i + 1; j < N; ++j)
						ans += swap[j];
				}
				else
					swap[i] = 1;
			}
			printf("%d\n", ans);
		}
	}

	return 0;
}
