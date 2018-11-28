# include <iostream>
# include <cstdio>
# include <cstring>
# include <vector>
# include <set>
# include <queue>
# include <string>
# define MAXN 30
using namespace std;

int main()
{
    int t, n, i, m, j, w[MAXN], ans;
    bool v[MAXN];
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%d", &n);
        ans = 0;
        m = 1 << (n - 2);
        for (i = 0; i < m; i++) {
            memset(v, 0, sizeof v);
            memset(w, 0, sizeof w);
            v[n] = true;
            for (j = 0; j < n - 2; j++) {
                if ((i & (1 << j)) > 0) {
                    v[j + 2] = true;
                    //cout << (j + 2) << " ";
                }
            }
            //cout << n << endl;
            for (j = 1; j <= n; j++) {
                w[j] = w[j - 1] + v[j];
            }
            j = n;
            while (j > 1) {
                if (!v[j]) {
                    break;
                }
                j = w[j];
            }
            if (j == 1) {
                //puts("YEEY");
                ans++;
                if (ans >= 100003) {
                    ans -= 100003;
                }
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
