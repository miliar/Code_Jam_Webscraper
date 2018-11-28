#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

#define pb push_back
#define sz(a) (int)((a).size())
#define ll long long
#define sqr(a) ((a) * (a))

#define Nmax 128

const int dx[6] = {-1, 0, -1, 0, 1, 1};
const int dy[6] = {-1, -1, 1, 1, -1, 1};

int n, m, ct1, ct2;
char mat[Nmax][Nmax];
int cnt[Nmax][Nmax];
vector<int> lv[Nmax * Nmax];
int dest[Nmax * Nmax];
int p[Nmax * Nmax];
int v[Nmax * Nmax];

void citire()
{
	int i;

	scanf("%d %d\n", &n, &m);
	for (i = 1; i <= n; ++i)
		scanf("%s", mat[i] + 1);
}

int cupleaza(int nod)
{
	int i;

    v[nod] = 1;

	for (i = 0; i < sz(lv[nod]); ++i)
		if (!dest[lv[nod][i]])
		{
			p[nod] = lv[nod][i];
			dest[lv[nod][i]] = nod;
			return 1;
		}

	for (i = 0; i < sz(lv[nod]); ++i)
		if (!v[dest[lv[nod][i]]] && cupleaza(dest[lv[nod][i]]))
		{
			p[nod] = lv[nod][i];
			dest[lv[nod][i]] = nod;
			return 1;
		}

	return 0;
}

void solve()
{
	int i, j, d, i0, j0, flux = 0, ok;

    memset(cnt, 0, sizeof(cnt));

	ct1 = ct2 = 0;

	for (i = 1; i <= n; ++i)
		for (j = 1; j <= m; j += 2)
			if (mat[i][j] == '.')
				cnt[i][j] = ++ct1;

	for (i = 1; i <= n; ++i)
		for (j = 2; j <= m; j += 2)
			if (mat[i][j] == '.')
				cnt[i][j] = ++ct2;
 
	for (i = 1; i <= ct1; ++i)
	    vector<int>().swap(lv[i]);
 
	for (i = 1; i <= n; ++i)
		for (j = 1; j <= m; j += 2)
			for (d = 0; d < 6; ++d)
			{
				i0 = i + dx[d];
				j0 = j + dy[d];

				if (cnt[i0][j0]) lv[cnt[i][j]].pb(cnt[i0][j0]);
			}

	memset(p, 0, sizeof(p));
	memset(dest, 0, sizeof(dest));
    do
	{
		ok = 0;
        memset(v, 0, sizeof(v));

		for (i = 1; i <= ct1; ++i)
			if (!p[i] && cupleaza(i))
			{
				++flux;
				ok = 1;
			}
	}
	while (ok);

	printf("%d\n", ct1 + ct2 - flux);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
