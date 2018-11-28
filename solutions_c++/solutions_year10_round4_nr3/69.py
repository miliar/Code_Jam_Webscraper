#include <iostream>
#include <cstdio>
#include <bitset>
#include <cstring>
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

bool a[128][128];
int main() {
#ifdef LOCAL
	freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);
#endif
    int test;
    scanf ("%d", &test);
    FOR (test_num, 1, test + 1) {
        int r;
        cin >> r;
        memset (a, 0, sizeof (a));
        int res = 0;
        REP (i, r) {
            int x1, y1, x2, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            FOR (x, x1, x2+1)
                FOR (y, y1, y2+1) {
                    a[x+1][y+1] = true;
                }
        }
        while (1) {
            bool any = false;
            FORD (i, 120, 1) FORD (j, 120, 1) {
                if (a[i][j]) any = true;
                if (a[i-1][j] && a[i][j-1]) a[i][j] = true;
                if (!a[i-1][j] && !a[i][j-1]) a[i][j] = false;
            }
            if (!any) break;
            ++res;
        }        
        printf ("Case #%d: ", test_num);
        cout << res << endl;
    }
	return 0;
}
