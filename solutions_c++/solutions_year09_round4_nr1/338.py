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

    int tt;
    cin >> tt;

    REP (t, tt)
    {
    	cout << "Case #" << (t+1) << ": ";
    	int n;
    	cin >> n;
    	vector <string> a(n);
    	REP(i, n)
			cin >> a[i];

    	VI b(n);
    	REP (i, n)
    	{
    		REP (j, n)
				if (a[i][j]=='1')
					b[i]>?=j;
    	}

    	int res = 0;

    	while (true)
    	{
			bool changed = false;
    		REP (i, b.size ()-1)
    		{
				if (b[i]>i)
				{
					int j = i+1;
					while (b[j] >= b[i])
						j++;
					FORD (k, j-1, i)
					{
						swap (b[k+1], b[k]);
						res++;
					}
					changed = true;
				}
				if (changed)
					break;
    		}
    		if (!changed)
    			break;
    	}
    	cout << res << endl;

    }

    return 0;
}
