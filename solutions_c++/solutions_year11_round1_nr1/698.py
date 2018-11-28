#include <iostream>
using namespace std;
#include <stdio.h>
int gcd(int x, int y)
{
     if(y == 0) return x;
     if(x < y)      return gcd(y,x);
     else        return gcd(y, x%y);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,PD,PG,PDL,PGL;
    long long N;
    scanf("%d",&T);
    for(int cnt=1;cnt<=T;cnt++)
    {
        scanf("%lld%d%d",&N,&PD,&PG);
        int Dmoment = gcd(PD,100);
        long long PDL = 100/Dmoment;
        if(PDL>N||(PG==0&&PD!=0)||(PG==100&&PD!=100)) { printf("Case #%d: Broken\n",cnt); }
        else printf("Case #%d: Possible\n",cnt);
    }
    return 0;
}
