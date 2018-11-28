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

	int tt;
	cin >> tt;

	REP (t, tt)
	{
		cout << "Case #" << t+1 << ": ";

		int n;
		cin >> n;

		if (n==0)
		{
			cout << 0 << endl;
			continue;
		}

		VI a(n);

		REP (i, n)
			cin >> a[i];

		SORT (a);

		int r1 = 1;
		int r2 = n;

		while (r1<r2)
		{
			int r = (r1+r2+1)/2;

			VI u(n);

			bool ok = true;

			//cout << r << endl;

			REP (i, n)
				if (!u[i])
				{
					//cout << i << " " << u[i] << endl;

					u[i] = 1;
					int x = i+1;
					int v = a[i]+1;

					while (1)
					{
						while (x < n && a[x] < v)
							x++;

						while (x < n && a[x] == v && u[x] == 1)
							x++;

						if (x >= n || a[x] > v)
						{
							if (v < a[i] + r)
							{
								ok = false;
							}
							break;
						}


						//cout << x << " " << a[x] << " " << v<< endl;

						while (x+1< n && a[x+1] == v && u[x+1] == 0)
							x++;

						//cout << x << endl;

						if (u[x] == 0)
						{
							if (v < a[i] + r)
								u[x] = 1;
							else
								u[x] = 2;
						}
						else
						{
							if (v < a[i] + r)
								u[x] = 1;
							else
								break;
						}

						v++;
						x++;
					}
					if (!ok)
						break;
				}
			if (ok)
				r1 = r;
			else
				r2 = r-1;
		}

		cout << r1 << endl;
	}

	return 0;
}
