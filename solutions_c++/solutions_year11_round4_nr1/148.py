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

#define N 1012
#define M 1012

#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000009
#endif

int n, m;
pair<int, int> A[N];

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

	int x, s, r;
	double t;
	
	int ts;	
#if 1
	int tss;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
		in(d, x); in(d, s); in(d, r); in(lf, t);
		in(d, n);
		A[0] = mp(0, x);
		rep(i, 0, n)
		{
			int a, b, v;
			in(d, a); in(d, b); in(d, v);
			A[i + 1] = mp(v, b - a);
			A[0].second -= b - a;
		}
		++n;
		double res = 0.;
		sort(A, A + n);
		double a;
		rep(i, 0, n) if((a = (double)A[i].second / (A[i].first + r)) <= t)
		{
			res += a; t -= a;
		}
		else if(t > eps)
		{
			res += t + (A[i].second - (A[i].first + r) * t) / (A[i].first + s);
			t = 0.;
		}
		else res += (double)A[i].second / (A[i].first + s);

		printf("Case #%d: ", ts);
		out(.7lf, res); nl;
	}

	return 0;
}
