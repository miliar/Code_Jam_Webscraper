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
#define M 1000

int DX[4] = {-1, 0, 0, 1};
int DY[4] = {0, -1, 1, 0};

int n, m, l;
int A[N][N], B[N][N];
char R[N];

struct point
{
	int i, j;
	bool operator<(const point &p) const
	{
		return A[i][j] < A[p.i][p.j];
	}
} p;

point P[N * N];

int main()
{
	freopen("B.in", "rt", stdin);
	freopen("B.out", "wt", stdout);

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
		rep(i, 0, n + 2) A[i][0] = A[i][m + 1] = inf;
		rep(j, 0, m + 2) A[0][j] = A[n + 1][j] = inf;
		l = 0;
		rep(i, 1, n + 1) rep(j, 1, m + 1) in(d, A[i][j]), p.i = i, p.j = j, P[l++] = p;

		sort(P, P + l);

		int r = 0;
		rep(i, 0, l)
		{
			int ii = P[i].i, jj = P[i].j;
			rep(k, 0, 4) if(A[P[i].i + DX[k]][P[i].j + DY[k]] < A[ii][jj]) ii = P[i].i + DX[k], jj = P[i].j + DY[k];
			if(ii == P[i].i && jj == P[i].j) B[ii][jj] = r++;
			else B[P[i].i][P[i].j] = B[ii][jj];
		}

		assert(r <= 26);

		rep(i, 0, r) R[i] = 0;

		printf("Case #%d:\n", iT);
		char res = 'a';
		rep(i, 1, n + 1)
		{
			rep(j, 1, m + 1) 
			{
				if(R[B[i][j]] == 0) R[B[i][j]] = res++;
				outf(c, R[B[i][j]]);
			}
			nl;
		}
	}

	return 0;
}
