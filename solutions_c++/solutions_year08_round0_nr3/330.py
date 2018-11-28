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

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<double> VD;
typedef vector<PII> VPI;
typedef vector<VPI> VVPI;
typedef set<string> SET;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<double, double> PDD;
typedef vector<PDD> VPD;

bool inside(const PDD &point, double R)
{
	return point.X*point.X+point.Y*point.Y < R*R;
}
double pi;
double R;
double add(const PDD &x1, const PDD &x2)
{
	double sum = 0.0;
	if (x1.X == x2.X || x1.Y == x2.Y)
	{
		sum += x1.X*x1.Y/2.0;
		sum += (x2.X-x1.X)*(x1.Y+x2.Y)/2.0;
		sum -= x2.X*x2.Y/2.0;
	}
	else
	{
		double a1 = atan2(x1.Y, x1.X);
		double a2 = atan2(x2.Y, x2.X);
		double da = a1-a2;
		sum = R*R*da/(2.0);
	}
	return sum;
}
int main()
{
    freopen("q3.in", "r", stdin);
    freopen("q3.out", "w+", stdout);
	pi = 2.0*acos(0.0);
	int n;
	cin >> n;
	REP(it,n)
	{
		double f, t, r, g;
		cin >> f >> R >> t >> r >> g;
		t += f;
		r += f;
		g -= 2.0*f;
		double base = pi*R*R;
		R -= t;
		double prob = 0.0;
		if (R <= 0.0 || g <= 0.0)
			prob = 1.0;
		else
		{
			double live = 0;
			for (double x = r; x < R; x += g+2.0*r)
				for (double y = r; x*x+y*y < R*R; y += g+2.0*r)
				{
					double nx = x+g;
					double ny = y+g;
					if (nx*nx+ny*ny < R*R)
						live += g*g;
					else
					{
						VPD it;
						it.pb(PDD(x, y));
						it.pb(PDD(x, ny));
						it.pb(PDD(nx, ny));
						it.pb(PDD(nx, y));
						it.pb(PDD(x, y));
						VPD ps;
						ps.pb(it[0]);
						REP(qi,SZ(it)-1)
						{
							PDD x1 = it[qi];
							PDD x2 = it[qi+1];
							bool in1 = inside(x1, R);
							bool in2 = inside(x2, R);
							//if (in1)
							//	ps.pb(x1);
							if (in1 != in2)
							{
								if (x1.X == x2.X)
								{
									x1.Y = sqrt(R*R-x1.X*x1.X);
								}
								else
								{
									x1.X = sqrt(R*R-x1.Y*x1.Y);
								}
								ps.pb(x1);
							}
							if (in2)
								ps.pb(x2);
						}
						double pis = 0.0;
						REP(qi,SZ(ps)-1)
						{
							PDD x1 = ps[qi];
							PDD x2 = ps[qi+1];
							double bb = add(x1, x2);
							pis += bb;
						}
						live += pis;
					}
				}
			live *= 4.0;
			prob = 1.0-live/base;
		}
		printf("Case #%d: %.6lf\n", it+1, prob);
	}
}
