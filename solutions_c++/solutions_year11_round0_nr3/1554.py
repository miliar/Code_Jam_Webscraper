#include <cstdio>
#include <algorithm>

using namespace std;

int cost[1100];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        int n;
        int sum = 0;
        int sum2 = 0;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &cost[i]);
            sum ^= cost[i];
            sum2 += cost[i];
        }
        sort(cost, cost+n);
        printf("Case #%d: ", ti);
        if(sum != 0)
        {
            printf("NO\n");
        }
        else
        {
            printf("%d\n", sum2 - cost[0]);
        }
    }
    return 0;
}
