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

#define Nmax 1024
const double eps = 1e-7;
const int dx[8] = {1, -1, 0, 0, 0, 0};
const int dy[8] = {0, 0, 1, -1, 0, 0};
const int dz[8] = {0, 0, 0, 0, 1, -1};

int n;
double sol;
int x[Nmax], y[Nmax], z[Nmax], p[Nmax];

void citire()
{
	int i;
	
	scanf("%d\n", &n);
    for (i = 1; i <= n; ++i)
		scanf("%d %d %d %d\n", &x[i], &y[i], &z[i], &p[i]);
}

inline double calc(double x0, double y0, double z0)
{
	int i;
	double ret = 0;

	for (i = 1; i <= n; ++i)
		ret = max(ret, ((double)fabs(x[i] - x0) + fabs(y[i] - y0) + fabs(z[i] - z0)) / p[i]);

	sol = min(sol, ret);

	return ret;
}

void cauta(double x0, double y0, double z0, double dif)
{
	int d, dir = -1;
	double best = calc(x0, y0, z0);

    if (dif < eps) return;

	for (d = 0; d < 8; ++d)
		if (calc(x0 + dx[d] * dif, y0 + dy[d] * dif, z0 + dz[d] * dif) < best)
		{
 			best = calc(x0 + dx[d] * dif, y0 + dy[d] * dif, z0 + dz[d] * dif);
			dir = d;
		} 

	if (dir != -1)
 		cauta(x0 + dx[dir] * dif, y0 + dy[dir] * dif, z0 + dz[dir] * dif, dif);
	else
		cauta(x0, y0, z0, dif / 2);
}

void solve()
{
	sol = calc(x[1], y[1], z[1]);
	cauta(x[1], y[1], z[1], Nmax * Nmax);
	printf("%.6lf\n", sol);
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
