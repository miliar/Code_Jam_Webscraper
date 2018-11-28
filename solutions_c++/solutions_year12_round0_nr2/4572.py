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
using namespace std;

const double PI = acos(-1.0);

int f[111][111], n, s, p, a[111];

int check(int a, int b, int c) {
    if (a < 0 || a > 10) return false;
    if (b < 0 || b > 10) return false;
    if (c < 0 || c > 10) return false;
    int ln = max(max(a, b), c);
    int nn = min(min(a, b), c);
    return ln - nn <= 2;
}

bool surprise(int a, int b, int c) {
    int ln = max(max(a, b), c);
    int nn = min(min(a, b), c);
    return ln - nn == 2;
}

int can(int a, int b, int c) {
    int ln = max(max(a, b), c);
    if (ln >= p) return 1;
    else return 0;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; scanf("%d", &ntest);
    FOR(test,1,ntest) {
        scanf("%d%d%d", &n, &s, &p);
        memset(f, -1, sizeof f);
        FOR(i,1,n) scanf("%d", &a[i]);
        
        f[0][0] = 0;
        FOR(i,0,n-1) FOR(j,0,i) if (f[i][j] >= 0) {
            FOR(x,0,10) FOR(y,max(0,x-2),min(10,x+2)) {
                int z = a[i+1] - x - y;
                if (check(x,y,z)) {
                    int jj = j; if (surprise(x,y,z)) jj++;
                    f[i+1][jj] = max(f[i+1][jj], f[i][j] + can(x,y,z));
                }
            }
        }
        
        printf("Case #%d: %d\n", test, f[n][s]);
    }
    return 0;
}
