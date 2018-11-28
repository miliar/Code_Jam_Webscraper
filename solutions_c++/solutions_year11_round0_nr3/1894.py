#include <iostream>

using namespace std;

int     solve()
{
    int n;
    scanf("%d", &n);
    int x;
    int t = 0;
    int ans = -1;
    int total = 0;
    for (int i = 0; i < n; i ++)
    {
        scanf("%d", &x);
        t ^= x;
        total += x;
        if (ans == -1 || x < ans)
            ans = x;
    }
    if (t != 0)
        return -1;
    return total - ans;
}

int     main()
{
    freopen("c.in", "r", stdin);
    freopen("c.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        printf("Case #%d: ", i);
        int ans = solve();
        if (ans == -1)
            printf("NO\n");
        else
            printf("%d\n", ans);
    }
}
