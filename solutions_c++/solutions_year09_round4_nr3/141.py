#include <iostream>

using namespace std;

const int MaxN = 205;
const int MaxK = 30;

int N, K, Ans, TCase, Match[MaxN], S[MaxN][MaxK];
bool Map[MaxN][MaxN], Used[MaxN];

bool Hungary(int T)
{
	for (int i = 1; i <= N; i++)
		if (Map[T][i] && !Used[i])
		{
			Used[i] = 1;
			if (!Match[i] || Hungary(Match[i]))
			{
				Match[i] = T;
				return 1;
			}
		}
	return 0;
}

bool Ok(int a, int b)
{
	for (int i = 1; i <= K; i++)
		if (S[a][i] <= S[b][i]) return 0;
	return 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case)
	{
		scanf("%d%d", &N, &K);
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= K; ++j)
				scanf("%d", &S[i][j]);
		memset(Map, 0, sizeof(Map));
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				if (Ok(i, j)) Map[i][j] = 1;
		memset(Match, 0, sizeof(Match));
		Ans = N;
		for (int i = 1; i <= N; ++i) {
			memset(Used, 0, sizeof(Used));
			if (Hungary(i)) Ans--;
		}
		printf("Case #%d: %d\n", Case, Ans);
	}
	return 0;


	/*scanf("%d%d", &N, &M);
	memset(Map, 0, sizeof(Map));
	int x, y;
	for (int i = 0; i < M; i++)
	{
		scanf("%d%d\n", &x, &y);
		Map[x][y] = Map[y][x] = 1;
	}
	memset(Match, 0, sizeof(Match));
	Ans = 0;
	for (int i = 1; i <= N; i++)
	{
		memset(Used, 0, sizeof(Used));
		if (Hungary(i)) Ans++;
	}
	printf("%d", Ans / 2);*/
}
