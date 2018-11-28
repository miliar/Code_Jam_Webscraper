#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
int sp[1000003];
int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("A-large (2).txt","w",stdout);
    int test,cas,x,s,r,n,i,b,e,w,j;
    double sum,d,t;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
        for (i=0;i<=x;i++) sp[i]=0;
        for (i=0;i<n;i++)
        {
            scanf("%d%d%d",&b,&e,&w);
            for (j=b+1;j<=e;j++) sp[j]=w;
        }
        sort(sp+1,sp+x+1);
        sum=0.0;
        for (i=1;i<=x;i++)
        {
            if (fabs(t)>1e-6)
            {
                if (t>=1.0/(sp[i]+r))
                {
                    t-=1.0/(sp[i]+r);
                    sum+=1.0/(sp[i]+r);
                }
                else
                {
                    d=(sp[i]*1.0+r)*t;
                    sum+=t+(1.0-d)/(sp[i]+s);
                    t=0.0;
                }
            }
            else sum+=1.0/(sp[i]+s);
            //printf("%.10lf\n",sum);
        }
        printf("Case #%d: %.10lf\n",cas,sum);
    }
    return 0;
}
