#include <iostream>

using namespace std;

int a[10000];

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases, sum, u, i, n;
    scanf("%d", &cases);
    for(u = 1; u <= cases; u++)
    {
        sum = 0;
        scanf("%d", &n);
        if(n == 1)
        {
            scanf("%d", &a[0]);
            printf("Case #%d: 0.000000\n", u);
            continue;
        }
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &a[i]);
            if(a[i] == i)
                sum++;
        }
        printf("Case #%d: %d.000000\n", u, n - sum);
    }
    return 0;
}
