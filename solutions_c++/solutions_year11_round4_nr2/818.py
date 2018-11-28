//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

//#define INF 1000000000

#define ll long long int
//#define INF ( ((ll)1) << 60 )


//////////////////////////////// GRAPHS ///////////////////////////////

//int di[] = {-1,0,1,0   ,   -1,1,1,-1};
//int dj[] = {0,1,0,-1   ,   1,1,-1,-1};

//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < n )   // square
//#define inr(i,j)  ( 0 <= (i) && (i) < n && 0 <= (j) && (j) < m )   // rectangular

#define N 511

int m, n, D;
int a[N][N];
int r[N][N], c[N][N];
ll p[N][N];
char s[N];

#define eps 1e-9

void precalc()
{
	int i, j;
	for (i = 0; i < n; ++i) r[i][0] = a[i][0];
	for (i = 0; i < m; ++i) c[0][i] = a[0][i];
	for (i = 0; i < n; ++i) for (j = 0; j < m; ++j)
	{
		if (i > 0) c[i][j] = c[i-1][j] + a[i][j];
		if (j > 0) r[i][j] = r[i][j-1] + a[i][j];
	}

	p[0][0] = a[0][0];
	for (i = 1; i < n; ++i) p[0][i] = p[0][i-1] + a[0][i];
	for (i = 1; i < m; ++i) p[i][0] = p[i-1][0] + a[i][0];
	for (i = 1; i < n; ++i) for (j = 0; j < m; ++j) p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1];
}

int solve()
{
	int i, j, K, x, y, r1, r2, c1, c2, rw1, rw2, cw1, cw2;

	for (K = min(n, m); K >= 3; --K)
	{
		for (x = 0; x + K < n; ++x) for (y = 0; y + K < m; ++y)
		{
			bool ok = true;

			for (r1 = x, r2 = x + K - 1; r1 < r2; r1++, r2--)
			{
				if (r1 == x)
				{
					rw1 = r[r1][y+K-2] - r[r1][y];
					rw2 = r[r2][y+K-2] - r[r2][y];
				}
				else
				{
					rw1 = r[r1][y+K-1] - (y-1 >= 0 ? r[r1][y-1] : 0);
					rw2 = r[r2][y+K-1] - (y-1 >= 0 ? r[r2][y-1] : 0);
				}

				if (rw1 != rw2) ok = false;
			}

			for (c1 = y, c2 = y + K - 1; c1 < c2; c1++, c2--)
			{
				if (c1 == y)
				{
					cw1 = c[x+K-2][c1] - c[x][c1];
					cw2 = c[x+K-2][c2] - c[x][c2];
				}
				else
				{
					cw1 = c[x+K-1][c1] - (x-1 >= 0 ? c[x-1][c1] : 0);
					cw2 = c[x+K-1][c2] - (x-1 >= 0 ? c[x-1][c2] : 0);
				}

				if (cw1 != cw2) ok = false;
			}

			if (ok) return K;
		}
	}

	return -1;
}

int stupid_solve()
{
	int i, j, K, x, y, r1, r2, c1, c2, rw1, rw2, cw1, cw2;
	double cx, cy, xx, yy, rx, ry;

	for (K = min(n, m); K >= 3; --K)
	{
		for (x = 0; x + K <= n; ++x) for (y = 0; y + K <= m; ++y)
		{
			cx = (double)(K-1) * 0.5;
			cy = (double)(K-1) * 0.5;
			rx = ry = 0.0;

			for (i = 0; i < K; ++i) for (j = 0; j < K; ++j)
			{
				if ((i == 0 || i == K-1) && (j == 0 || j == K-1)) continue;
				xx = (double)i - cx;
				yy = (double)j - cy;
				rx += xx * a[x+i][y+j];
				ry += yy * a[x+i][y+j];
			}

			if (fabs(rx) < eps && fabs(ry) < eps) return K;
		}
	}

	return -1;
}

int main () {
	int i, j, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {
		scanf("%d%d%d", &n, &m, &D);
		for (i = 0; i < n; ++i)
		{
			scanf("%s", s);
			for (j = 0; j < m; ++j) a[i][j] = D + (s[j] - '0');
		}

		int res = stupid_solve();
		if (res == -1)
		{		
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
		else
		{
			printf("Case #%d: %d\n", cas, res);
		}
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}


