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
	cin >> tt;

	REP (t, tt) {
		cout << "Case #"<<t+1 <<": ";

		int n, s, p;
		cin >> n >> s >> p;

		int res = 0;

		REP (i, n)
		{
			int x;
			cin >> x;
			int v1, v2;

			if (x%3 == 0) {
				v1 = x/3;
				v2 = x > 0 ? x/3+1 : 0;
			} else if (x%3 == 1) {
				v1 = x/3+1;
				v2 = x/3+1;
			} else if (x%3 == 2) {
				v1 = x/3+1;
				v2 = x > 2 ? x/3+2 : x/3+1;
			}

			if (v1 >= p) {
				res ++;
			} else if (v2 >= p && s)
			{
				res ++;
				s--;
			}
		}

		cout << res <<endl;

	}

	return 0;
}
