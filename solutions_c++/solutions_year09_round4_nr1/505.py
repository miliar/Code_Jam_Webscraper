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
typedef vector<string> VS;

int calc(const string &s)
{
	int res = 0;
	REP(i,SZ(s))
		if (s[i] == '1')
			res = i;
	return res;
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
	int T;
	cin >> T;
	REP(it,T)
	{
		int n;
		cin >> n;
		VI v;
		REP(i,n)
		{
			string s;
			cin >> s;
			v.pb(calc(s));
		}
		int res = 0;
		REP(i,n)
			if (v[i] > i)
				FOR(j,i+1,n)
				{
					res ++;
					if (v[j] <= i)
					{
						v.erase(v.begin()+j);
						v.insert(v.begin()+i, v[i]);
						break;
					}
				}
				
		cout << "Case #" << it+1 << ": " << res << endl;
	}
}
