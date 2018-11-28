#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1024;

int N, RR;
int Miss[MaxN];
int MinMiss[MaxN][MaxN];
int DP[MaxN][MaxN][11];
int Price[11][MaxN];

int Search(int L, int R, int MISSED, int Round)
{
	if (L == R)
		return 0;
	if (DP[L][R][MISSED] != -1)
		return DP[L][R][MISSED];
	//printf("[%d %d] %d\n", L, R, Price[Round][L >> (RR - Round)]);
	int Mid = (L + R) / 2;
	DP[L][R][MISSED] = Price[Round][L >> (RR - Round)] + Search(L, Mid, MISSED, Round + 1) + Search(Mid + 1, R, MISSED, Round + 1);
	if (MinMiss[L][R] > MISSED)
		DP[L][R][MISSED] = min(DP[L][R][MISSED], Search(L, Mid, MISSED + 1, Round + 1) + Search(Mid + 1, R, MISSED + 1, Round + 1));
	return DP[L][R][MISSED];
}

int Work()
{
	scanf("%d", &RR);
	N = 1 << RR;
	for (int i = 0; i < N; i ++)
		scanf("%d", &Miss[i]);
	for (int i = 0; i < N; i ++)
	{
		MinMiss[i][i] = Miss[i];
		for (int j = i + 1; j < N; j ++)
			MinMiss[i][j] = min(MinMiss[i][j - 1], Miss[j]);
	}
	for (int i = (RR - 1); i >= 0; i --)
		for (int j = 0; j < (1 << i); j ++)
			scanf("%d", &Price[i][j]);
	memset(DP, -1, sizeof(DP));
	return Search(0, N - 1, 0, 0);
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
