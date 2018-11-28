#include <cstdio>
#include <cmath>
using namespace std;

int xx[4],yy[4],rr[4];
int n,run;

double sqr(double a)
{
       return a*a;
}

double max(double a, double b)
{
       return (a>b)?a:b;
}

int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&run);
    for (int r=1;r<=run;r++)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
             scanf("%d%d%d",&xx[i],&yy[i],&rr[i]);
        printf("Case #%d: ",r);
        if (n==1) printf("%d.000000\n",rr[1]);
        else
        if (n==2) printf("%.6lf\n",max(rr[1],rr[2]));
        else
        {
            double ans=99999999;
            ans<?=max(double(sqrt(sqr(xx[1]-xx[2])+sqr(yy[1]-yy[2]))+rr[1]+rr[2])/2,rr[3]);
            ans<?=max(double(sqrt(sqr(xx[1]-xx[3])+sqr(yy[1]-yy[3]))+rr[1]+rr[3])/2,rr[2]);            
            ans<?=max(double(sqrt(sqr(xx[2]-xx[3])+sqr(yy[2]-yy[3]))+rr[2]+rr[3])/2,rr[1]);
            printf("%.6lf\n",ans);
        }
    }
    fclose(stdout);
    return 0;
}
