#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int gcd(int a,int b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
int main()
{
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("A.out","w",stdout);
    int cas,n,pd,pg,i,g,t;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++)
    {
        scanf("%d %d %d",&n,&pd,&pg);
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

