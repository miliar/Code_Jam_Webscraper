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

bool a[1000001];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

	memset(a, 0, sizeof(a));

	VI p;

	FOR (i, 2, 1000001)
		if (!a[i])
		{
			p.pb (i);

			for (int j=i+i; j<1000001; j+=i)
				a[j] = 1;
		}

	int tt;
	cin >> tt;
	REP (t, tt)
	{
		cout << "Case #" << t+1 << ": ";
		long long n;
		cin>> n;
		int res = 0;
		if (n>1)
			res++;

		REP (i, p.size())
		{
			int c = 0;
			long long x = n;
			while (x>=p[i])
			{
				x/=p[i];
				c++;
			}
			if (c<=1)
				break;
			res += c-1;
		}

		cout << res << endl;
	}

	return 0;
}
