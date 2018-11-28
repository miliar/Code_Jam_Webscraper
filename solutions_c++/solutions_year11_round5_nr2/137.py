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
int A[N];

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("b.in", "rt", stdin);
	freopen("b.out", "wt", stdout);
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
		in(d, n);
		rep(i, 0, n) in(d, A[i]);

		int res = 0;

		printf("Case #%d: ", ts);
		if(n == 0) out(d, res), nl;
		else
		{
			res = inf;
			sort(A, A + n);
			multiset<int> s, ss;
			s.clear(); ss.clear();
			a = -inf;
			rep(i, 0, n)
			{
				if(A[i] != a + 1)
				{
					if(!s.empty()) res = min(res, *s.begin());
					s = ss;
					ss.clear();
					++a;
					if(A[i] != a + 1)
					{
						if(!s.empty()) res = min(res, *s.begin());
						s.clear();
						a = A[i] - 1;
					}
				}
				if(s.empty()) ss.insert(1);
				else
				{
					ss.insert(*s.begin() + 1);
					s.erase(s.begin());
				}
			}
			if(!s.empty()) res = min(res, *s.begin());
			if(!ss.empty()) res = min(res, *ss.begin());
			out(d, res); nl;
		}
	}

	return 0;
}
