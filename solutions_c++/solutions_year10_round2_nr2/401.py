#include <stdio.h>
struct data{
    int x,v,tt;
}chick[60];

int main(void)
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    int n,k,b,t,i,j,res,t_case,t0;scanf("%d",&t_case);
    for (t0=1;t0<=t_case;++t0)
    {
        res=0;
        scanf("%d%d%d%d",&n,&k,&b,&t);
        for (i=0;i<n;++i)
            scanf("%d",&chick[i].x);
        for (i=0;i<n;++i)
        {
            scanf("%d",&chick[i].v);chick[i].tt=(b-chick[i].x)/chick[i].v;
            if ((b-chick[i].x)%chick[i].v)
                chick[i].tt++;
        }j=0;
        for (i=n-1;i>=0;--i)
        {
            if (chick[i].tt<=t)
            {
                res+=j;
                if (n-i-j>=k)
                    break;
            }
            else
                ++j;
        }
        if (n-j<k)
            printf("Case #%d: IMPOSSIBLE\n",t0);
        else
            printf("Case #%d: %d\n",t0,res);
    }

    fclose(stdin);fclose(stdout);
    return 0;
}

