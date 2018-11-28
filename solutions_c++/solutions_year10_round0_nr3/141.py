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

int a[1024];
long long pay[1024];
int next[1024];

int main() {
    #ifdef LOCAL
	freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    #endif
    int test;
    scanf ("%d", &test);
    FOR (test_num, 1, test + 1) {
        int r, k, n;
        scanf ("%d%d%d", &r, &k, &n);
        REP (i, n)
            scanf ("%d", &a[i]);
        memset (pay, 0, sizeof (pay));
        REP (i, n) {
            int x = k;
            int j = 0;
            while (j < n && x >= a[(i+j) % n]) {
                x -= a[(i+j) % n];
                pay[i] += a[(i+j) % n];
                ++j;
            }
            next[i] = (i+j)%n;            
        }
        long long ans = 0;
        int c = 0;
        REP (i, r) {
            ans += pay[c];
            c = next[c];
        }
        printf ("Case #%d: ", test_num);
        cout << ans << endl;
    }
	return 0;
}
