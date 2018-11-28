#include <iostream>
#include <cstdio>
using namespace std;
typedef long long LL;
LL gcd(LL a,LL b)
{
    LL t;
    while(b != 0)
    {
        t = b;
        b = a % b;
        a = t;
    }
    return a;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    LL pd,pg,n,y;
    int t,k;
    bool flag;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%I64d%I64d%I64d",&n,&pd,&pg);
        y = 100 / gcd(pd,100);
        if(y <= n)
        {
            if(pg == 0)
            {
                if(pd == 0) flag = true;
                else flag = false;
            }
            else if(pg == 100)
            {
                if(pd == 100) flag = true;
                else flag = false;
            }
            else flag = true;
        }
        else flag = false;
        if(flag) printf("Case #%d: Possible\n",k);
        else printf("Case #%d: Broken\n",k);
    }
    return 0;
}
