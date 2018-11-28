#include <iostream>
#include <math.h>
double p,l,c,i,j;
int t,cc,ans;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&t);
    for (cc=1;cc<=t;cc++)
    {
        scanf("%lf %lf %lf",&l,&p,&c);
        i=p/l;
        if (i<=c) ans=0;
        else
        {
        ans=0;
        while (i>c+1e-12)
        {
              i=pow(i,0.5);
              ans++;
        }
        }
        printf("Case #%d: %d\n",cc,ans);
    }
}
