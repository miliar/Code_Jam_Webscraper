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

bool check(int x, int y, int n, int m)
{
	if (0 <= x && x <= n && 0 <= y && y <= m)
		return true;
	return false;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w+", stdout);
	int c;
	cin >> c;
	REP(it,c)
	{
		int n, m, a;
		cin >> n >> m >> a;
		if (a > m*n)
		{
			cout << "Case #" << it+1 << ": IMPOSSIBLE" << endl;
		}
		else
		{
			int x1 = 0;
			int y1 = 0;
			int x2 = n;
			int y3 = (a+n-1)/n;
			bool done = false;
			int y2;
			REP(x3,n+1)
			{
				y2 = a;
				if (x3)
					y2 = abs(a-x2*y3)/x3;
				if (check(x2,y2,n,m) && check(x3,y3,n,m) && a == abs(x2*y3-x3*y2))
				{
					cout << "Case #" << it+1 << ":" << ' ' << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
					done = true;
					break;
				}
			}
			if (!done)
				cout << "ERROR" << endl;
			if (a != abs(x2*y3-x3*y2))
				cout << "ERROR" << endl;
		}
	}
}

