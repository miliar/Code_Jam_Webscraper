#include <cstdio>
#include <vector>

using namespace std;

#define Nmax 1000015
#define pb push_back
#define sz(a) (int)((a).size())
#define ll long long

ll p, a, b, n;
vector<int> lv[Nmax];
int v[Nmax];
int prim[Nmax];

void citire()
{
	scanf("%lld %lld %lld\n", &a, &b, &p);
}

void DF(int nod)
{
	int i;

	v[nod] = 1;
	for (i = 0; i < sz(lv[nod]); ++i)
		if (!v[lv[nod][i]])
			DF(lv[nod][i]);
}

void ciur()
{
	int i, j;

	for (i = 1; i < Nmax; ++i)
		prim[i] = 1;

	for (i = 2; i < Nmax; ++i)
		if (prim[i] == 1)
			for (j = 2 * i; j < Nmax; j += i)
				prim[j] = 0;
}

void solve()
{
	int i, j, last, sol = 0;

    n = b - a;

	for (i = 0; i <= n; ++i)
		vector<int>().swap(lv[i]);

	for (i = p; i <= n + 1; ++i)
	{
		if (!prim[i]) continue;
		last = (i - (a % i)) % i;

		for (j = last + i; j <= n; j += i)
			lv[last].pb(j), lv[j].pb(last);
	}

	memset(v, 0, sizeof(v));
	for (i = 0; i <= n; ++i)
		if (!v[i]) ++sol, DF(i);
	
	printf("%d\n", sol);
}

int main()
{
	freopen("date.in", "r", stdin);
	freopen("date.out", "w", stdout);

	int t;

	scanf("%d\n", &t);
	ciur();
	for (int i = 1; i <= t; ++i)
	{
		citire();
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
