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

int readt ()
{
	string s;
	cin >> s;
	s[2]=' ';
	int x, y;
	sscanf (s.c_str(), "%d%d", &x, &y);
	return x*60+y;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	int tt;
	cin >> tt;
	REP (t, tt)
	{
		cout << "Case #"<<(t+1)<<": ";
		int T;
		cin >> T;

		VPII a, b;
		int na, nb;
		cin >> na >> nb;
		a.resize(na);
		REP (i, na)
		{
			a[i].X = readt();
			a[i].Y = readt();
		}

		b.resize(nb);
		REP (i, nb)
		{
			b[i].X = readt();
			b[i].Y = readt();
		}

		VI ua (na);
		VI ub (nb);

		SORT (a);
		SORT (b);

		int resa = na;
		int resb = nb;

		REP (i, na)
		{
			int x = 0;
			while (x<nb && (ub[x] || b[x].X<a[i].Y+T))
				x++;
			if (x<nb)
			{
				ub[x] = 1;
				resb--;
			}
		}

		REP (i, nb)
		{
			int x = 0;
			while (x<na && (ua[x] || a[x].X<b[i].Y+T))
				x++;
			if (x<na)
			{
				ua[x] = 1;
				resa--;
			}
		}
		cout << resa << " " << resb<< endl;
	}

	return 0;
}
