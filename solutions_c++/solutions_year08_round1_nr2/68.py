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

VI c, malted;
VVI e;
bool ok;
VI u;
int res;

void doit (int x)
{
	if (u[x])
		return;
	u[x] = 1;
	res++;

	if (!ok)
		return;

	REP (i, e[x].size ())
	{
		int y = e[x][i];
		c[y]--;
		if (c[y]<0)
			ok = false;
		if (c[y]==0)
		{
			if (malted[y]==-1)
			{
				ok = false;
				return;
			}
			doit (malted[y]);
		}
	}
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP (t, tt)
	{
		cout << "Case #" << (t+1) << ":";

		int n, m;
		cin >> n >> m;
		c = VI(m);
		malted = VI (m, -1);
		e = VVI(n);
		u = VI(n);
		res = 0;
		ok = true;

		REP (i, m)
		{
			cin >> c[i];
			REP (j, c[i])
			{
				int x, y;
				cin >> x >> y;
				x--;

				if (y)
				{
					c[i]--;
					malted[i] = x;
				}
				else
					e[x].pb (i);
			}
		}

		REP (i, m)
			if (!c[i])
			{
				if (malted[i]==-1)
					ok = false;
				else
					doit (malted[i]);
			}

		if (!ok)
 			cout <<" IMPOSSIBLE" << endl;
		else
		{
			REP (i, n)
				cout << " " <<u[i];
			cout << endl;
		}

	}

	return 0;
}
