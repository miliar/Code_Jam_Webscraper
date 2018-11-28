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

#define Nmax 6015
#define INF 0x3f3f3f3f

const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

int n;
int x[Nmax * Nmax], y[Nmax * Nmax];
int jos[Nmax], sus[Nmax];
int stj[Nmax], drj[Nmax];
int sts[Nmax], drs[Nmax];
char sir[64];

void citire()
{
	int cnt, rep, dir = 0, l;

	n = 1;
	x[1] = y[1] = 3002;
	scanf("%d", &cnt);
	for (int i = 1; i <= cnt; ++i)
	{
		scanf("%s %d", sir + 1, &rep);
		l = strlen(sir + 1);
		for (int j = 1; j <= rep; ++j)
			for (int k = 1; k <= l; ++k)
			{
				if (sir[k] == 'F')
				{
					++n;
					x[n] = x[n - 1] + dx[dir];
					y[n] = y[n - 1] + dy[dir];
				}

				if (sir[k] == 'R') ++dir;
				if (sir[k] == 'L') --dir;

				if (dir == 4) dir = 0;
				if (dir == -1) dir = 3;
			}
	}
}

void solve()
{
	int i, arie = 0;

	for (i = 1; i < n; ++i)
		arie += (x[i] * y[i + 1] - x[i + 1] * y[i]);
	if (arie > 0) arie *= -1;
	arie /= 2;

    for (i = 0; i < Nmax; ++i)
	{
		jos[i] = INF;
		sus[i] = 0;
	}

    for (i = 1; i <= n; ++i)
	{
		sus[y[i]] = max(sus[y[i]], x[i]);
		jos[y[i]] = min(jos[y[i]], x[i]);
	}

	sts[0] = 0;
	stj[0] = INF;

	for (i = 1; i < Nmax; ++i)
	{
		sts[i] = max(sts[i - 1], sus[i]);
		stj[i] = min(stj[i - 1], jos[i]);
	}

	drs[Nmax - 1] = 0;
	drj[Nmax - 1] = INF;
	for (i = Nmax - 2; i >= 0; --i)
	{
		drs[i] = max(drs[i + 1], sus[i]);
		drj[i] = min(drj[i + 1], jos[i]);
	}

	for (i = 0; i < Nmax - 1; ++i)
		arie += max(min(sts[i], drs[i + 1]) - max(stj[i], drj[i + 1]), 0);

	printf("%d\n", arie);
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
