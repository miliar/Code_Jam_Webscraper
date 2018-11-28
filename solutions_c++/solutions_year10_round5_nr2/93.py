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

int a[128];
int d[1100001];

int main() {
    #ifdef LOCAL
	freopen("B-small-attempt1.in" , "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    #endif
    int test;
    scanf ("%d", &test);
    FOR (test_num, 1, test + 1) {
        ll l;
        int n;
        cin >> l >> n;        
        REP (i, 1100001)
            d[i] = INF;        
        d[0] = 0;
        REP (i, n) {
            cin >> a[i];
            REP (j, 1000001)
                d[j+a[i]] = min (d[j+a[i]], d[j]+1);
        }                
        sort (a, a + n);
        
        long long res = (long long) INF * INF + 1;
        for (long long take = l / a[n-1]; take >= 0 && l - take * a[n-1] <= 1000000; --take) 
            if (d[l - take * a[n-1]] != INF && take + d[l - take * a[n-1]] < res)
                res = take + d[l - take * a[n-1]];
        printf ("Case #%d: ", test_num);
        if (res == (long long) INF * INF + 1)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << res << endl;
    }
	return 0;
}
