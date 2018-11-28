#include <cstdio>
#include <algorithm>
using namespace std;

const int inf = 10000000;
const int maxM = 10005;
int opt[maxM][2];
bool mark[maxM][2];
int C[maxM], G[maxM], I[maxM];
int M, V, L;

int calc(int u, int v)
{
	if (mark[u][v]) return opt[u][v];
	int ret = inf; mark[u][v] = true;
	if (u >= L) ret = (v == I[u]? 0: inf);
	else
	{
		int delta;
		if (G[u]) delta = 0; else delta = (C[u]? 1: inf);
		for (int l = 0; l < 2; l ++)
			for (int r = 0; r < 2; r ++)
				if ((l & r) == v)
					ret = min(ret, calc(u * 2 + 1, l) + calc(u * 2 + 2, r) + delta);
		if (!G[u]) delta = 0; else delta = (C[u]? 1: inf);
		for (int l = 0; l < 2; l ++)
			for (int r = 0; r < 2; r ++)
				if ((l | r) == v)
					ret = min(ret, calc(u * 2 + 1, l) + calc(u * 2 + 2, r) + delta);
	}
	opt[u][v] = ret;
	return ret;
}

int main()
{
	int N;
	scanf("%d", &N);
	for (int _N = 1; _N <= N; _N ++)
	{
		scanf("%d%d", &M, &V);
		L = (M - 1) / 2;
		for (int i = 0; i < L; i ++)
			scanf("%d%d", &G[i], &C[i]);
		for (int i = L; i < M; i ++)
			scanf("%d", &I[i]);
		for (int i = 0; i < M; i ++) mark[i][0] = mark[i][1] = false;
		int ans = calc(0, V);
		printf("Case #%d: ", _N);
		if (ans < inf) printf("%d\n", ans); else printf("IMPOSSIBLE\n");
	}
}
