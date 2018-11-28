/*
 * by purple
 * at 12-04-14 11:34:17
 */

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <set>

using namespace std;

#define sz(x) ((int)((x).size()))
#define out(x) printf(#x" %d\n", x)
#define rep(i,n) for(int i=0;i<(n);++i)
#define repf(i,a,b) for(int i=(a);i<=(b);++i)

int main() {
    freopen ("C.in", "r", stdin);
    freopen ("C.out", "w", stdout);
    
    int t, a, b, Case = 1;
    for (scanf ("%d\n", &t); t; --t) {
        scanf ("%d%d", &a, &b);
        long long ans = 0;
        repf (i, a, b) {
            int tmp = i, now = i, base = 1;
            while (tmp) {
                base *= 10; tmp /= 10;
            }
            base /= 10;
            tmp = i; 
            set<int> has;
            while (tmp >= 10) {
                now = (now / 10) + (now % 10) * base;
                if (has.find(now) == has.end() && tmp % 10 != 0 && now > i && now <= b) {
                    //printf ("%d %d\n", ans, i, now);
                    has.insert(now);
                    ++ans;
                }
                tmp /= 10;
            }
        }
        printf ("Case #%d: %I64d\n", Case++, ans);
    }
    
    return 0;
}

