#include <iostream>
#include <cstring>

#define N 1024
using namespace std;

int main()
{
    int t, test = 1, n;
    int i, j;
    int x[N];
    int ans;

    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--)
    {
        scanf("%d", &n);
        for (i=1; i<=n; i++)
            scanf("%d", &x[i]);

        ans = 0;
        for (i=1; i<=n; i++)
            if (x[i] != i)
                ans++;

        printf("Case #%d: %d.000000\n", test++, ans);
    }

    return 0;
}
