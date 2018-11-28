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
using namespace std;

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

#define inf 1000000000
#define eps 1e-9

#define N 50
#define M 1000

int n;
int X[N], Y[N], R[N];

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);

	int i, j, k, d;
	char c;
	int a;
	
#if 1
	int T, iT;
	in(d, T);
	rep(iT, 1, T + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		in(d, n);
		rep(i, 0, n) in(d, X[i]), in(d, Y[i]), in(d, R[i]);
		double res = 0.;
		rep(i, 0, n) res = max(res, (double)R[i]);
		if(n == 3)
		{
			res = inf;
			rep(i, 0, n) rep(j, i + 1, n) 
			{
				rep(k, 0, n) if(i != k && j != k) break;
				res = min(res, max((R[i] + R[j] + hypot(X[i] - X[j], Y[i] - Y[j])) / 2., (double)R[k]));
			}
		}
		printf("Case #%d: %.6lf\n", iT, res);
	}

	return 0;
}
