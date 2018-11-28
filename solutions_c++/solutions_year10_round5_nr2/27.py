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
#define INFLL 1000000000000000001LL
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

    int t;
    cin >> t;
    REP (tt, t)
    {
        cout << "Case #" << (tt+1) << ": ";

        long long l;
        int n;
        cin >> l >> n;
        VI a(n);

        REP (i, n)
            cin >> a[i];

        SORT (a);

        int c = 0;
        REP (i, a.size()-1)
            c += a[i]*(a[i+1]-1);

        VI r(c+1, INF);
        r[0] = 0;

        REP (i, c)
            if (r[i]<INF)
                REP (j, n-1)
                    if (i + a[j] <= c)
                        r[i + a[j]] <?= r[i]+1;

        long long res = INFLL;

        REP (i, c+1)
            if (r[i]<INF && i<=l)
            {
                if ((l - i) % a.back())
                    continue;
                res <?= r[i] + (l-i)/a.back();
            }

        if (res == INFLL)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << res << endl;
    }

	return 0;
}
