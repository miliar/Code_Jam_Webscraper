#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>
#include <assert.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
#define LL long long
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
#define fo(i, n) for (int i = 0; i < (n); i++)
#define foz(i, a) for (int i = 0; i < (a).size(); i++)

void init()
{

}

#define maxn 1005

int n, w, l;
pair<int, int> r[maxn];
int rr[maxn];
bool taken[maxn];
int x[maxn], y[maxn];

void goy(int x0, int x1, int y0, int y1)
{
	x0 = max(0, x0);
	x1 = min(w, x1);
	y0 = max(0, y0);
	y1 = min(l, y1);
	if (x0 >= x1) return;
	if (y0 >= y1) return;
	for (int i = 0; i < n; i++) if (!taken[i])
	{
		int q = 2 * r[i].first;
		if (x1 - x0 >= q && y1 - y0 >= q)
		{
			taken[i] = true;
			x[r[i].second] = x0 + q / 2;
			y[r[i].second] = y0 + q / 2;
			goy(x0, x1, y0 + q, y1);
			goy(x0 + q, x1, y0, y0 + q);
			return;
		}
	}
}

inline double sqr(double x) { return x*x; }

void solvecase()
{
	scanf("%d%d%d", &n, &w, &l);
	for (int i = 0; i < n; i++) { scanf("%d", &r[i].first); r[i].second = i; taken[i] = false; rr[i] = r[i].first; x[i] = -1; y[i] = -1; }
	bool sw = false;
	if (w < l)
	{
		swap(w, l);
		sw = true;
	}
	sort(r, r+n); reverse(r, r+n);
	// first row
	//x[r[0].second] = 0;
	//y[r[0].second] = 0;
	//taken[0] = true;
	int curx = -r[0].first;
	int i;
	int cury = 0;
	for (i = 0; i < n && curx + r[i].first <= w; i++)
	{
		if (taken[i]) continue;
		x[r[i].second] = curx + r[i].first;
		y[r[i].second] = cury;
		taken[i] = true;
		goy(curx, curx + 2 * r[i].first, cury + r[i].first, l);
		curx += 2 * r[i].first;		
	}
	assert(i == n);
	for (int i = 0; i < n; i++)
	{
		if (sw) swap(x[i], y[i]);
		printf("%d %d ", x[i], y[i]);
	}
	if (sw) swap(l, w);
	for (int i = 0; i < n; i++)
	{
		assert(x[i] >= 0 && x[i] <= w && y[i] >= 0 && y[i] <= l);
		for (int j = i + 1; j < n; j++)
		{
			double dist = sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]));
			assert(dist > rr[i] + rr[j] - 1e-9);
		}
	}
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define problem_letter "B"
//#define fname "test"
//#define fname problem_letter "-small-attempt0"
//#define fname problem_letter "-small-attempt1"
//#define fname problem_letter "-small-attempt2"
#define fname problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}