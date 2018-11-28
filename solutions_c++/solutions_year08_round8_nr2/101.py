#pragma warning(disable:4996)
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
#define SZ(c) ((int)(c).size())

typedef vector<int> VI;
typedef vector<bool> VB;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<VB> VVB;
typedef vector<VI> VVI;
typedef vector<VPI> VVPI;
typedef map<string, VPI> MAP;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w+", stdout);
	int t;
	cin >> t;
	REP(it,t)
	{		
		int n;
		cin  >> n;
		cerr << it << ' ' << n << endl;
		MAP M;
		int mi = INF;
		int ma = -INF;
		REP(i,n)
		{
			string color;
			int start;
			int end;
			cin >> color >> start >> end;
			M[color].pb(PII(start, end+1));			
		}
		mi = 1;
		ma = 10000+1;
		VVPI V;
		for (MAP::const_iterator it1 = M.begin(); it1 != M.end(); ++it1)
		{
			V.pb(it1->Y);
		}
		REP(i,SZ(V))
			sort(ALL(V[i]));
		int res = INF;
		REP(x,SZ(V))
		{
			FOR(y,-1,x)
				FOR(z,-2,y)
		{
			VPI v;
			v.insert(v.end(), ALL(V[x]));
			if (y >= 0)
			v.insert(v.end(), ALL(V[y]));
			if (z >= 0)
			v.insert(v.end(), ALL(V[z]));
			sort(ALL(v));

			int cur = mi;
			int next = mi;
			int r = 0;
			int ind = 0;
			while (next != ma)
			{
				if (ind == SZ(v))
				{
					r = INF;
					break;
				}
				const PII &p = v[ind];
				if (p.X > cur)
				{
					cur = next;
					r++;
				}
				if (p.X > cur)
				{
					r = INF;
					break;
				}
				next = max(next, p.Y);
				ind++;
			}
			res = min(r+1, res);
		}
		}
		if (res == INF)
			cout << "Case #" << it+1 << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << it+1 << ": " << res << endl;
	}
}
