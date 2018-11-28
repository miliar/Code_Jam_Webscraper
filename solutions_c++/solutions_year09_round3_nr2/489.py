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


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int T,N;
	VI x(500,0);
	VI y(500,0);
	VI z(500,0);
	VI vx(500,0);
	VI vy(500,0);
	VI vz(500,0);
	double x0,y0,z0;
	cin >> T;
	REP (il, T)
	{
		cout << "Case #"<<(t+1)<< ": ";
		cin >> N;
		REP(tt, N)
			cin >> x[tt] >> y[tt] >> z[tt] >> vx[tt] >> vy[tt] >> vz[tt];
		REP(tt,N)
		{
			x0+=x[tt]/N;
			y0+=y[tt]/N;
			z0+=z[tt]/N;

		}
		double t=0;

	}

	return 0;
}
