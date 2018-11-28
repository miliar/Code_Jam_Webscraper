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

#define N 512
#define M 1012

#ifdef XDEBUG
#define mod 23
#else
#define mod 1000000009
#endif

int n, m;
int A[N][N];
int HX[N][N], HM[N][N], VX[N][N], VM[N][N];

void add(ll &x, ll &y, ll vx, ll vy, ll m, ll cx, ll cy)
{
	x += vx - cx * m;
	y += vy - cy * m;
}

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
		cerr << ts << endl;
		in(d, n); in(d, m); in(d, a);
		rep(i, 1, n + 1) rep(j, 1, m + 1) in(1d, A[i][j]);
		rep(i, 1, n + 1)
		{
			HX[i][0] = HM[i][0] = 0;
			rep(j, 1, m + 1)
			{
				HM[i][j] = HM[i][j - 1] + A[i][j];
				HX[i][j] = HX[i][j - 1] + 2 * j * A[i][j];
			}
		}
		rep(j, 1, m + 1)
		{
			VX[0][j] = VM[0][j] = 0;
			rep(i, 1, n + 1)
			{
				VM[i][j] = VM[i - 1][j] + A[i][j];
				VX[i][j] = VX[i - 1][j] + 2 * i * A[i][j];
			}
		}
		int res = 0;

		rep(i, 1, n + 1) rep(j, 1, m + 1)
		{
			ll x, y;
			x = y = 0;
			int i0 = 2 * i, j0 = 2 * j;
			for(k = 1; i - k > 0 && j - k > 0 && i + k <= n && j + k <= m; ++k)
			{
				int lk = -k, rk = k;			
				int ms, i1, j1, i2, j2;
				i1 = i + lk; j1 = j + rk - 1;
				i2 = i + lk; j2 = j + lk;
				ms = HM[i1][j1] - HM[i2][j2];
				add(x, y, 2 * i1 * ms, HX[i1][j1] - HX[i2][j2], ms, i0, j0);
				i1 = i + rk; j1 = j + rk - 1;
				i2 = i + rk; j2 = j + lk;
				ms = HM[i1][j1] - HM[i2][j2];
				add(x, y, 2 * i1 * ms, HX[i1][j1] - HX[i2][j2], ms, i0, j0);
				i1 = i + rk - 1; j1 = j + lk;
				i2 = i + lk; j2 = j + lk;
				ms = VM[i1][j1] - VM[i2][j2];
				add(x, y, VX[i1][j1] - VX[i2][j2], 2 * j1 * ms, ms, i0, j0);
				i1 = i + rk - 1; j1 = j + rk;
				i2 = i + lk; j2 = j + rk;
				ms = VM[i1][j1] - VM[i2][j2];
				add(x, y, VX[i1][j1] - VX[i2][j2], 2 * j1 * ms, ms, i0, j0);
				if(x == 0 && y == 0) res = max(res, 2 * k + 1);

				int ii = i + lk, jj = j + lk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
				ii = i + lk, jj = j + rk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
				ii = i + rk, jj = j + lk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
				ii = i + rk, jj = j + rk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
			}
		}
		rep(i, 1, n) rep(j, 1, n)
		{
			ll x, y;
			x = y = 0;
			int i0 = 2 * i + 1, j0 = 2 * j + 1;			
			for(k = 1; i - k + 1 > 0 && j - k + 1 > 0 && i + k <= n && j + k <= m; ++k)
			{
				int lk = -k + 1, rk = k;			
				int ms, i1, j1, i2, j2;
				i1 = i + lk; j1 = j + rk - 1;
				i2 = i + lk; j2 = j + lk;
				ms = HM[i1][j1] - HM[i2][j2];
				add(x, y, 2 * i1 * ms, HX[i1][j1] - HX[i2][j2], ms, i0, j0);
				i1 = i + rk; j1 = j + rk - 1;
				i2 = i + rk; j2 = j + lk;
				ms = HM[i1][j1] - HM[i2][j2];
				add(x, y, 2 * i1 * ms, HX[i1][j1] - HX[i2][j2], ms, i0, j0);
				i1 = i + rk - 1; j1 = j + lk;
				i2 = i + lk; j2 = j + lk;
				ms = VM[i1][j1] - VM[i2][j2];
				add(x, y, VX[i1][j1] - VX[i2][j2], 2 * j1 * ms, ms, i0, j0);
				i1 = i + rk - 1; j1 = j + rk;
				i2 = i + lk; j2 = j + rk;
				ms = VM[i1][j1] - VM[i2][j2];
				add(x, y, VX[i1][j1] - VX[i2][j2], 2 * j1 * ms, ms, i0, j0);
				if(x == 0 && y == 0) res = max(res, 2 * k);

				int ii = i + lk, jj = j + lk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
				ii = i + lk, jj = j + rk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
				ii = i + rk, jj = j + lk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
				ii = i + rk, jj = j + rk;
				add(x, y, 2 * ii * A[ii][jj], 2 * jj * A[ii][jj], A[ii][jj], i0, j0);
			}
		}

		printf("Case #%d: ", ts);
		if(res <= 2) out(s, "IMPOSSIBLE");
		else out(d, res); 
		nl;
	}

	return 0;
}
