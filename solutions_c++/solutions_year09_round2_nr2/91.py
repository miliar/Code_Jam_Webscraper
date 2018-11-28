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
#define SZ(c) (c).size()
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w+", stdout);
	int t;
	cin >> t;
	FOR(it,1,t+1)
	{
		string s;
		cin >> s;
		if (!next_permutation(ALL(s)))
		{
			s += "0";
			sort(ALL(s));
			REP(i,SZ(s))
				if (s[i] != '0')
				{
					swap(s[0], s[i]);
					break;
				}
		}
		cout << "Case #" << it << ": " << s << endl;
	}
}
