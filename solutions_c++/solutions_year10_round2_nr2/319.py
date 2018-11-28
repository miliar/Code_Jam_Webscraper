#include <cstdio>
#include <cstring>
#include <string>
#include <map>

using namespace std;

int N, K, B, T, X[50], V[50];

void solve()
{
	int res = 0;

	for (int chick = N-1; chick >= 0; --chick)
	{
		if (X[chick] + T*V[chick] >= B) { --K; if (K == 0) break; continue; }
		res += K;
	}

	if (K == 0)
		printf("%d\n", res);
	else
		printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int C;
	scanf("%d", &C);
	for (int c = 1; c <= C; ++c)
	{
		printf("Case #%d: ", c);
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for (int i = 0; i < N; ++i) scanf("%d", &X[i]);
		for (int i = 0; i < N; ++i) scanf("%d", &V[i]);
		solve();
	}

	return 0;
}
