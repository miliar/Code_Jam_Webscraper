#include <stdio.h>

int main()
{
    int i,j;
    int t;
    int num[120];
    int n,s,p;
    int mid,cnt;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        cnt = 0;
        scanf("%d%d%d",&n,&s,&p);
        for(j=0;j<n;j++)
        {
            scanf("%d",&num[j]);
        }
        for(j=0;j<n;j++)
        {
            mid = num[j]%3;
            if(mid==1 && (num[j]+2)/3 >= p)
            {
                cnt++;
                continue;
            }
            if(mid==2)
            {
                if((num[j]+1)/3 >= p)
                {
                    cnt++;
                    continue;
                }
                if((num[j]+4)/3 >=p && s>0)
                {
                    s--;
                    cnt++;
                    continue;
                }
                continue;
            }
            if(mid ==0)
            {
                if(num[j]/3>=p)
                {
                    cnt++;
                    continue;
                }
                if((num[j]+3)/3>=p && s>0 && num[j]>0)
                {
                    s--;
                    cnt++;
                    continue;
                }
            }
        }
        printf("Case #%d: %d\n",i,cnt);
    }
    return 1;
}
