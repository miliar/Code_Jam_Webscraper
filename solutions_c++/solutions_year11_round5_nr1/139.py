#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
using namespace std;
#pragma comment(linker, "/STACK:255000000")

typedef long long ll;

#define rep(i, a, b) for(i = (a); i < (b); ++i)
#define repb(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define repd(i, a, b, d) for(i = (a); i < (b); i += (d))
#define repbd(i, a, b, d) for(i = (a) - 1; i >= (b); i -= (d))
#define reps(i, s) for(i = 0; (s)[i]; ++i)
#define repl(i, l) for(i = l.begin(); i != l.end(); ++i)

#define in(f, a) scanf("%"#f, &(a))

bool firstout = 1;

#define out(f, a) printf("%"#f, (a))
#define outf(f, a) printf((firstout) ? "%"#f : " %"#f, (a)), firstout = 0
#define nl printf("\n"), firstout = 1

#define all(x) (x).begin(),(x).end()
#define sqr(x) ((x) * (x))
#define mp make_pair

#define inf 1012345678
#define eps 1e-9

#define N 102

#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000009
#endif

typedef pair<double, double> point;
#define x first
#define y second

int n, m, l, w;
point A[N], B[N];
double s;

void rec(point a, point b, int i, int j, int l, double t)
{
	double x = min(A[i].x, B[j].x);
	double x0 = a.x;
	double dy1 = (A[i].y - a.y) / (A[i].x - a.x);
	double dy2 = (B[j].y - b.y) / (B[j].x - b.x);
	double tt = (x - x0) * (b.y - a.y + (x - x0) * (dy2 - dy1) / 2.);
	if(tt + eps < t)
	{
		t -= tt;
		a = mp(x, a.y + dy1 * (x - x0));
		b = mp(x, b.y + dy2 * (x - x0));
		if(fabs(x - A[i].x) < eps) ++i;
		if(fabs(x - B[j].x) < eps) ++j;
		rec(a, b, i, j, l, t);
		return;
	}
	double aa = b.y - a.y, bb = (dy2 - dy1) / 2.;
	if(abs(bb) < eps) x = x0 + t / aa;
	else x = x0 + (sqrt(sqr(aa) + 4 * bb * t) - aa) / 2 / bb;
	tt = (x - x0) * (b.y - a.y + (x - x0) * (dy2 - dy1) / 2.);
	assert(fabs(t - tt) < eps);
	out(.7lf, x); nl;
	t = s;
	--l;
	if(l == 0) return;
	a = mp(x, a.y + dy1 * (x - x0));
	b = mp(x, b.y + dy2 * (x - x0));
	if(fabs(x - A[i].x) < eps) ++i;
	if(fabs(x - B[j].x) < eps) ++j;
	rec(a, b, i, j, l, t);
	return;
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
	int ts;	
#if 1
	int tss;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
		in(d, w); in(d, n); in(d, m); in(d, l);
		rep(i, 0, n) in(lf, A[i].x), in(lf, A[i].y);
		rep(i, 0, m) in(lf, B[i].x), in(lf, B[i].y);
		s = 0.;
		rep(i, 0, n - 1) s -= (A[i].y + A[i + 1].y) / 2. * (A[i + 1].x - A[i].x);
		rep(i, 0, m - 1) s += (B[i].y + B[i + 1].y) / 2. * (B[i + 1].x - B[i].x);
		s /= l;
		printf("Case #%d:\n", ts);
		rec(A[0], B[0], 1, 1, l - 1, s);
	}

	return 0;
}
