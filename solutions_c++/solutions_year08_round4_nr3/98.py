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

typedef vector<bool> VB;
typedef set<int> SET;
typedef vector<SET> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef pair<double, double> PDD;
typedef pair<PDD, PDD> PPD;
typedef vector<PPD> VPD;

double dist(const VPD &ships, const PPD &point)
{
	double res = 0.0;
	REP(i,SZ(ships))
	{
		const PPD &ship = ships[i];
		res = max(res, (fabs(ship.X.X-point.X.X)+fabs(ship.X.Y-point.X.Y)+fabs(ship.Y.X-point.Y.X))/ship.Y.Y);
	}
	return res;
}
int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w+", stdout);
	int c;
	cin >> c;
	REP(it,c)
	{
		int n;
		cin >> n;
		VPD ships;
		REP(i,n)
		{
			PPD ship;
			cin >> ship.X.X >> ship.X.Y >> ship.Y.X >> ship.Y.Y;
			ships.pb(ship);
		}
		PPD point;
		double ans = dist(ships, point);
		double shift = ans;
		while (shift > 1e-8)
		{
			bool update = true;
			while (update)
			{
				update = false;
				{
					double add = shift;
					point.X.X += add;
					double ax = dist(ships, point);
					if (ax < ans)
					{
						ans = ax;
						update = true;
					}
					else
						point.X.X -= add;

					point.X.Y += add;
					ax = dist(ships, point);
					if (ax < ans)
					{
						ans = ax;
						update = true;
					}
					else
						point.X.Y -= add;


					point.Y.X += add;
					ax = dist(ships, point);
					if (ax < ans)
					{
						ans = ax;
						update = true;
					}
					else
						point.Y.X -= add;
				}

				{
					double add = -shift;
					point.X.X += add;
					double ax = dist(ships, point);
					if (ax < ans)
					{
						ans = ax;
						update = true;
					}
					else
						point.X.X -= add;

					point.X.Y += add;
					ax = dist(ships, point);
					if (ax < ans)
					{
						ans = ax;
						update = true;
					}
					else
						point.X.Y -= add;


					point.Y.X += add;
					ax = dist(ships, point);
					if (ax < ans)
					{
						ans = ax;
						update = true;
					}
					else
						point.Y.X -= add;
				}
			}
			shift /= 2.0;
		}
		printf("Case #%d: %.6lf\n", it+1, ans);
	}
}
