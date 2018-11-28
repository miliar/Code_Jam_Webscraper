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

const int h = 111;

struct P
{
	double x,y;
	P(double x=0, double y=0) : x(x), y(y) {}
	void inp () { scanf("%lf%lf", &x, &y); }
} a[h],b[h];

int w, l,u, g;

double S (const P &a, const P &b)
{
	return (b.x-a.x) * (a.y + b.y) / 2.0;
}

double sx (double m)
{
	double t = 0;
	REP(i, l-1)
	{
		if(a[i+1].x <= m) t -= S(a[i], a[i+1]);
		else if(a[i].x < m)
			t -= (m-a[i].x) * ((a[i].y + (a[i+1].y-a[i].y)*(m-a[i].x)/(a[i+1].x-a[i].x)) + a[i].y) / 2.0;
	}
	REP(i, u-1)
	{
		if(b[i+1].x <= m) t += S(b[i], b[i+1]);
		else if(b[i].x < m)
			t += (m-b[i].x) * ((b[i].y + (b[i+1].y-b[i].y)*(m-b[i].x)/(b[i+1].x-b[i].x)) + b[i].y) / 2.0;
	}
	return t;
}

int main()
{
	freopen("a-large.in", "r", stdin); //-small-attempt0
	freopen("a-large.out", "w", stdout); //-large
	int ntest, itest=1;
for(scanf("%d", &ntest); itest<=ntest; ++itest)
{
	scanf("%d%d%d%d", &w, &l, &u, &g);
	REP(i, l) a[i].inp();
	REP(i, u) b[i].inp();
	double sp = 0;
	REP(i, l-1) sp -= S(a[i], a[i+1]);
	REP(i, u-1) sp += S(b[i], b[i+1]);
	sp /= g;
	//printf("%lf\n", sp);
	printf("Case #%d:\n", itest);
	REP(c, g-1)
	{
		double o = sp * (c+1);
		//printf("%lf\n", o);
		double L=0, R=w, m;
		REP(it, 100)
		{
			m = (L+R) / 2;
			if(sx(m) < o) L = m;
			else R = m;
		}
		printf("%.9lf\n", L);
	}
}
	return 0;
}
