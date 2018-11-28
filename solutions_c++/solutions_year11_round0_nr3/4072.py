#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define sz(a) ((int)((a).size()))
#define forn(i, n) for (int i = 0; i < (n); i++)
#define foreach(i, a) for (typeof((a).begin()) i = (a).begin(); i != (a).end(); ++i)
#define eprintf(...) {fprintf(stderr,__VA_ARGS__);fflush(stderr);}
typedef pair<int, int> ii;
typedef long long LL;

int a[20];

int main() {
    int tests;
    scanf("%d", &tests);
    forn(test, tests) {
        int n;
        scanf("%d", &n);
        forn(i, n) scanf("%d", &a[i]);
        int nn = 1 << n;
        int ans = -1;
        int c[2];
        forn(m, nn - 1) if (m) {
            c[0] = c[1] = 0;
            forn(i, n) c[!!(m & (1 << i))] ^= a[i];
            if (c[0] != c[1]) continue;
            c[0] = c[1] = 0;
            forn(i, n) c[!!(m & (1 << i))] += a[i];
            ans = max(ans, max(c[0], c[1]));
        }
        printf("Case #%d: ", test + 1);
        if (ans < 0) printf("NO\n");
            else printf("%d\n", ans);
    }
    return 0;
}
