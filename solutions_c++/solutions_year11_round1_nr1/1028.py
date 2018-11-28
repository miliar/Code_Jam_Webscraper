#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
long long  gcd(long long a,long long  b)
{
    long long  r;
    while(b)
    {
        r=a%b;
        a=b;
        b=r;
    }
    return a;
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a_out.txt","w",stdout);
    long long  cases,n,pd,pg,i,g,t;
    scanf("%lld",&cases);
    for(i=1;i<=cases;i++)
    {
        scanf("%lld%lld%lld",&n,&pd,&pg);
        g=gcd(pd,100);
        t=100/g;
        if(n>=t)
        {
            if(pg==0)
            {
                if(pd==0) printf("Case #%d: Possible\n",i);
                else printf("Case #%d: Broken\n",i);
            }
            else if(pg==100)
            {
                if(pd==100) printf("Case #%lld: Possible\n",i);
                else printf("Case #%lld: Broken\n",i);
            }
            else
                printf("Case #%lld: Possible\n",i);
        }
        else
            printf("Case #%lld: Broken\n",i);
    }
    return 0;
}
