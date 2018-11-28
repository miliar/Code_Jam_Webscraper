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
#define M 10000
#define L 510

int n, m;
char S[N] = "welcome to code jam", SS[L];
int D[N][L];

int fnd(int i, int j)
{
	int &res = D[i][j];
	if(res < 0)
	{
		if(i == n)
		{
			res = 1;
			return res;
		}
		res = 0;
		if(j == m) return res;
		int k;
		rep(k, j, m) if(S[i] == SS[k]) res = (res + fnd(i + 1, k + 1)) % M;
	}
	return res;
}

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("C.in", "rt", stdin);
	freopen("C.out", "wt", stdout);

	int i, j, k, d;
	char c;
	int a;
	
#if 1
	int T, iT;
	in(d, T);
	gets(SS);
	rep(iT, 1, T + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		gets(SS);
		n = N - 1;
		m = strlen(SS);
		rep(i, 0, n + 1) rep(j, 0, m + 1) D[i][j] = -1;
		printf("Case #%d: %04d\n", iT, fnd(0, 0));
	}

	return 0;
}
