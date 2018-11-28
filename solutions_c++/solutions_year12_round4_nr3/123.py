//#pragma comment(linker, "/STACK:66777216")
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <deque>
#include <complex>
#include <bitset>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; --i)
#define REP(i,a) for(int i=0,_a=(a); i<_a; ++i)
#define ll long long
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define DEBUG(x) cout << #x << " = " << x << endl;
#define PR(a,n) cout << #a << " = "; FOR(i,1,n) cout << a[i] << ' '; puts("");
#define PR0(a,n) cout << #a << " = "; REP(i,n) cout << a[i] << ' '; puts("");
using namespace std;

const double PI = acos(-1.0);

int n, x[2011], h[2011], l[2011], r[2011], a[2011];

bool can() {
    FOR(i,1,n) {
        int u = a[i];
        h[u] = r[u];
        FOR(v,1,u-1) {
            if (x[v] == u) {
                FOR(j,v+1,n) if (j != u) {
                    r[j] = min(r[j], (h[u] - l[v]) / (u-v) * (j-v) + l[v]);
                    if (r[j] < 0) return false;
                }
            }
            else {
                int j = x[v];
                l[j] = max(l[j], ((h[u] - l[v]) / (u-v) + 1) * (j-v) + l[v]);
            }
        }
    }
    FOR(i,1,n) if (r[i] < l[i]) return false;
    return true;
}

bool solve2() {
    REP(turn,10000) {
        FOR(i,1,n) h[i] = rand() * rand() % 1000000000;
        int cnt = 0;
        bool has = true;
        
        bool cont = true;
        while (cont) {
            cont = false;
            ++cnt;
            if (cnt > 100) {
                has = false;
                break;
            }
            FOR(v,1,n-1) {
                int u = x[v];
                FOR(j,v+1,n) if (j != u) {
                    int val = h[v] + (j-v) * (ll)(h[u] - h[v]) / (u-v) - 1;
                    if (val < h[j]) {
                        cont = true;
                        h[j] = val;
                    }
                }
            }
            FOR(i,1,n) if (h[i] < 0) {
                has = false;
                break;
            }
        }
        
        if (has) return true;
    }
    return false;
}

bool check() {
    FOR(v,1,n-1) {
        int u = x[v];
        FOR(j,v+1,n) if (j != u) {
            if ((h[u] -h[v]) * (ll) (j-v) <= (h[j] - h[v]) * (ll) (u-v)) return false;
        }
    }
    return true;
}

void solve() {
    FOR(i,1,n) a[i] = i;
    FOR(i,1,n) l[i] = 0, r[i] = 1000000000;
    bool has = false;
    int cnt = 0;
    do {
        ++cnt;
        if (cnt == 100) break;
        if (can()) {
            has = true;
            break;
        }
    } while (next_permutation(a+1, a+n+1));
    if (!has) {
        if (!solve2() || !check()) puts("Impossible");
        else {
            FOR(i,1,n) printf("%d ", h[i]);
            puts("");
        }
    }
    else {
        FOR(i,1,n) printf("%d ", h[i]);
        puts("");
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        scanf("%d", &n);
        FOR(i,1,n-1) scanf("%d", &x[i]);
        solve();
    }
    return 0;
}
