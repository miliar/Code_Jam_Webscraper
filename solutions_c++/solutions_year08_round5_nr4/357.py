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

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w+", stdout);
	int c;
	cin >> c;
	REP(it,c)
	{
		int n, m, r;
		cin >> n >> m >> r;
		VVI B(n, VI(m, true));
		REP(i,r)
		{
			int x, y;
			cin >> x >> y;
			x--;
			y--;
			B[x][y] = false;
		}
		VVI A(n+100, VI(m+100));
		A[0][0] = 1;
		REP(i,n)
			REP(j,m)
			{
				if (B[i][j])
				{
					A[i+2][j+1] += A[i][j];
					A[i+1][j+2] += A[i][j];
					A[i+2][j+1] %= 10007;
					A[i+1][j+2] %= 10007;
				}
			}
		printf("Case #%d: %d\n", it+1, A[n-1][m-1]);
	}
}
