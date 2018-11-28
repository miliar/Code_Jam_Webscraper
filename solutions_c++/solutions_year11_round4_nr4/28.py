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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	scanf ("%d", &tt);

	REP (T, tt)
	{
		cout << "Case #" << T+1 << ": ";

		int n,m;
		scanf ("%d%d", &n, &m);

		VI t(n, INF);
		VVI r(n, VI(n, -1));

		int ee[512][512];
		memset (ee, 0, sizeof(ee));
		VVI e(n);

		while (m--)
		{
			int x, y;
			scanf ("%d,%d", &x,&y);
			e[x].pb (y);
			e[y].pb (x);
			ee[x][y] = 1;
			ee[y][x] = 1;
		}

		r[0][0] = e[0].size();
		t[0] = 0;

		queue<int> q;
		q.push(0);

		int rt = 0;

		while (!q.empty())
		{
			int x = q.front();
			q.pop();
			if (ee[x][1])
			{
				rt = t[x];
				break;
			}

			REP (i, n)
				if (r[x][i] != -1)
				{
					REP (j, e[x].size())
					{
						int E = e[x][j];

						if (t[E] < t[x]+1)
							continue;

						int res = r[x][i]-1;

						REP (k, e[E].size())
							if (!ee[e[E][k]][i] && !ee[e[E][k]][x] && e[E][k]!=x)
								res++;

						if (t[E] == INF)
							q.push(E);
						t[E] = t[x]+1;

						r[E][x] = max(r[E][x], res);
					}
				}

		}
		int rr = 0;
		REP (i, n)
			if (ee[i][1] && t[i] == rt)
			{
				REP (j, n)
					rr = max(rr, r[i][j]);
			}

		cout << rt << " " <<rr << endl;

	}

	return 0;
}
