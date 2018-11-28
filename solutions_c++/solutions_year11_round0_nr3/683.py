#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int inf = 1000000000;

int a[1005];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("w.out", "w", stdout);
    int cases, n, mi, u, i;
    int ans, sum;
    scanf("%d", &cases);
    for(u = 1; u <= cases; u++)
    {
        ans = 0;
        sum = 0;
        mi = inf;
        scanf("%d", &n);
        for(i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            if(mi > a[i])
                mi = a[i];
            sum += a[i];
            ans ^= a[i];
        }
        if(ans)
            printf("Case #%d: NO\n", u);
        else
            printf("Case #%d: %d\n", u, sum - mi);
    }
    return 0;
}
