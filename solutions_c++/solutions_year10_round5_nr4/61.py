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

const int mod = 1000000007;
const int base = 70;
const int maxcarry = base+1;
int precalc[base+1][base+1][base*base+1 + base];
int cnk[base+1][base+1];
int fact[base+1];
int d[base+1][maxcarry][base+1];

ll inverse(ll a, ll n) {
    ll x = 1, y = 0, b = n, k;
    for (;b; swap(x, y), swap(a, b)) {
        k = a / b;
        a -= b * k;
        x -= y * k;
    }
    return x < 0 ? x + n : x;
}

int main() {
    REP (i, base+1) {
        cnk[i][0] = cnk[i][i] = 1;
        FOR (j, 1, i)
            cnk[i][j] = (cnk[i-1][j-1] + cnk[i-1][j]) % mod;
    }
    fact[0] = 1;
    FOR (i, 1, base+1) {
        fact[i] = ((long long) fact[i-1] * i) % mod;
    }
    #ifdef LOCAL
	freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    #endif
    precalc[0][1][0] = 1;
    for (int len = 0; len < base; ++len)
        for (int last = 1; last < base; ++last)
            for (int res = 0; res < base*base; ++res) 
                    if (precalc[len][last][res]) {
                        precalc[len][last+1][res] += precalc[len][last][res];
                        precalc[len][last+1][res] %= mod;
                        precalc[len+1][last+1][res + last] += precalc[len][last][res];
                        precalc[len+1][last+1][res + last] %= mod;
                    }    
    REP (len, base+1) REP (last, base) REP (res, base*base)
        precalc[len][last][res] = ((ll) precalc[len][last][res] * fact[len]) % mod;
    int test;
    scanf ("%d", &test);
    FOR (test_num, 1, test + 1) {
        long long n;
        int b;
        cin >> n >> b;
        vector <int> arr;
        while (n) {
            arr.pb (n % b);
            n /= b;
        }
        int m = SZ (arr);
        long long ans = 0;
        FOR (start, 1, b+1) {
            memset (d, 0, sizeof (d));
            d[0][0][start] = 1;
            REP (i, m) {
                REP (j, b+1)
                    REP (k, b+1) if (d[i][j][k]) {
                        REP (zero, 2) {
                            REP (active, k+1) {
                                for (int t = (arr[i] - j + b) % b; t <= b * k; t += b) {                                                                        
                                    if (zero) {
                                        if (!active) continue;
                                        d[i+1][(j+t) / b][active] = (d[i+1][(j+t) / b][active] + (k*(((ll) precalc[k-1][b][t] * cnk[k-1][active-1]) % mod)) % mod * d[i][j][k]) % mod;
                                    } else {
                                        d[i+1][(j+t) / b][active] = (d[i+1][(j+t) / b][active] + (((ll) precalc[k][b][t] * cnk[k][active]) % mod) * d[i][j][k]) % mod;
                                    }
                                }                                
                            }
                        }
                    }
                ans += (ll) d[m][0][0] * inverse (fact[start], mod);
                ans %= mod;
            }
        }
        printf ("Case #%d: %d\n", test_num, ans);
    }
	return 0;
}
