#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int gcd(int a,int b)
{
    int r;
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
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int cas,pd,pg,i,g,t;
    long long n;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++)
    {
        scanf("%I64d %d %d",&n,&pd,&pg);
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
                if(pd==100) printf("Case #%d: Possible\n",i);
                else printf("Case #%d: Broken\n",i);
            }
            else
                printf("Case #%d: Possible\n",i);
        }
        else
            printf("Case #%d: Broken\n",i);
    }
}
