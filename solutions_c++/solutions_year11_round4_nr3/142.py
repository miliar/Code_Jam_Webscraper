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

#define N 1012345
#define M 1012

#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000009
#endif

int n, m, np;
int A[N];
bool PP[N];
int P[N];

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;

	rep(i, 0, N) PP[i] = 1;
	PP[0] = PP[1] = 0;
	for(i = 2; i * i < N; ++i) if(PP[i]) for(j = i * i; j < N; j += i) PP[j] = 0;
	np = 0;
	rep(i, 2, N) if(PP[i]) P[np++] = i;
	
	int ts;	
#if 1
	int tss;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(ts = 1; in(d, n) > 0; ++ts)
#endif
	{
		ll a;
		in(lld, a);
		int res = 0;

		printf("Case #%d: ", ts);
		if(a == 1) out(d, 0), nl;
		else
		{
			res = 1;
			rep(i, 0, np) if(P[i] < a)
			{
				ll d = P[i];
				for(; d <= a; d *= P[i]) ++res;
				--res;				
			}
			out(d, res); nl;
		}
	}

	return 0;
}
