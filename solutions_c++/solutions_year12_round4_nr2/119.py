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

int n, X, Y;
int r[1011], x[1011], y[1011], a[1011];

bool cut(int i, int j) {
    if (x[i] + r[i] > x[j] - r[j] && x[j] + r[j] > x[i] - r[i])
    if (y[i] + r[i] > y[j] - r[j] && y[j] + r[j] > y[i] - r[i])
        return true;
    return false;
}

bool can() {
    int lastx = -r[a[1]];
    FOR(i,1,n) {
        x[a[i]] = lastx + r[a[i]];
        if (x[a[i]] > X) {
            lastx = 0;
            x[a[i]] = 0;
        }
        y[a[i]] = 0;
        FOR(j,1,i-1) if (cut(a[i], a[j])) {
            y[a[i]] = max(y[a[i]], y[a[j]] + r[a[j]] + r[a[i]]);
        }
        
        if (x[a[i]] > X || y[a[i]] > Y) return false;
        
        lastx = x[a[i]] + r[a[i]];
    }
    return true;
}

void solve() {
    FOR(i,1,n) a[i] = i;
    FOR(turn,1,n) {
        FOR(i,1,n-1)
        if (r[a[i]] > r[a[i+1]]) swap(a[i], a[i+1]);
    }
    
    bool has = false;
    int cnt = 0;
    do {
        ++cnt;
        if (can()) {
            has = true;
            break;
        }
    } while (next_permutation(a+1, a+n+1));
    
    if (!has) puts("WRONG");
    FOR(i,1,n) {
        printf(" %d %d", x[i], y[i]);
        if (x[i] > X || y[i] > Y) puts("WRONG");
    }
    puts("");
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        cout << "Case #" << test << ":";
        scanf("%d%d%d", &n, &X, &Y);
        FOR(i,1,n) {
            scanf("%d", &r[i]);
        }
        solve();
    }
    return 0;
}
