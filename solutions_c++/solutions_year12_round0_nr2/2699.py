#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(void) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int i, t, T, n, s, p, x[111], ans;

    scanf("%d", &T);

    for (int t=1; t<=T; ++t) {
        scanf("%d %d %d", &n, &s, &p);
        ans = 0;

        for (i=0; i<n; ++i) {
            scanf("%d", &x[i]);
        }

        sort(x, x+n);

        for (i=n-1; i>=0; i--) {
            int a = (x[i]/3) + (x[i]%3 != 0);
            if ( a >= p ) ans++;
            else if ( s && x[i] > 1 && a+1 == p ) { ans++; s--; }
        }

        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
