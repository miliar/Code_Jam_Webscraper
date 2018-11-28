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
int GG[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

char buffer[1024];
string pattern = "welcome to code jam";
string to4(int x)
{
	string s;
	REP(i,4)
	{
		s.pb(char('0'+x%10));
		x /= 10;
	}
	reverse(ALL(s));
	return s;
}
int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w+", stdout);
	int t;
	cin >> t;
	cin.getline(buffer, 1024);
	FOR(it,1,t+1)
	{
		cin.getline(buffer, 1024);
		string line(buffer);
		VI next(SZ(line), 0);
		REP(i,SZ(pattern))
		{
			char letter = pattern[i];
			VI was = next;
			int sum = i == 0 ? 1 : 0;
			REP(j,SZ(was))
			{
				next[j] = line[j] == letter ? sum : 0;
				sum = (sum+was[j])%10000;
			}
		}
		cout << "Case #" << it << ": " << to4(accumulate(ALL(next), 0)) << endl;
	}
}
