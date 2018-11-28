#include <iostream>
using namespace std;

int r, k, n, g[1000], p[1000];

long long s[1000];

int main()
{
    freopen("C-small.in.txt", "r", stdin);
    freopen("C.out", "w", stdout);
    int cs;
    scanf("%d", &cs);
    for (int fcs=1; fcs<=cs; fcs++)
    {
        scanf("%d%d%d", &r, &k, &n);
        long long sum=0;
        for (int i=0; i<n; i++)
            scanf("%d", &g[i]), sum+=g[i];
        if(sum<=k) {
            printf("Case #%d: %lld\n", fcs, sum*r); continue;
        }
        for (int i=0; i<n; i++)
            for (s[p[i]=i]=0; s[i]+g[p[i]]<=k; ) {
                s[i]+=g[p[i]];
                p[i]=(p[i]+1)%n;
            }
        int now=0;
        long long ans=0;
        for (int i=0; i<r; i++, now=p[now])
            ans+=s[now];
        printf("Case #%d: %lld\n", fcs, ans);
    }
    return 0;
}
