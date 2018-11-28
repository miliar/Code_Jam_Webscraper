#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <complex>
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

#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()

#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<string> VS;
struct SO
{
	bool operator()(VI x, VI y)
	{
		while (SZ(x))
		{
			int xI = max_element(ALL(x))-x.begin();
			int yI = max_element(ALL(y))-y.begin();
			if (x[xI] != y[yI])
				return x[xI] > y[yI];
			if (xI != yI)
				return xI < yI;
			x.erase(x.begin()+xI);
			y.erase(y.begin()+yI);
		}
		return false;
	}
};

bool operator<(const VI &x, const VI &y)
{
	return true;
}

bool good(const VI &v1, const VI &v2)
{
	REP(i,SZ(v1))
		if (v1[i] <= v2[i])
			return false;
	return true;
}

double x2(double x)
{
	return x*x;
}
double dist(const VI &x, const VI &y)
{
	return sqrt(x2(y[0]-x[0])+x2(y[1]-x[1]));
}
double dist2(const VI &x)
{
	return x[2];
}
double dist2(const VI &x, const VI &y)
{
	return (dist(x, y)+x[2]+y[2])/2.0;
}
int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w+", stdout);	int T;
	cin >> T;
	REP(it,T)
	{
		int n, k;
		cin >> n;
		k = 3;
		VVI v(n, VI(k));
		REP(i,n)
			REP(j,k)
				cin >> v[i][j];
		double res = 0;
		if (n == 1)
			res = v[0][2];
		if (n == 2)
			res = max(v[0][2], v[1][2]);
		if (n == 3)
		{
			res = max(dist2(v[0], v[1]),dist2(v[2]));
			res = min(res, max(dist2(v[0], v[2]),dist2(v[1])));
			res = min(res, max(dist2(v[1], v[2]),dist2(v[0])));
		}
		printf("Case #%d: %.7lf\n", it+1, res);
	}
}
