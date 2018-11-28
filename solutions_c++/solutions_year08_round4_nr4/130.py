#include <iostream>
#include <cmath>
#include <deque>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>

using namespace std;

int		K, a[20][20], b[20][20];
int		f[16][16][1 << 16];
char		st[60000];

inline int	two(int k) { return 1 << k; }

int	DFS(int u, int v, int s, int cnt)
{
	if (cnt == 1) return 0;
	if (cnt == 2) return a[u][v];
	int &ret = f[u][v][s];
	for (int k = 0; k < K; ++k) if (u != k && v != k && (two(k) & s))
		ret = max(ret, DFS(k, v, s - two(u), cnt - 1) + a[u][k]);
	return ret;
}

int	main()
{
	int nCase;
	scanf("%d\n", &nCase);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d\n", &K);
		gets(st);
		puts(st);

		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		for (char *s = st; *s; s = s + K)
			for (int i = 0; i < K; ++i)
				for (int j = 0; j < K; ++j) if (i != j)
					if (s[i] == s[j]) ++a[i][j];

		for (char *s = st, *t = st + K; *t; s = s + K, t = t + K)
			for (int i = 0; i < K; ++i)
				for (int j = 0; j < K; ++j) if (i != j)
					if (s[i] == t[j]) ++b[i][j];

		memset(f, 255, sizeof(f));
		int answer = 0;
		for (int i = 0; i < K; ++i) f[i][i][two(i)] = 0;
		for (int i = 0; i < K; ++i)
			for (int j = 0; j < K; ++j)
				answer = max(answer, DFS(i, j, two(K) - 1, K) + b[j][i]);

		printf("Case #%d: %d\n", nowCase, strlen(st) - answer);
	}
	return 0;
}
