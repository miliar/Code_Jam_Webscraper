#include <iostream>

using namespace std;

const int MaxN = 105;
const int Dx[4] = {-1, 0, 0, 1};
const int Dy[4] = {0, -1, 1, 0};

int TCase, H, W, Map[MaxN][MaxN], F[MaxN * MaxN], C[MaxN * MaxN], Num[MaxN][MaxN];

int GetFather(int x)
{
	if (F[x] != x) F[x] = GetFather(F[x]);
	return F[x];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; Case++)
	{
		scanf("%d%d", &H, &W);
		int num = 0;
		for (int i = 1; i <= H; i++)
			for (int j = 1; j <= W; j++)
			{
				scanf("%d", &Map[i][j]);
				Num[i][j] = ++ num;
				F[num] = num;
			}
		for (int i = 1; i <= H; i++)
			for (int j = 1; j <= W; j++)
			{
				int Min = 10005, P = -1;
				for (int k = 0; k < 4; k++)
				{
					int x = i + Dx[k], y = j + Dy[k];
					if (x < 1 || y < 1 || x > H || y > W || Map[x][y] >= Map[i][j]) continue;
					if (Min > Map[x][y]) Min = Map[x][y], P = k;
				}
				if (P >= 0) F[Num[i][j]] = F[Num[i + Dx[P]][j + Dy[P]]];
			}
		num = 0;
		memset(C, 0, sizeof(C));
		for (int i = 1; i <= H; i++)
			for (int j = 1; j <= W; j++)
			{
				int f = GetFather(Num[i][j]);
				if (C[f] == 0) C[f] = ++num;
			}
		printf("Case #%d:\n", Case);
		for (int i = 1; i <= H; i++)
		{
			for (int j = 1; j < W; j++)
				printf("%c ", C[F[Num[i][j]]] + 96);
			printf("%c\n", C[F[Num[i][W]]] + 96);
		}
	}
	return 0;
}
