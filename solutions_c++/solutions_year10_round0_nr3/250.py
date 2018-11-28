# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <ctime>
# include <cmath>
# include <iostream>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <map>
# include <list>
# include <queue>
# include <list>
# include <functional>
# include <numeric>
# include <utility>
# include <iomanip>
# include <sstream>
# define MAXN 1000
using namespace std;

int main()
{
    int t, r, k, n;
    int v[MAXN], w[MAXN], ind[MAXN];
    bool vis[MAXN];
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%d%d%d", &r, &k, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &v[i]);
        }
        memset(vis, 0, sizeof vis);
        for (int i = 0; i < n; i++) {
            int sum = 0;
            int j;
            for (j = 0; j < n && sum + v[(i + j) % n] <= k; sum += v[(i + j) % n], j++);
            w[i] = sum;
            ind[i] = (i + j) % n;
        }
        int ii = 0;
        while(true) {
            if (vis[ii]) {
                break;
            }
            vis[ii] = true;
            ii = ind[ii];
        }
        int kk = 0;
        int jj = ii;
        long long int ans = 0LL;
        long long int tot = 0LL;
        do {
            kk++;
            tot += (long long int) (w[jj]);
            jj = ind[jj];
        } while(jj != ii);
        jj = 0;
        while(r > 0 && jj != ii) {
            ans += (long long int) (w[jj]);
            jj = ind[jj];
            r--;
        }
        ans += tot * (long long int) (r / kk);
        jj = ii;
        for (int i = 0; i < (r % kk); i++) {
            ans += (long long int) (w[jj]);
            jj = ind[jj];
        }
        printf("Case #%d: %lld\n", tt, ans);
    }
    return 0;
}
