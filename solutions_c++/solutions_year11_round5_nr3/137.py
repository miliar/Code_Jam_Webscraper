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

typedef long double cfloat;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int t;
	cin >> t;

	REP (tt, t)
	{

		cout << "Case #" << tt+1 << ": ";

		int res = 0;

		int n, m;
		cin >> n >> m;
		vector<string> s(n);
		REP (i, n)
		{
			cin >> s[i];
		}

		vector < VPII> a(n, VPII(m));

		int u[6][6];

		REP (i, 1<<(n*m))
		{
			int ii = i;

			REP (x, n)
				REP (y, m)
				{
					int o = ii&1;
					ii >>= 1;
					if (s[x][y] == '|')	a[x][y] = PII (1, 0);
					if (s[x][y] == '-')	a[x][y] = PII (0, 1);
					if (s[x][y] == '\\') a[x][y] = PII (1, 1);
					if (s[x][y] == '/')	a[x][y] = PII (1, -1);

					if (o)
						a[x][y] = PII (-a[x][y].X, -a[x][y].Y);
				}

			memset (u, 0, sizeof(u));

			bool  ok = true;

			REP (sx, n)
				REP (sy, m)
					if (!u[sx][sy])
					{
						int x = sx;
						int y = sy;

						while (1)
						{
							if (u[x][y])
							{
								ok = false;
								goto next;
							}

							u[x][y] = 1;

							int nx = (x+a[x][y].X+n)%n;
							int ny = (y+a[x][y].Y+m)%m;

							if (nx == sx && ny == sy)
								break;

							x = nx;
							y = ny;
						}
					}

			next:;

			if (ok)
				res++;
		}

		cout << res << endl;
	}

	return 0;
}
