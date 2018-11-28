#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

__int64 gcd(__int64 a,__int64 b)
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


int main ()
{
    freopen("A-large.in","r",stdin);
    freopen("o.txt","w",stdout);
    __int64 n,pd,pg,k,t;
    scanf("%I64d",&t);
    for(int i = 1;i <= t;++i)
    {
        scanf("%I64d%I64d%I64d",&n,&pd,&pg);
        k = gcd(pd,100);
        k = 100 / k;
//        printf("t=%d %d %d\n",t,pd,k);
        if(n>=k)
        {
            if(pg == 0 && pd == 0)
                printf("Case #%d: Possible\n",i);
            else if (pg == 0)
                printf("Case #%d: Broken\n",i);
            else if(pg==100 && pd == 100)
                printf("Case #%d: Possible\n",i);
            else if(pg== 100)
                printf("Case #%d: Broken\n",i);
            else
                printf("Case #%d: Possible\n",i);
        }
        else
            printf("Case #%d: Broken\n",i);

    }
    return 0;
}
