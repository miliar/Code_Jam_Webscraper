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

int n, D, d[10111], l[10111], f[10111];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        scanf("%d", &n);
        FOR(i,1,n) scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &D);
        
        FOR(i,1,n) f[i] = 0;
        f[1] = min(l[1], d[1]);
        FOR(j,1,n) if (f[j]) {
            FOR(i,j+1,n) if (f[j] >= d[i] - d[j]) {
                f[i] = max(f[i], min(l[i], d[i] - d[j]));
            }
        }
        
        bool can = false;
        FOR(i,1,n) if (f[i] + d[i] >= D) can = true;
        if (can) puts("YES"); else puts("NO");
    }
    return 0;
}
