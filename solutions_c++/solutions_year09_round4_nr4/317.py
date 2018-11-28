#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

typedef long double ld;
typedef long long ll;
const double pi = M_PI;

const int NMAX = 45;

struct Point
{
	double x, y;
};

double r[NMAX];
Point p[NMAX];
int n;

double dist(Point a, Point b)
{
	return hypot(a.x-b.x, a.y-b.y);
}

void solve(int tc)
{
	printf("Case #%d: ", tc);

	cin >> n;
	forn(i, n) cin >> p[i].x >> p[i].y >> r[i];

	double ans = 1e10;

	if (n == 1) 
	{
		printf("%.6lf\n", r[0]);
		return;
	}

	if (n == 2)
	{
		printf("%.6lf\n", max(r[0], r[1]));
		return;
	}
	
	int perm[3];
	forn(i, 3) perm[i] = i;
	do 
	{
		double d = dist(p[perm[0]], p[perm[1]]) + r[perm[0]] + r[perm[1]];
		d /= 2;
		ans = min(ans, max(d, r[perm[2]]));
	} while (next_permutation(perm, perm+3));

	printf("%.6lf\n", ans);
}


int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tc; cin >> tc;
	forn(i, tc) solve(i+1);

	return 0;
}