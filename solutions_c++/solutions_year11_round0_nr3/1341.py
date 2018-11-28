#include<cstdio>
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n;
        scanf("%d",&n);
        int min=0x7fffffff;
        int sum=0,tot=0;
        for (int i=0;i<n;i++)
        {
            int x;
            scanf("%d",&x);
            sum^=x;
            if (x<min) min=x;
            tot+=x;
        }
        if (sum)
            printf("Case #%d: NO\n",cas);
        else
            printf("Case #%d: %d\n",cas,tot-min);
    }
    return 0;
}
