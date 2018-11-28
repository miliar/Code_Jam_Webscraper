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

typedef long long lint;
typedef vector<bool> VB;
typedef vector<int> VI;
typedef vector<VI> VVI;
int calc(bool and, int x, int y)
{
	if (and)
		return x&&y;
	return x||y;
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
	int t;
	cin >> t;
	REP(it,t)
	{
		int m, v;
		cin >> m >> v;
		VB A(m);
		VB C(m);
		VVI R(m, VI(2,INF));
		REP(i,(m-1)/2)
		{
			int x, y;
			cin >> x >> y;
			A[i] = x;
			C[i] = y;
		}
		FOR(i,(m-1)/2,m)
		{
			int r;
			cin >> r;
			R[i][r] = 0;
		}
		FORD(i,(m-1)/2-1,0)
		{
			REP(x,2)
				REP(y,2)
				{
					int res = calc(A[i],x,y);
					R[i][res] = min(R[i][res], R[2*i+1][x]+R[2*i+2][y]);
					if (C[i])
					{
						int res = calc(!A[i],x,y);
						R[i][res] = min(R[i][res], R[2*i+1][x]+R[2*i+2][y]+1);
					}
				}
		}
		int ans = R[0][v];
		if (ans == INF)
			cout << "Case #" << it+1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << it+1 << ": " << ans << endl;
	}
}
