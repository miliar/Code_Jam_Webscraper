#include <cstdio>
#include <memory.h>

int Tests, Cases;
int N, K;
int Y[110][50], Map[110][110];
int Link[110];
bool y[110];

bool Check(int a, int b)
{
	/*if (Y[a][0] > Y[b][0])
	{
		int c = a; a = b; b = c;
	}*/
	for (int i = 0; i < K; ++ i)
		if (Y[a][i] >= Y[b][i])
			return false;
	return true;
}

bool find(int u)
{
	for (int i = 0; i < N; ++ i)
		if (!y[i] && Map[u][i])
		{
			y[i] = true;
			if (Link[i] < 0 || find(Link[i]))
			{
				Link[i] = u;
				return true;
			}
		}
	return false;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &Tests);
	for (int Cases = 1; Cases <= Tests; ++ Cases)
	{
		memset(Map, 0, sizeof(Map));
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++ i)
			for (int j = 0; j < K; ++ j)
				scanf("%d", &Y[i][j]);
		for (int i = 0; i < N; ++ i)
			for (int j = 0; j < N; ++ j)
				if (i != j && Check(i, j))
				{
					Map[i][j] = 1;
				}
		memset(Link, 0xFF, sizeof(Link));
		int Ans = 0;
		for (int i = 0; i < N; ++ i)
		{
			memset(y, 0, sizeof(y));
			if (find(i)) ++ Ans;
		}
		printf("Case #%d: %d\n", Cases, N - Ans);
	}
}
