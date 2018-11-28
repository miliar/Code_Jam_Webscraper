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

#define inf 1000000000
#define eps 1e-9

#define N 210
#define M 1111

int n, m;
pair<int, int> A[N];

bool can(double x)
{
	double a = -(double)inf * inf;
	int i;
	rep(i, 0, n)
	{
		a = max(a, A[i].first - x);
		a += (A[i].second - 1) * m;
		if(a - A[i].first > x) return 0;
		a += m;
	}
	return 1;
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
#if 1
	int tss, ts;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		in(d, n); in(d, m);
		rep(i, 0, n) in(d, A[i].first), in(d, A[i].second);
		sort(A, A + n);
		double l = 0., r = pow(10., 12.), mid;
		for(; l + eps < r;)
		{
			mid = (l + r) / 2.;
			if(can(mid)) r = mid;
			else l = mid;
		}
		double res = r;
		printf("Case #%d: %.7lf\n", ts, res);
	}

	return 0;
}
