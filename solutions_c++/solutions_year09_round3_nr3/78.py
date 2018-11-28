#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int QMAX = 105;

int r[QMAX][QMAX];
bool u[QMAX][QMAX];
int g[QMAX], sg[QMAX];
int d[QMAX];
int p, q;

int Count(int i, int j)
{
	if (u[i][j])
		return r[i][j];

	u[i][j] = true;

	if (i == j)
	{
		r[i][j] = 0;
		return 0;
	}

	r[i][j] = Count(i, i) + Count(i + 1, j) + sg[j] - sg[i - 1] + j - i - 1;
	for (int k = i + 1; k < j; k++)
		r[i][j] = min(r[i][j], Count(i, k) + Count(k + 1, j) + sg[j] - sg[i - 1] + j - i - 1);

	return r[i][j];
}

int Solve()
{
	memset(u, false, sizeof(u));

	d[0] = 0;
	d[q + 1] = p + 1;
	for (int i = 1; i <= q + 1; i++)
		g[i] = d[i] - d[i - 1] - 1;

	sg[0] = 0;
	for (int i = 1; i <= q + 1; i++)
		sg[i] = sg[i - 1] + g[i];

	int res = Count(1, q + 1);

	return res;
}

int main()
{
	freopen("prison.in", "r", stdin);
	freopen("prison.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int tnum = 1; tnum <= n; tnum++)
	{
		scanf("%d%d", &p, &q);
		for (int i = 1; i <= q; i++)
			scanf("%d", &d[i]);

		printf("Case #%d: %d\n", tnum, Solve());
	}

	return 0;
}
