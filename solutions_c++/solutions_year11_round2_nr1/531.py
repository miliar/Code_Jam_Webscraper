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

#define inf 1000000000
#define eps 1e-9

#define N 110
#define M 1111

int n;
char A[N][N];
double D[N], DD[N], DDD[N];
int S[N];

double fnd(int i)
{
	double &res = D[i];
	if(res >= 0) return res;
	res = 0;
	int j;
	rep(j, 0, n) if(A[i][j] == '1') ++res;
	res /= S[i];
	return res;
}

double fndd(int i)
{
	double &res = DD[i];
	if(res >= 0) return res;
	res = 0;
	int j;
	rep(j, 0, n) if(A[i][j] != '.') res += (fnd(j) * S[j] - (A[j][i] - '0')) / (S[j] - 1);
	res /= S[i];
	return res;
}

double fnddd(int i)
{
	double &res = DDD[i];
	if(res >= 0) return res;
	res = 0;
	int j;
	rep(j, 0, n) if(A[i][j] != '.') res += fndd(j);
	res /= S[i];
	return res;
}

int main()
{
#ifdef XDEBUG
	freopen("in.txt", "rt", stdin);
#else
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
#endif

	int i, j, k;
	char c;
	int a, d;
	
#if 1
	int tss, ts;
	in(d, tss);
	rep(ts, 1, tss + 1)
#else
	for(; in(d, n) > 0;)
#endif
	{
		in(d, n);
		rep(i, 0, n) in(s, A[i]);
		rep(i, 0, n)
		{
			S[i] = 0;
			rep(j, 0, n) if(A[i][j] != '.') ++S[i];
		}
		rep(i, 0, n) D[i] = DD[i] = DDD[i] = -1;
		printf("Case #%d:", ts); nl;
		rep(i, 0, n)
		{
			double res = 0.25 * fnd(i) + 0.5 * fndd(i) + 0.25 * fnddd(i);
			out(.7lf, res); nl;
		}
	}

	return 0;
}
