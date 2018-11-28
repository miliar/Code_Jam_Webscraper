#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int ncomp;
int n, m, K;

int end[10][10], dg[10], a[10], b[10];

int d[10][10], deg[10];

int ans;
int x[10];
bool col[10];
int check()
{
	int mx = -1;
	for (int i = 0; i < ncomp; ++i)
	{
		memset(col, 0, sizeof(col));
		for (int j = 0; j < deg[i]; ++j)
			col[x[d[i][j]]] = 1;
		int w = 0;
		for (int j = 1; j <= K; ++j)
			w += col[j];
		if (i == 0)
			mx = w;
		else
			if (mx != w)
				return -1;
	}
	return mx;
}
int y[10];
void solve(int p)
{
	if (p == n)
	{
		int w = check();
		if (ans < w)
		{
			ans = w;
			if (ans == 3)
				ans = ans;
			for (int i = 0; i < n; ++i)
				y[i] = x[i];
		}
		return;
	}
	for (int i = 1; i <= K; ++i)
	{
		x[p] = i;
		solve(p + 1);
	}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int nt = 1; nt <= T; ++nt)
	{
		int i, j, k;
		scanf("%d%d", &n, &m);
		if (m == 0)
		{
			printf("Case #%d: %d\n", nt, n);
			for (i = 1; i <= n; ++i)
				printf("%d%c", i, i == n ? '\n':' ');
			continue;
		}

		memset(dg, 0, sizeof(dg));
		for (i = 0; i < m; ++i)
		{
			scanf("%d", a + i);
			--a[i];
		}
		for (i = 0; i < m; ++i)
		{
			scanf("%d", b + i);
			--b[i];
			if (a[i] > b[i])
				swap(a[i], b[i]);
			end[b[i]][dg[b[i]]++] = a[i];
		}
		for (i = 0; i < n; ++i)
		{
			sort(end[i], end[i] + dg[i]);
			reverse(end[i], end[i] + dg[i]);
		}

		int s[10], sz = 0;
		ncomp = 0;
		for (i = 0; i < n; ++i)
		{
			j = 0;
			for (k = sz - 1; j < dg[i] && k >= 0; --k)
				if (s[k] == end[i][j])
				{
					deg[ncomp] = 0;
					d[ncomp][deg[ncomp]++] = i;
					while (s[sz-1] != end[i][j])
					{
						d[ncomp][deg[ncomp]++] = s[sz - 1];
						--sz;
					}
					d[ncomp][deg[ncomp]++] = end[i][j];
					++j;
					++ncomp;
				}
			s[sz++] = i;
		}
		deg[ncomp] = sz;
		for (i = 0; i < sz; ++i)
			d[ncomp][i] = s[i];
		++ncomp;

		K = n;
		for (i = 0; i < ncomp; ++i)
			K = min(K, deg[i]);

		ans = 0;
		solve(0);
		printf("Case #%d: %d\n", nt, ans);
		for (i = 0; i < n; ++i)
			printf("%d%c", y[i], i == n-1?'\n':' ');
	}
	return 0;
}
