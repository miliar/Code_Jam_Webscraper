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

#define N 510
#define M 100003

int n;
int C[N][N];
int D[N][N];
int R[N];

int main()
{
	//freopen("in.txt", "rt", stdin);
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);

	int i, j, k, d;
	char c;
	int a;
	
	n = N;
	rep(i, 0, n) rep(j, 0, i + 1) if(j == 0 || j == i) C[i][j] = 1;
	else C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % M;

	rep(i, 2, n) rep(j, 1, i) 
	{
		if(j == 1) 
		{
			D[i][j] = 1; continue;
		}
		D[i][j] = 0;
		rep(k, 0, min(i - j - 1, j - 2) + 1) D[i][j] = (D[i][j] + (ll)D[j][j - k - 1] * C[i - j - 1][k]) % M;
	}
	rep(i, 2, n)
	{
		R[i] = 0;
		rep(j, 1, i) R[i] = (R[i] + D[i][j]) % M;
	}
	
#if 1
	int T, iT;
	in(d, T);
	rep(iT, 1, T + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		in(d, n);
		printf("Case #%d: %d\n", iT, R[n]);
	}

	return 0;
}
