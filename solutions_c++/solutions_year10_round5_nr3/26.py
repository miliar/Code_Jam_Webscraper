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

    int t;
    cin >> t;
    REP (tt, t)
    {
        cout << "Case #" << (tt+1) << ": ";
        int c;
        cin >> c;
        VI a, b;

        int r = 0;

        while (c--)
        {
            int x, v;
            cin >> x >> v;
            while (v--)
                a.pb(x);
        }

        bool ch = true;

        while (ch)
        {
            ch = false;
            SORT (a);
            b = VI();
            REP (i, a.size())
            {
                if (i<a.size()-1 && a[i] == a[i+1])
                {
                    b.pb (a[i]-1);
                    b.pb (a[i]+1);
                    r ++;
                    ch = true;
                    i++;
                }
                else
                    b.pb (a[i]);
            }

            swap (a, b);
        }

        cout << r << endl;
    }

	return 0;
}
