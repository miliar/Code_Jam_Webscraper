#include <iostream>
#include <memory.h>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("3.in","r",stdin);
    freopen("3.out","w",stdout);
    int ca=0,i,n,xiao,now,s,t,x;
    scanf("%d",&t);
    while(t--)
    {
        ++ca;
        scanf("%d",&n);
        xiao=2000000000;
        s=0;
        for(i=1;i<=n;i++)
        {
            scanf("%d",&x);
            if(x<xiao) xiao=x;
            s+=x;
            if(i==1) {now=x; continue;}
            now=now^x;
        }
        printf("Case #%d: ",ca);
        if(now!=0) printf("NO\n");
        else
        {
            printf("%d\n",s-xiao);
        }
    }
    return 0;
}