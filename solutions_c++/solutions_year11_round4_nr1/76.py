#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for(int i=(a), _b=(b); i<_b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FORD(i, a, b) for(int i=(a), _b=(b); i>=_b; --i)
#define CL(a, v) memset(a, v, sizeof a)
#define INF 1000000000
#define INF_LL 1000000000000000000LL
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int h = 1111;
const double eps = 1e-9;

int x, s, r, n;
double t, d;
int b[h],e[h], w[h];
int p[h];

bool comp (int a, int b) { return w[a] < w[b]; }

int main()
{
	freopen("a-large.in", "r", stdin); //-small-attempt0
	freopen("a-large.out", "w", stdout); //-large
	int ntest, itest=1;
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	scanf("%d%d%d%lf%d", &x, &s, &r, &t, &n);
	REP(i, n) scanf("%d%d%d", b+i, e+i, w+i), p[i]=i;
	REP(i, n) x -= (e[i]-b[i]);
	b[n] = 0;
	e[n] = x;
	w[n] = 0;
	p[n] = n;
	sort(p, p+n+1, comp);
	double ans = 0;
	REP(i, n+1)
	{
		int u = p[i];
		s += w[u];
		r += w[u];
		//printf("%d %d %d, %lf\n", b[u], e[u], w[u], t);
		if(t >= double(e[u]-b[u]) / r)
		{
			d = double(e[u]-b[u]) / r;
			t -= d;
			ans += d;
		}
		else
		{
			ans += t;
			ans += ((e[u]-b[u]) - r*t) / s;
			t = 0;
		}
		s -= w[u];
		r -= w[u];
	}
	printf("Case #%d: %.9lf\n", itest, ans);
}
	return 0;
}
