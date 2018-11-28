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

#define N 1111
#define M 1111

int n;
int A[N];

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("d.in", "rt", stdin);
	freopen("d.out", "wt", stdout);
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
		int res = 0;
		in(d, n);
		rep(i, 0, n) 
		{
			in(d, a);
			if(a != i + 1) ++res;
		}
		printf("Case #%d: ", ts);
		out(d, res); nl;
	}

	return 0;
}
