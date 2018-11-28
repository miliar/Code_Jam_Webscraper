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

const long long INFLL = 100000000000000000LL;

int a[1<<10];
long long b[16][1<<10][16];

int main() {
#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif
    int test;
    scanf ("%d", &test);
    FOR (test_num, 1, test + 1) {
        int p;
        cin >> p;
        REP (i, 1<<p) {
            cin >> a[i];
            a[i] -= p;
            
            REP (j, p+1)
                b[0][i][j] = INFLL;
                
            if (a[i] > 0) a[i] = 0;
            
            b[0][i][-a[i]] = 0;
            
        }
        
        FOR (i, 1, p+1)
            REP (j, 1<<(p-i)) {
                REP (k, p+1)
                    b[i][j][k] = INFLL;
                int cost;
                cin >> cost;
                REP (q, p+1) REP (w, p+1) {               
                    b[i][j][max (max (q, w)-1, 0)] = min (b[i][j][max (max (q, w)-1, 0)], b[i-1][j*2][q] + b[i-1][j*2+1][w] + cost);
                    b[i][j][max (q, w)] = min (b[i][j][max (q, w)], b[i-1][j*2][q] + b[i-1][j*2+1][w]);
                }
            }
        printf ("Case #%d: ", test_num);
        cout << b[p][0][0] << endl;
    }
	return 0;
}
