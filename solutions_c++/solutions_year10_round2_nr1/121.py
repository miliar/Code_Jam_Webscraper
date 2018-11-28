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

#define N 1000000
#define M 1000

int n, m;
string A[N];

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

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
		in(d, n); in(d, m);
		rep(i, 0, n) cin >> A[i];
		int res = 0;
		rep(i, 0, m)
		{
			string s;
			cin >> s;
			int mx = 0;
			rep(j, 0, n) 
			{
				reps(k, A[j]) if(A[j][k] != s[k]) break;
				if(A[j][k] == 0 && (s[k] == 0 || s[k] == '/')) mx = max(mx, k);
			}
			for(j = mx; s[j] == '/';)
			{
				for(++j; s[j] != '/' && s[j] != 0; ++j);
				c = s[j];
				s[j] = 0;
				A[n++] = s.data();
				s[j] = c;
				++res;
			}
		}
		printf("Case #%d: %d\n", iT, res);
	}

	return 0;
}
