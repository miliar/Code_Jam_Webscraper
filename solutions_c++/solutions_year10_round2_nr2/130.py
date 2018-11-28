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

#define N 1000
#define M 1000

int n, m;
int X[N], V[N];
bool B[N];

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);

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
		int b, t;
		in(d, n); in(d, m); in(d, b); in(d, t);
		rep(i, 0, n) in(d, X[i]);
		rep(i, 0, n) in(d, V[i]);
		rep(i, 0, n) B[i] = (b - X[i] - 1) / V[i] < t;
		int res = 0;
		for(i = n - 1, j = 0, k = 0; i >= 0 && j < m; --i) if(B[i]) res += k, ++j;
		else ++k;
		printf("Case #%d: ", iT);
		if(j == m) out(d, res);
		else out(s, "IMPOSSIBLE");
		nl;
	}

	return 0;
}
