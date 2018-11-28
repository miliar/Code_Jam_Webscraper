#include <stdio.h>
#include <math.h>
const double eps = 1e-12;
int n;
double x,y,z,vx,vy,vz;
void init()
{
    double a,b,c,d,e,f;
    x=y=z=vx=vy=vz=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%lf %lf %lf %lf %lf %lf",&a,&b,&c,&d,&e,&f);
        x+=a;y+=b;z+=c;vx+=d;vy+=e;vz+=f;
    }
}
void solve()
{
    double a,b,c;
    a = vx * vx + vy * vy + vz * vz;
    b = 2*x*vx + 2*y*vy + 2*z*vz;
    c = x * x + y * y + z * z;
    if(fabs(vx*vx+vy*vy+vz*vz)<eps||a*b>=0)
    {
        printf("%.10lf %.10lf\n",sqrt(x*x+y*y+z*z)*1.0/n,0.0);
    }
    else
    {
        double xx,zz;
        xx = -b/2/a;
        zz= a*xx*xx + b*xx +c;
        if(zz<1e-12)zz = 0.0;
        zz = sqrt(zz*1.0)*1.0/n;
        printf("%.10lf %.10lf\n",zz,xx);
    }
}
int main()
{
    freopen("bribe.in","r",stdin);
    freopen("bribe.out","w",stdout);
    int Case;scanf("%d",&Case);
    for(int i = 1;i<= Case ;i++)
    {
        printf("Case #%d: ",i);
        init();
        solve();
    }
    return 0;
}
