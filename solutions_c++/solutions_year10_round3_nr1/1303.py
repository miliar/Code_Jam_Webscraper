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
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int t;
	cin >> t;
	REP (tt, t)
	{
		cout << "Case #" << (tt + 1) << ": ";

		int res = 0;
		int num, l, r;
		VI left, right, left2, right2;

		cin >> num;
		REP (nn, num)
		{
			cin >> l >> r;
			left.push_back(l);
			right.push_back(r);
			left2.push_back(l);
			right2.push_back(r);
		}

		vector<int>::iterator li, ri, lx, rx;
		for (li = left.begin(), ri = right.begin();  li < left.end();  li++, ri++)
		{
			for (lx = left2.begin(), rx = right2.begin();  lx < left2.end();  lx++, rx++)
			{
				if (((*li > *lx) && (*ri < *rx)) || ((*li < *lx) && (*ri > *rx)))
				{
					res++;
				}
			}
		}

		res /= 2;
		cout << res << endl;
	}

	return 0;
}
