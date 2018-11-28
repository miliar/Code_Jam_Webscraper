#include <cstdio>
#include <algorithm>
using namespace std;
int l[10010];
int d[10010];

int a[10010];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        int n;
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%d%d", &d[i], &l[i]);
            a[i] = 0;
        }
        int dd;
        scanf("%d", &dd);
        a[0] = d[0];

        int ans = 0;
        for(int i = 0; i < n; i++)
        {
            if(a[i] + d[i] >= dd)
            {
                ans = 1;
                break;
            }
            if(ans)break;
            for(int j = i+1; j < n && d[j] <= d[i]+a[i]; j++)
            {
                if(a[j] < min(l[j],d[j]-d[i]))
                {
                    a[j] = min(l[j],d[j]-d[i]);
                }

            }
        }
        printf("Case #%d: ", ti);
        if(ans)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
