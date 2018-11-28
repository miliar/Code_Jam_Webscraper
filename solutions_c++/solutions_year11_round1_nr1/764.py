#include <stdio.h>
#include <stdlib.h>
int gcd(int n,int m)
{
    if (n%m==0) return m;
    return gcd(m,n%m);
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int a[101],i,j,t,T,D,G;
    long long N;
    for (i=1;i<=100;i++)
        a[i]=100/gcd(i,100);
    a[0]=1;
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        scanf("%lld%d%d",&N,&D,&G);
        if (D<100&&G==100||D>0&&G==0)
        {
           printf("Case #%d: Broken\n",t);
           continue;
        }
        if (a[D]<=N)
           printf("Case #%d: Possible\n",t);
        else
           printf("Case #%d: Broken\n",t);
    }
    return 0;
}
