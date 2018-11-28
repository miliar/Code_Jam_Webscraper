#include <cstdio>
#include <cstring>

int N, K;
int Price[128][32];
int Map[128][128];
int Used[128], Link[128];

int AugPath(int i)
{
	for (int j = 0; j < N; j ++)
		if (Map[i][j] && ! Used[j])
		{
			Used[j] = 1;
			if (Link[j] == -1 || AugPath(Link[j]))
			{
				Link[j] = i;
				return 1;
			}
		}
	return 0;
}

void Work()
{
	scanf("%d%d", &N, &K);
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < K; j ++)
			scanf("%d", &Price[i][j]);
	
	for (int i = 0; i < N; i ++)
		for (int j = 0; j < N; j ++)
		{
			Map[i][j] = 1;
			for (int k = 0; k < K; k ++)
				if (Price[i][k] >= Price[j][k])
				{
					Map[i][j] = 0;
					break;
				}
		}
	
	int Ans = 0;
	memset(Link, -1, sizeof(Link));
	for (int i = 0; i < N; i ++)
	{
		memset(Used, 0, sizeof(Used));
		Ans += AugPath(i);
	}
	printf("%d\n", N - Ans);
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d: ", Case);
		Work();
	}
	return 0;
}
