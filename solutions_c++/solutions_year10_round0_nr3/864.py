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

#define N 1010
#define M 1000

int n, m, r;
int A[N];
bool B[N];
int P[N], S[N];

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);

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
		in(d, r); in(d, m); in(d, n);
		rep(i, 0, n) B[i] = 0, in(d, A[i]);
		B[0] = 0;
		for(i = 0; !B[i]; i = j)
		{
			B[i] = 1;
			S[i] = 0;
			for(j = i; S[i] + A[j] <= m;)
			{
				S[i] += A[j];
				j = (j + 1) % n;
				if(j == i) break;
			}
			P[i] = j;
		}
		int o = j;
		ll res = 0;
		for(i = 0; r > 0 && i != o; i = P[i]) res += S[i], --r;
		if(r > 0)
		{
			int l = 1;
			ll s = S[i];
			for(i = P[i]; i != o; i = P[i]) ++l, s += S[i];
			res += r / l * s;
			r %= l;
		}
		if(r > 0)
		{
			for(; r > 0; i = P[i]) res += S[i], --r;
		}
		printf("Case #%d: %lld\n", iT, res);
	}

	return 0;
}
