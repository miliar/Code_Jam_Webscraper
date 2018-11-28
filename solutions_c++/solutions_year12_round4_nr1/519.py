#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 10000 + 10;

int N;
int D[MaxN], L[MaxN];
int DP[MaxN], Tar[MaxN];
int GD;

int Work()
{
	memset(DP, 0, sizeof(DP));
	memset(Tar, 0, sizeof(Tar));
	scanf("%d", &N);
	for (int i = 0; i < N; i ++)
		scanf("%d%d", &D[i], &L[i]);
	scanf("%d", &GD);
	
	DP[0] = 1;
	Tar[0] = D[0];
	int OK = DP[0] && (long long) D[0] + (long long) Tar[0] >= (long long) GD;
	for (int i = 1; i < N; i ++)
	{
		Tar[i] = 0;
		for (int j = 0; j < i; j ++)
			if (DP[j] && D[i] - D[j] <= Tar[j])
			{
				DP[i] = 1;
				Tar[i] = max(Tar[i], min(D[i] - D[j], L[i]));
			}
		if (DP[i] && (long long) D[i] + (long long) Tar[i] >= (long long) GD)
			OK = 1;
	}
	return OK;
}

int main()
{
	//freopen("A-small.in", "r", stdin);
	//freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %s\n", Case, Work() ? "YES" : "NO");
	return 0;
}