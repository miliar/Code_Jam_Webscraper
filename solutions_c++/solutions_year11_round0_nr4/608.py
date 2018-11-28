#include <stdio.h>
#include <string.h>

int main()
{
    int cas;
    int n,x;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d",&n);
        int num=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&x);
            if (i!=x) num++;
        }
        printf("Case #%d: %d.000000\n",ll,num);
    }
    return 0;
}
