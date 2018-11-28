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

#define N 110
#define M 30

int n, m, l;
int A[N][M], C[2 * N][2 * N];
bool B[2 * N];

bool dfs(int i)
{
	B[i] = 1;
	if(i == l - 1) return 1;
	int j;
	rep(j, 0, l) if(!B[j] && C[i][j])
	{
		--C[i][j];
		++C[j][i];
		if(dfs(j)) return 1;
		++C[i][j];
		--C[j][i];
	}
	return 0;
}

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
		in(d, n); in(d, m);
		rep(i, 0, n) rep(j, 0, m) in(d, A[i][j]);
		l = 2 * n + 2;
		rep(i, 0, l) rep(j, 0, l) C[i][j] = 0;
		rep(i, 1, n + 1) C[0][i] = 1;
		rep(i, n + 1, 2 * n + 1) C[i][2 * n + 1] = 1;
		rep(i, 0, n) rep(j, 0, n)
		{
			rep(k, 0, m) if(A[j][k] <= A[i][k]) break;
			if(k == m) C[1 + i][n + 1 + j] = 1;
		}
		int res = 0;
		for(;;)
		{
			rep(i, 0, l) B[i] = 0;
			if(dfs(0)) ++res;
			else break;
		}
		printf("Case #%d: %d\n", iT, n - res);
	}

	return 0;
}
