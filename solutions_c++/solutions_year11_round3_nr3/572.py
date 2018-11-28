#include<cstdio>
int a[100];
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++)
    {
        int n,l,r;
        scanf("%d%d%d",&n,&l,&r);
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        int ans=0;
        for (int i=l;i<=r;i++)
        {
            int flag=1;
            for (int j=0;j<n;j++)
                if (i%a[j] && a[j]%i)
                {
                    flag=0;
                    break;
                }
            if (flag)
            {
                ans=i;
                break;
            }
        }
        if (ans) printf("Case #%d: %d\n",cas,ans);
        else printf("Case #%d: NO\n",cas);
    }
    return 0;
}
