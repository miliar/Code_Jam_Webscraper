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

typedef vector<string> VS;
bool Can[256][256];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w+", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	VS words;
	string word;
	REP(i,d)
	{
		cin >> word;
		words.pb(word);
	}
	FOR(it,1,n+1)
	{
		string pattern;
		cin >> pattern;
		memset(Can, false, sizeof(Can));
		int index = 0;
		REP(j,SZ(pattern))
		{
			if (pattern[j] == '(')
			{
				while (pattern[++j] != ')')
					Can[index][pattern[j]] = true;
			}
			else
			{
				Can[index][pattern[j]] = true;
			}
			index++;
			if (index > l)
				break;
		}
		int res = 0;
		if (index == l)
		{
			REP(j,d)
			{
				string word = words[j];
				bool good = true;
				REP(k,l)
					good &= Can[k][word[k]];
				res += good;
			}
		}
		else
		{
			cerr << "BUG" << endl;
		}
		cout << "Case #" << it << ": " << res << endl;
	}
}
