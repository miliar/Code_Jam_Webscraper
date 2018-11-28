#include <stdio.h>
#include <queue>
#include <algorithm>
#define INF 0x3fffffff
using namespace std;
struct QueNode
{
    int c;
    bool operator<(const QueNode & b) const
    {
        return c < b.c;
    }
};
int d[10010], l[10010];
int f[10010];
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("Asmall.txt", "w", stdout);
    int T, tcnt = 0;
    scanf("%d", &T);
    int n;
    while (T--)
    {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d%d", &d[i], &l[i]);
        }
        scanf("%d", &d[n]);
        memset(f, 0, sizeof(f));
        l[n] = INF;
        if (d[0] > l[0])
            printf("Case #%d: NO\n", ++tcnt);
        else
        {
            f[0] = d[0];
            int i;
            for (i = 0; i < n; i++)
            {
                int j;
                for (j = i + 1; j <= n && f[i] + d[i] >= d[j]; j++)
                {
                    f[j] = max(f[j], min(d[j] - d[i], l[j]));
                }
                if (j == n + 1)
                {
                    break;
                }
            }
            printf("Case #%d: %s\n", ++tcnt, i < n ? "YES" : "NO");
        }
    }
    return 0;
}
