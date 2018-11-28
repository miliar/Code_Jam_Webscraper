#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int l, d, n;
    cin >> l >> d >> n;
    vector <string> a (d);
    REP (i, d)
        cin >> a[i];
    REP (i, n)
    {
        string s;
        cin >> s;
        VI x;        
        REP (i, SZ (s))
            if (isalpha (s[i]))
                x.pb (1<<(s[i]-'a'));
            else
            {   
                ++i;
                int y = 0;
                while (s[i] != ')')
                {
                    y |= 1<<(s[i]-'a');
                    ++i;
                }
                x.pb (y);
            }
        int res = 0;
        REP (i, SZ (a))
        {
            bool ok = true;
            REP (j, SZ (a[i]))
                if (!(x[j] & (1<<(a[i][j]-'a'))))
                {
                    ok = false;
                    break;
                }
            if (ok)
                ++res;
        }
        printf ("Case #%d: %d\n", i+1, res);
    }
	return 0;
}
