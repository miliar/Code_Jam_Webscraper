#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int MOD = 100003;
const int MAXN = 511;
typedef long long i64;


i64 c[MAXN + 1][MAXN + 1];
i64 d[MAXN + 1][MAXN + 1];
i64 ans[MAXN + 1];

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	memset(c, 0, sizeof(c));
	for (int i = 0; i <= MAXN; i++)
		c[i][0] = c[i][i] = 1;
	for (int i = 2; i <= MAXN; i++)
		for (int j = 1; j < i; j++)
			c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;

	memset(d, 0, sizeof(d));
	d[1][0] = 1;
	for (int i = 2; i <= MAXN; i++)
	{
		d[i][1] = 1;
		for (int j = 2; j < i; j++)
		{
			for (int k = 1; k < j; k++)
			{
				d[i][j] = (d[i][j] + d[j][k] * c[i - j - 1][j - k - 1]) % MOD;
			}
		}
	}
	memset(ans, 0, sizeof(ans));
	for (int i = 2; i <= MAXN; i++)
	{
		for (int j = 1; j < i; j++)
			ans[i] = (ans[i] + d[i][j]) % MOD;
	}

	int tcn, n;
	scanf("%d", &tcn);
	for (int tc = 1; tc <= tcn; tc++)
	{
		scanf("%d", &n);
		printf("Case #%d: %lld\n", tc, ans[n]);
	}

	return 0;
}
