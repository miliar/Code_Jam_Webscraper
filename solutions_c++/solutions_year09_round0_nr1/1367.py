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

#define N 20
#define M 6000

int n, m, l;
string A[M];
char S[N * N];

int cnt(int l, int r, int i, int j)
{
	if(r <= l) return 0;
	if(i == n) return r - l;
	int b = 0, k;
	if(S[j] == '(') b = 1, ++j;
	for(k = j; S[k] != ')' && b >= 0; ++k)
	{
		if(b == 0) b = -1;
	}
	if(S[k] == ')') ++k;
	else b = 0;

	int res = 0;
	for(; S[j] != ')' && b >= 0; ++j)
	{
		int ll, rr;
		for(ll = l; ll < r && A[ll][i] < S[j]; ++ll);
		for(rr = r; rr > l && A[rr - 1][i] > S[j]; --rr);
		res += cnt(ll, rr, i + 1, k);
		if(b == 0) b = -1;
	}

	return res;
}

int main()
{
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);

	int i, j, k, d;
	char c;
	int a;
	
#if 0
	int T, iT;
	in(d, T);
	rep(iT, 1, T + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		in(d, m); in(d, l);
		rep(i, 0, m) cin >> A[i];
		sort(A, A + m);

		rep(i, 0, l)
		{
			in(s, S);
			printf("Case #%d: %d\n", i + 1, cnt(0, m, 0, 0));
		}
	}

	return 0;
}
