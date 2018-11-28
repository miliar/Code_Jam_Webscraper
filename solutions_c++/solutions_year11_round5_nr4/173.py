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
		cout <<"Case #" << (tt+1) << ": ";

		string s;

		cin >> s;

		long long num = 0;
		long long mask = -1;

		int ii = 0;

		FORD (i, s.size()-1, 0)
		{
			if (s[i] == '?')
				mask ^= (1LL << ii);
			if (s[i] == '1')
				num |= (1LL << ii);
			ii++;
		}

		//cout << num << " " << mask << endl;

		//cout << (9 & mask) <<endl;

		long long res = 0;

		REP (i, 1<<30)
		{
			if (((((long long)i) * i) & mask) == num)
			{
				res = i;
				res *= i;
				break;
			}
		}

		string rs = "";
		if (res == 0)
			rs = "0";

		while (res)
		{
			if (res&1)
				rs = "1"+rs;
			else
				rs = "0"+rs;

			res /= 2;
		}

		cout << rs << endl;
	}

	return 0;
}
