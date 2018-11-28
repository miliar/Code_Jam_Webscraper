#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
#define K 100
#define inf 1000000000

int x[110];
char s[110];
int d[110][110];
int main()
{
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int t, l;
	scanf("%d", &t);
	for (l = 1; l <= t; ++l)
	{
		int n, i, j, k;
		scanf("%d", &n);
		for (i = 1; i <= n; ++i)
		{
			char ch[2];
			scanf("%s%d", ch, x + i);
			s[i] = ch[0];
		}
		for (i = 1; i <= n; ++i)
			for (j = 1; j <= K; ++j)
				d[i][j] = inf;
		for (i = 1; i <= K; ++i)
			d[1][i] = max(i - 1, x[1]);
		
		for (i = 1; i < n; ++i)
			for (j = 1; j <= K; ++j)
				if (d[i][j] != -1)
				{
					if (s[i+1] == s[i])
						for (k = 1; k <= K; ++k)
							d[i + 1][k] = min(d[i + 1][k], d[i][j] + max(abs(x[i] - x[i + 1]) + 1, abs(j - k)));
					else
						for (k = 1; k <= K; ++k)
							d[i + 1][k] = min(d[i + 1][k], d[i][j] + max(abs(x[i] - k), abs(x[i + 1] - j) + 1));
				}
		int ans = inf;
		for (k = 1; k <= K; ++k)
			ans = min(ans, d[n][k]);
		printf("Case #%d: %d\n", l, ans);
	}
	return 0;
}
