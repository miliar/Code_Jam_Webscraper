#include<stdio.h>
#include<math.h>
typedef long long LL;
int gcd(int a,int b)
{
    int t;
    while(b)
    {
        t=a%b;a=b;b=t;
    }
    return a;
}
int main()
{
    int t,pd,pg;
    LL n;
    freopen("GAL.in","r",stdin);
    freopen("GAL.out","w",stdout);
    scanf("%d",&t);
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%lld %d %d",&n,&pd,&pg);
        printf("Case #%d: ",cn);
        //printf("%d\n",100/gcd(pd,100));
        if((!pg&&pd)||(pg==100&&pd!=100)||(n<100/gcd(pd,100)))
        {
                printf("Broken\n");
                continue;
        }

            printf("Possible\n");

    }
    return 0;
}
