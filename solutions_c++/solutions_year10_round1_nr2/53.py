#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 100 + 5;
const int MaxC = 256;

int D, I, M, N;
int A[MaxN];
int DP[MaxN][MaxC]; // 当前处理第i个, 前一个是j
int Used[MaxC];

void Dijkstra(int* Dist, int ii)
{
	memset(Used, 0, sizeof(Used));
	while (1)
	{
		int Min = -1;
		for (int i = 0; i < MaxC; i ++)
			if (! Used[i] && (Min == -1 || Dist[Min] > Dist[i]))
				Min = i;
		if (Min == -1)
			break;
		Used[Min] = 1;
		for (int i = max(0, Min - M); i <= min(Min + M, MaxC - 1); i ++)
			Dist[i] = min(Dist[i], Dist[Min] + I);
	}
}

int Work()
{
	scanf("%d%d%d%d", &D, &I, &M, &N);
	for (int i = 0; i < N; i ++)
		scanf("%d", &A[i]);

	memset(DP, 10, sizeof(DP));
	for (int i = 0; i < N; i ++)
	{
		for (int j = 0; j < MaxC; j ++)
			DP[i + 1][j] = min(DP[i + 1][j], D * i + abs(j - A[i]));
		// Insert
		Dijkstra(DP[i], i);
		// Modify
		for (int k = 0; k < MaxC; k ++)
			for (int j = max(0, k - M); j <= min(k + M, MaxC - 1); j ++)
				DP[i + 1][k] = min(DP[i + 1][k], DP[i][j] + abs(k - A[i]));
		// Delete
		for (int j = 0; j < MaxC; j ++)
			DP[i + 1][j] = min(DP[i + 1][j], DP[i][j] + D);
	}

	int Ans = D * N;
	for (int j = 0; j < MaxC; j ++)
		Ans = min(Ans, DP[N][j]);
	return Ans;
}

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %d\n", Case, Work());
	return 0;
}
