/*
 * by purple
 * at 12-04-15 2:47:00
 */

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define rep(i,n) for(int i=0;i<(n);++i)
#define repf(i,a,b) for(int i=(a);i<=(b);++i)

int main() {
    freopen ("B.in", "r", stdin);
    freopen ("B.out", "w", stdout);
    
    int t, Case = 1;
    for (scanf ("%d", &t); t; --t) {
        int n, s, p;
        scanf ("%d%d%d", &n, &s, &p);
        int ans = 0;
        rep (i, n) {
            int num;
            scanf ("%d", &num);
            if (num >= 3 * p - 2) ++ans;
            else if (num >= max(1, 3 * p - 4) && s > 0) ++ans, --s;
        }
        if (p == 0) ans = n;
        printf ("Case #%d: %d\n", Case++, ans);
    }
    return 0;
}

