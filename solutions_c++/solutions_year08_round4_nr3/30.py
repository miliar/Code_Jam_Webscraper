#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long ll;

#define NMAX 1005
#define EPS 1e-7
#define INF 1e+8

int n;
double x[NMAX], y[NMAX], z[NMAX], p[NMAX];

bool can(double t)
{
	double u1 = INF, u2 = INF, u3 = INF, u4 = INF;
	double d1 = -INF, d2 = -INF, d3 = -INF, d4 = -INF;

	forn(i, n)
	{
		u1 = min(u1, x[i] + y[i] + z[i] + p[i] * t);
		d1 = max(d1, x[i] + y[i] + z[i] - p[i] * t);

		u2 = min(u2, x[i] + y[i] - z[i] + p[i] * t);
		d2 = max(d2, x[i] + y[i] - z[i] - p[i] * t);

		u3 = min(u3, -x[i] + y[i] + z[i] + p[i] * t);
		d3 = max(d3, -x[i] + y[i] + z[i] - p[i] * t);

		u4 = min(u4, x[i] - y[i] + z[i] + p[i] * t);
		d4 = max(d4, x[i] - y[i] + z[i] - p[i] * t);
	}

	if (u1 > d1 - EPS && u2 > d2 - EPS && u3 > d3 - EPS && u4 > d4 - EPS) return true;
	return false;
}
void solve(int test)
{
	scanf("%d", &n);	
	forn(i, n)
	{
		scanf("%lf %lf %lf %lf", &x[i], &y[i], &z[i], &p[i]);
	}

	double L = 0.0, R = 1e+8;

	forn(it, 100)
	{
		double mid = (L + R) / 2;
		if (can(mid))
		{
			R = mid;
		}
		else
		{
			L = mid;
		}
	}

	printf("Case #%d: %.6lf\n", test, L);
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}

	return 0;
}
