#include <stdio.h>

long long s[33];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,n,i,k,p,x,y;
    
    scanf("%d",&t);
    for(p=1;p<=t;p++)
    {
        s[1]=1;
        for(int i=2;i<=31;i++)
        {
            s[i]=s[i-1]*2+1;
        }
        scanf("%d %d",&x,&y);
        if(s[x]>y)
        {
            printf("Case #%d: OFF\n",p);
            continue;
        }
        k=y/(s[x]+1);
        y-=(s[x]+1)*k;
        if(y==s[x])
        {
            printf("Case #%d: ON\n",p);
        }
        else
        {
            printf("Case #%d: OFF\n",p);
        }
    }
    return 0;
}
            
