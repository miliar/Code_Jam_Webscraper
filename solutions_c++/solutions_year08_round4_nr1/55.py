#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int dp[10000][2];
int M, V, G[10000], C[10000], I[10000];

int doit(int n, int v)
{
	if (I[n] >= 0) {
		if (I[n] != v) {
			return (1 << 20);
		} else {
			return 0;
		}
	}
	if (dp[n][v] >= 0) {
		return dp[n][v];
	}

	int ret = (1 << 20);
	if (v == 0 && G[n] == 1) {
		ret = min(ret, doit(n * 2 + 1, 0) + doit(n * 2 + 2, 0));
		ret = min(ret, doit(n * 2 + 1, 1) + doit(n * 2 + 2, 0));
		ret = min(ret, doit(n * 2 + 1, 0) + doit(n * 2 + 2, 1));
	} else if (v == 0 && G[n] == 0) {
		ret = min(ret, doit(n * 2 + 1, 0) + doit(n * 2 + 2, 0));
		if (C[n] == 1) {
			ret = min(ret, doit(n * 2 + 1, 0) + doit(n * 2 + 2, 1) + 1);
			ret = min(ret, doit(n * 2 + 1, 1) + doit(n * 2 + 2, 0) + 1);
		}
	} else if (v == 1 && G[n] == 1) {
		ret = min(ret, doit(n * 2 + 1, 1) + doit(n * 2 + 2, 1));
		if (C[n] == 1) {
			ret = min(ret, doit(n * 2 + 1, 0) + doit(n * 2 + 2, 1) + 1);
			ret = min(ret, doit(n * 2 + 1, 1) + doit(n * 2 + 2, 0) + 1);
		}
	} else if (v == 1 && G[n] == 0) {
		ret = min(ret, doit(n * 2 + 1, 1) + doit(n * 2 + 2, 1));
		ret = min(ret, doit(n * 2 + 1, 0) + doit(n * 2 + 2, 1));
		ret = min(ret, doit(n * 2 + 1, 1) + doit(n * 2 + 2, 0));
	}

	return (dp[n][v] = ret);
}

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int casenum = 1; casenum <= cases; casenum++) {
		gets(inp); sscanf(inp, "%d%d", &M, &V);
		for (int i = 0; i < (M - 1) / 2; i++) {
			gets(inp); sscanf(inp, "%d%d", &(G[i]), &(C[i]));
			I[i] = -1;
		}
		for (int i = (M - 1) / 2; i < M; i++) {
			gets(inp); sscanf(inp, "%d", &(I[i]));
			G[i] = -1;
			C[i] = -1;
		}

		memset(&(dp[0][0]), -1, sizeof(dp));
		int s = doit(0, V);

		if (s < (1 << 20)) {
			printf("Case #%d: %d\n", casenum, s);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", casenum);
		}
	}

	return 0;
}
