#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int MaxN = 3;

double x[MaxN], y[MaxN], r[MaxN];

double cover(int i, int j)
{
	double d = hypot(x[i]-x[j], y[i]-y[j]);
	d += r[i] + r[j];
	return d/2;
}

double solve()
{
	int N;
	scanf("%d", &N);
	REP(i, N)
		scanf("%lf %lf %lf\n", &x[i], &y[i], &r[i]);

	if (N == 1)
		return r[0];

	if (N == 2)
		return max(r[0], r[1]);

	double res = 1e+100;
	res = min(res, max(r[0], cover(1, 2)));
	res = min(res, max(r[1], cover(0, 2)));
	res = min(res, max(r[2], cover(0, 1)));
	return res;
}

int main()
{
	//freopen("input.txt", "r", stdin);

	int n_test;
	scanf("%d\n", &n_test);
	REP(i_test, n_test) {
		printf("Case #%d: %.7lf\n", i_test+1, solve());
	}

	return 0;
}
