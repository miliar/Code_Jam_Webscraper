#include <stdio.h>
#include <string.h>

int abss(int x)
{
    return x>0?x:-x;
}

int main()
{
    int cas;
    int ans,posa,posb,ta,tb,n;
    char s[10];
    int x,need;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d",&n);
        ans=0;
        posa=1;posb=1;
        ta=0;tb=0;
        for(int i=0;i<n;i++)
        {
            scanf("%s %d",s,&x);
            if (s[0]=='O')
            {
                need=abss(posa-x);
                if (need>ans-ta)
                {
                    ans+=need-(ans-ta);
                }
                ans++;
                ta=ans;
                posa=x;
            } else
            {
                need=abss(posb-x);
                if (need>ans-tb)
                {
                    ans+=need-(ans-tb);
                }
                ans++;
                tb=ans;
                posb=x;
            }
        }
        printf("Case #%d: %d\n",ll,ans);
    }
    return 0;
}
