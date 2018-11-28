#include <iostream>
using namespace std;

const int N = 50;
char s[N][N + 1];
int dp[N][N][N][N + 1];
int n, m, L;
const int MAX = N * N * 2;

int run(int x, int y, int ss, int tt)
{
	for (--y; y >= 0 && s[x][y] == '.' && (s[x + 1][y] == '#' || x + 1 == n); --y);
	++y;
	int &ret = dp[x][y][ss][tt];
	if (ret >= 0) return ret;
	if (x == n - 1) return ret = 0;
	ret = MAX;
	int z, w, u, v;
	for (z = y + 1; z < m && s[x][z] == '.' && s[x + 1][z] == '#'; ++z);
	--z;
	if (y - 1 >= 0 && s[x][y - 1] == '.')
	{
		for (w = x + 1; w < n && s[w][y - 1] == '.'; ++w);
		if (w - 1 - x <= L) ret = min(ret, run(w - 1, y - 1, 0, 0));
	}
	if (z + 1 < m && s[x][z + 1] == '.')
	{
		for (w = x + 1; w < n && s[w][z + 1] == '.'; ++w);
		if (w - 1 - x <= L) ret = min(ret, run(w - 1, z + 1, 0, 0));
	}
	if (z - y > 0)
	{
		int len;
		for (len = 1; len <= z - y; ++len)
		{
			for (u = y; u + len - 1 <= z; ++u)
			{
				for (v = 0; v < len; ++v) s[x + 1][v + u] = '.';
				if (u > y) // jump from u
				{
					for (w = x + 1; w < n && s[w][u] == '.'; ++w);
					if (w - 1 - x <= L) ret = min(ret, run(w - 1, u, u, u + len) + len);
				}
				if (u + len - 1 < z) // jump from u + len - 1
				{
					for (w = x + 1; w < n && s[w][u + len - 1] == '.'; ++w);
					if (w - 1 - x <= L) ret = min(ret, run(w - 1, u + len - 1, u, u + len) + len);
				}
				for (v = 0; v < len; ++v) s[x + 1][v + u] = '#';
			}
		}
	}
	return ret;
}

int main()
{
	int cas, num = 0;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &cas);
	while (cas--)
	{
		scanf("%d %d %d", &n, &m, &L);
		int i;
		for (i = 0; i < n; ++i)
			scanf("%s", s[i]);
		memset(dp, 255, sizeof(dp));
		printf("Case #%d: ", ++num);
		int ret = run(0, 0, 0, 0);
		if (ret == MAX) puts("No");
		else printf("Yes %d\n", ret);
	}
	return 0;
}
