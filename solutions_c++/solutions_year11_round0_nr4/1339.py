#include<cstdio>
int a[1000];
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
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        int ans=0;
        for (int i=0;i<n;i++)
            if (i==a[i]-1) ans++;
        printf("Case #%d: %d.000000\n",cas,n-ans);
    }
    return 0;
}
