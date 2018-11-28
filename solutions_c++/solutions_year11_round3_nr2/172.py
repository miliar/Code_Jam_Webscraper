#include <stdio.h>
#include <string.h>

int a[111];

int main()
{
    int cas;
    int n,l,r;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d %d %d",&n,&l,&r);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        int end=0;
        for(int i=l;i<=r;i++)
        {
            bool flag=1;

            for(int j=0;j<n;j++)
             if(i%a[j]!=0&&a[j]%i!=0)
             {
                 flag=0;
                 break;
             }
            if (flag) {end=i;break;}
        }
        if (end) printf("Case #%d: %d\n",ll,end);
        else printf("Case #%d: NO\n",ll);
    }
    return 0;
}
