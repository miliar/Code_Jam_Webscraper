#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
int gcd(long long a,long long b)
{
    if(!a) return b;
    return gcd(b%a,a);
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca=0;
    int a,b,m;
    long long n;
    scanf("%d",&m);
    while(m--)
    {
        scanf("%I64d%d%d",&n,&a,&b);
        bool fg=1;
        if(a==0||a==100)
        {
            if(b!=a&&(b==0||b==100)) fg=0;
        }
        else
        {
            if(b==0||b==100) fg=0;
            if(100/gcd(a,100)>n) fg=0;
        }
        if(fg) printf("Case #%d: Possible\n",++ca);
        else printf("Case #%d: Broken\n",++ca);
    }
    return 0;
}
