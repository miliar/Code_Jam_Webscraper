#include <iostream>
#include <vector>
#include <memory.h>
#include <math.h>
using namespace std;

#define MAX 501
#define epf 1e-5
#define EPF 0.00001
#define INF 100000000000
#define MINF -1000000000

double getd(double x,double y,double z)
{
    double total=x*x+y*y+z*z;

    return (double)sqrt(total);

}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

//freopen("B-small.out","w",stdout);
    int t;
    cin>>t;
    for (int g=1;g<=t;++g)
    {
        int n;
        cin>>n;
        int x[MAX],y[MAX],z[MAX],vx[MAX],vy[MAX],vz[MAX];
        for (int a=0;a<n;++a)
        {
            cin>>x[a]>>y[a]>>z[a]>>vx[a]>>vy[a]>>vz[a];
        }
        double dt=10000000;
        double time=10000000;
        double newx[MAX],newy[MAX],newz[MAX];


        int VX=0,VY=0,VZ=0,X=0,Y=0,Z=0;

        for (int b=0;b<n;++b)
        {
            VX+=vx[b];
            VY+=vy[b];
            VZ+=vz[b];
            X+=x[b];
            Y+=y[b];
            Z+=z[b];
        }

        long long rhs=(X*VX) + (Y*VY) + (Z*VZ);
        long long lhs = (VX*VX)+(VY*VY)+(VZ*VZ);
        double mint=(double)rhs/lhs;
        mint*=-1;
        if (mint<=0.0 or mint==(double)-0.0 or isnan(mint) )
        {
            mint=0.0;
        }

        double d1=X+((double)mint*VX);
        double d2=Y+((double)mint*VY);
        double d3=Z+((double)mint*VZ);
        d1=(double)d1/n;
        d2=(double)d2/n;
        d3=(double)d3/n;
        d1=d1*d1;
        d2=d2*d2;
        d3=d3*d3;
        double mind=sqrt(d1+d2+d3);
        printf("Case #%d: %0.8f %0.8f\n",g,mind,mint);

    }
    return 0;
}

