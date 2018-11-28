#include <stdio.h>
long long gcd(long long x,long long y)
{
    while (x&&y)
        if (x>y) x%=y;
        else y%=x;
    return x==0?y:x;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        long long n;
        int pd,pg;
        scanf("%I64d%d%d",&n,&pd,&pg);
        printf("Case #%d: ",ii);
        long long gg=gcd(pd,100);
        if (gg==0)
        {
            if (pg!=100) puts("Possible");
            else puts("Broken");
        }
        long long less=100/gg;
        if (less>n) puts("Broken");
        else
        {
            if (pg!=100&&pg!=0) puts("Possible");
            else if (pd==100&&pg==100) puts("Possible");
            else if (pd==0&&pg==0) puts("Possible");
            else puts("Broken");
        }
    }
    return 0;
}
