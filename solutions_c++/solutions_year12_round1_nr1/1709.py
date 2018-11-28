#include<iostream>
#include<stdio.h>
#include<memory.h>
using namespace std;

double p[10002],ans,d[10002];
int a,b;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.out","w",stdout);
    int T,cas=0,i,k;
    scanf("%d",&T);
    while(T--)
    {
        cas++;
        scanf("%d%d",&a,&b);
        for(i=1;i<=a;i++)
            scanf("%lf",&p[i]);
        d[0]=1;
        for(i=1;i<=a;i++)
            d[i]=d[i-1]*p[i];
        ans=b+2;
        for(i=0;i<=a;i++)
        {
            ans=min(ans,(b+1.0-a+i*2.0)*d[a-i]+(2*(b+1.0)-a+i*2.0)*(1-d[a-i]));
        }
        printf("Case #%d: %.6lf\n",cas,ans);
    }
    return 0;
}
