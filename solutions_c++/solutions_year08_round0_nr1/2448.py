#include <cstdio>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

#define Nmax 105
#define Mmax 1005

int n, m;
string name[Nmax];
string query[Mmax];
map<string, int> M;
int sir[Mmax];
int D[Mmax], next[Nmax];

void citire()
{
	int i;
	char tmp[Nmax];

	scanf("%d\n", &n);
	for (i = 1; i <= n; ++i)
	{
		fgets(tmp, Nmax, stdin);
		name[i] = tmp;
	}

	scanf("%d\n", &m);
	for (i = 1; i <= m; ++i)
	{
		fgets(tmp, Nmax, stdin);
		query[i] = tmp;
	}
}

void solve()
{
	int i, j, best;

	M.clear();
	for (i = 1; i <= n; ++i)
		M[name[i]] = i;

	for (i = 1; i <= m; ++i)
		sir[i] = M[query[i]];

	memset(next, 0x3f, sizeof(next));
	for (i = m; i >= 1; --i)
	{
		next[sir[i]] = i;
		best = -1;

        for (j = 1; j <= n; ++j)
			best = max(best, next[j]);

		if (best > m) D[i] = 0;
		else D[i] = D[best] + 1;
	}

	printf("%d\n", D[1]);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int i, t;

	scanf("%d\n", &t);

	for (i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
