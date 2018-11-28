#include <iostream>
using namespace std;

int pd,pg;
long long n;

int gcd(int a, int b)
{
    while (b)
    {
        int t=b;
        b=a%b;
        a=t;
    }
    return a;
}

int main()
{
    freopen("a4.in","r",stdin);
    freopen("a4.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%I64d%d%d",&n,&pd,&pg);
        if (pd<100&&pg==100)
        {
            printf("Case #%d: Broken\n",cas);
            continue;
        }
        if (pd>0&&pg==0)
        {
            printf("Case #%d: Broken\n",cas);
            continue;
        }
        int t=gcd(pd,100);
        if (n>=100/t) printf("Case #%d: Possible\n",cas);
        else printf("Case #%d: Broken\n",cas);
    }
    return 0;
}
