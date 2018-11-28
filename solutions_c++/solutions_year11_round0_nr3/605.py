#include <stdio.h>
#include <string.h>

int main()
{
    int cas,n,x;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        int now=0,sum=0,mi=10000000;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&x);
            now^=x;
            sum+=x;
            if (x<mi) mi=x;
        }
        if (now==0) printf("Case #%d: %d\n",ll,sum-mi);
        else printf("Case #%d: NO\n",ll);
    }
    return 0;
}
