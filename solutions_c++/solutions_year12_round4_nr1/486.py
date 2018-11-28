#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#define N 20010
using namespace std;
struct data
{
    int d, l;
}dat[N];
int n, s, dp[N];
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int CA = 1; CA <= T; ++CA)
    {
        memset(dp, 0, sizeof(dp));
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i)
            scanf("%d%d", &dat[i].d, &dat[i].l);

        dp[1] = dat[1].d + min(dat[1].d, dat[1].l);
        for (int i = 2; i <= n; ++i)
            for (int j = 1; j < i; ++j)
                if ((dp[j] >= dat[i].d))
                    dp[i] = max(dp[i], min(dat[i].l + dat[i].d, 2 * dat[i].d - dat[j].d));
        bool flag = false;
        scanf("%d", &s);
        for (int i = 1; i <= n; ++i)
            if (dp[i] >= s)
            {
                flag = true;
                break;
            }
        printf("Case #%d: %s\n", CA, (flag) ? "YES" : "NO");
    }
    return 0;
}
