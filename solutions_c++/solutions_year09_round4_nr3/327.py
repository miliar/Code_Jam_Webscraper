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
    	int n, k;
    	cin >> n >> k;

    	int e[128][128];
    	vector <vector <long long> > a(n, vector <long long >(k));
    	memset (e, 0, sizeof (e));

    	REP (i, n)
			REP (j, k)
				cin >> a[i][j];
    	if (t==111119)
    	{
    		REP (i, n)
    		{
    			REP (j, k)
					cout << a[i][j] << " ";
    			cout << endl;
    		}
    	}
    	SORT (a);

    	int c[128];
    	memset (c, 0, sizeof (c));

    	REP (i, n)
			FOR (j, i+1, n)
				REP (l, k-1)
				{
					if ((a[i][l]-a[j][l])*(a[i][l+1]-a[j][l+1])<=0)
					{
						e[i][j] = 1;
						e[j][i] = 1;
						c[i]++;
						c[j]++;
						break;
					}
				}

    	int res = 0;

		REP (i, 1<<n)
		{
			int r = 0;
			REP (j, n)
				if (i & (1<<j))
					r++;

			REP (j1, n)
				if (i & (1<<j1))
					FOR (j2, j1+1, n)
						if (i & (1<<j2))
							if (!e[j1][j2])
								goto next;

			res >?= r;

			next:;
		}

		cout << res << endl;
    }

    return 0;
}
