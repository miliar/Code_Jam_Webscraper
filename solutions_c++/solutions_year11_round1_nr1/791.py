#include <iostream>
#include <cstdio>

using namespace std;

int gcd(int a,int b)
{
    int t;
    while(b!=0)
    {
        t=a%b;
        a=b;
        b=t;
    }
    return a;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,tmp,cas;
    long long n;
    int pd,pg;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        scanf("%I64d %d %d",&n,&pd,&pg);
        if (pd==0||pg==0||pd==100||pg==100)
        {
            if (pd==pg) printf("Possible\n");
            else printf("Broken\n");
        }
        else
        {
            tmp=gcd(100,pd);
            tmp=100/tmp;
            if (n>=tmp) printf("Possible\n");
            else printf("Broken\n");
        }
    }
    return 0;
}
