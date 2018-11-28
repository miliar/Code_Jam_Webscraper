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
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w+", stdout);

    int l, d, n;

    cin >> l >> d >> n;

    vector <string> w(d);

    REP (i, d)
		cin >> w[i];

    REP (t, n)
    {
    	string s;
    	cin >> s;
    	vector < set<char> > a;

    	REP (i, s.size ())
    	{
    		set <char> S;
    		if (s[i]=='(')
    		{
    			i++;
    			while (s[i]!=')')
    				S.insert(s[i++]);
    		}
    		else
    			S.insert(s[i]);

    		a.pb (S);
    	}

    	int res = 0;

    	REP (i, d)
    	{
    		REP (j, l)
				if (a[j].find(w[i][j]) == a[j].end())
					goto next;

			res++;

    		next:;
    	}

    	cout << "Case #" << t+1 <<": " << res << endl;
    }

    return 0;
}
