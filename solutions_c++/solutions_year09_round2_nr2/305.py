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

#define N 30
#define M 1000

int n;
int A[N], C[N];
char S[N];

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
		in(s, S);
		reps(i, S) A[i + 1] = S[i] - '0';
		A[0] = 0;
		int mx = -1;
		rep(j, 0, 10) C[j] = 0;
		for(; A[i] >= mx; --i) ++C[A[i]], mx = max(mx, A[i]);

		printf("Case #%d: ", iT);
		rep(j, 1, i) out(d, A[j]);
		++C[A[i]];
		for(i = A[i] + 1; C[i] == 0; ++i);
		out(d, i);
		--C[i];
		rep(i, 0, 10) rep(j, 0, C[i]) out(d, i);
		nl;
	}

	return 0;
}
