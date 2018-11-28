#include<stdio.h>
#include<math.h>


double x[10],y[10],r[10];

double dis(int i, int j)
{
    return sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]));
}

int main()
{
    freopen("D1.in","r",stdin);
    freopen("D1.out","w",stdout);
    int t,i;
    scanf("%d",&t);

    for(int cs=1;cs<=t;cs++)
    {
        int n;
        scanf("%d",&n);
        double ans=0;
        for(i=0;i<n;i++)
            scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);
        if(n==1)
            ans=r[0];
        else if(n==2)
        {
            ans=r[0];
            if(ans<r[1])
                ans=r[1];
        }
        else
        {
            ans=1E10;

            double ans2;
            ans2=0;

            for(i=0;i<3;i++)
            {
                ans2=(dis((i+1)%3,(i+2)%3)+r[(i+1)%3]+r[(i+2)%3])/2;
                if(ans2<r[i])
                    ans2=r[i];
                if(ans2<ans)
                    ans=ans2;
            }
        }

        printf("Case #%d: %.9lf\n",cs,ans);
    }

    return 0;
}
