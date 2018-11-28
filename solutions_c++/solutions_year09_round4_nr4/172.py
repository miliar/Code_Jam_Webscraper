#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

double x[6],y[6],r[6];
int n;

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int i,k,t;
    double minr;
    scanf("%d",&t);
    for(k=0;k<t;k++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%lf %lf %lf",&x[i],&y[i],&r[i]);
            x[i+3]=x[0];
            y[i+3]=y[0];
            r[i+3]=r[0];
        }
        if(n==1)
        {
            printf("Case #%d: %.6f\n",k+1,r[0]);
            continue;
        }
        if(n==2)
        {
            printf("Case #%d: %.6f\n",k+1,max(r[0],r[1]));
            continue;
        }
        minr=1e99;
        for(i=0;i<3;i++)
        {
            minr=min(minr,max(0.5*(sqrt((x[i]-x[i+1])*(x[i]-x[i+1])+(y[i]-y[i+1])*(y[i]-y[i+1]))+r[i]+r[i+1]),r[i+2]));
        }
        printf("Case #%d: %.6f\n",k+1,minr);
    }
    return 0;
}
