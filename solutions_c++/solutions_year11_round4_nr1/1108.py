#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define foreach(x, i) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i ++)
#define pb push_back
#define mp make_pair


using namespace std;

const int N = 100000;
struct Stuff
{
	double s, v;
	bool operator < (const Stuff &t) const
	{ return v < t.v; }
	Stuff(){}
	Stuff(double _s, double _v) : s(_s), v(_v){}
} a[N * 3];

struct Tmp { double l, r, w; 
	bool operator < (const Tmp &t) const
	{ return l < t.l ; }
} b[N];
double solve()
{
	double X, S, R, t, dt;
	int N;
	scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &N);
	dt = R - S;
	For (i, N) scanf("%lf%lf%lf", &b[i].l, &b[i].r, &b[i].w);
	sort(b, b + N);
	double prev = 0;
	int m = 0;
	For (i, N)
	{
		double len = b[i].r - b[i].l;
		double v = b[i].w + S;
		a[m ++] = Stuff(len, v);
		if (b[i].l > prev)
			a[m ++] = Stuff(b[i].l - prev, S);
		prev = b[i].r;
	}
	if (X > prev) a[m ++] = Stuff(X - prev, S);
	sort(a, a + m);
	double ans = 0;
	for (int i = 0; i < m; i ++)
	{
		double v = a[i].v + dt;
		double consume = a[i].s / (a[i].v + dt);
		if (consume <= t)
		{
			ans += consume;
			t -= consume;
		} else
		{
			ans += t + (a[i].s - v * t) / a[i].v;
			t = 0;
		}
	}
	return ans;
}

int main()
{
	int t; scanf("%d", &t);
	For (i, t) printf("Case #%d: %.8lf\n", i + 1, solve());
	return 0;
}

