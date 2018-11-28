#include <stdio.h>

int main()
{
    int tmp,i,t,j,s,p,n,ans,max,min;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        ans = 0;
        printf("Case #%d: ",i);
        scanf("%d%d%d",&n,&s,&p);
        max = 3*p - 2;
        min = 3*p - 4;
        for(j=0;j<n;j++)
        {
            scanf("%d",&tmp);
            if(p == 0)
                ans++;
            else if(p == 1)
            {
                if(tmp>0)
                    ans++;
            }
            else if(tmp>=max)
                ans ++;
            else if(s>0&&tmp>=min)
            {
                ans ++;
                s--;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
