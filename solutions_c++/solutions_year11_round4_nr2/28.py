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
#include "string.h"
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

class Sum
{
public:
	Sum (const VVI& aa)
	{
		int n = aa.size()+1;
		int m = aa[0].size()+1;
		a = VVI (n+1, VI(m+1));
		REP (i, n-1)
			REP (j, m-1)
				a[i+1][j+1] = aa[i][j];

		REP (i, a.size())
			REP (j, a[i].size())
			{
				if (i)
					a[i][j] += a[i-1][j];
				if (j)
					a[i][j] += a[i][j-1];
				if (i && j)
					a[i][j] -= a[i-1][j-1];
			}
	}

	int getSum (int x1, int y1, int x2, int y2)
	{
		return a[x2+1][y2+1]-a[x1][y2+1]-a[x2+1][y1] + a[x1][y1];
	}
private:
	VVI a;
};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP(t, tt)
	{
		cout << "Case #" << t+1 << ": ";

		int n, m, d;

		cin >> n >> m >> d;

		VVI a(n, VI(m));

		REP (i, n)
		{
			string s;
			cin >> s;
			REP (j, m)
				a[i][j] = s[j]-'0';
		}

		VVI ax, ay;
		ax = a;
		ay = a;

		REP (i, n)
			REP (j, m)
			{
				ax[i][j] *= i * 2;
				ay[i][j] *= j * 2;
			}
		//cout << "ok" << endl;

		Sum sx(ax), sy(ay), s(a);
		//cout << "ok2" << endl;

		int res = 0;

		REP (x1, n-2)
			REP (y1, m-2)
			{
				FOR (d, 2, min(n-x1, m-y1))
				{
					int x2 = x1+d;
					int y2 = y1+d;

					int sumx = sx.getSum(x1,y1,x2,y2) - s.getSum(x1,y1,x2,y2)*(x1+x2);
					sumx -= a[x1][y1]*(2*x1-x1-x2);
					sumx -= a[x1][y2]*(2*x1-x1-x2);
					sumx -= a[x2][y1]*(2*x2-x1-x2);
					sumx -= a[x2][y2]*(2*x2-x1-x2);

					//cout << x1 << " " << y1 << " " << x2 << " " << y2 << " " << sumx << endl;
					//cout << sx.getSum(x1,y1,x2,y2) << endl;
					//cout << s.getSum(x1,y1,x2,y2)*(x1+x2) << endl;

					if (sumx)
						continue;

					int sumy = sy.getSum(x1,y1,x2,y2) - s.getSum(x1,y1,x2,y2)*(y1+y2);
					sumy -= a[x1][y1]*(2*y1-y1-y2);
					sumy -= a[x1][y2]*(2*y2-y1-y2);
					sumy -= a[x2][y1]*(2*y1-y1-y2);
					sumy -= a[x2][y2]*(2*y2-y1-y2);

					if (sumy)
						continue;

					res = max (res, d+1);
				}
			}

		if (!res)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}

	return 0;
}
