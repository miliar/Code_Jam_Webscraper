#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

#define Max 5010
#define eps 1e-8

int main(int argc, char *argv[])
{   
    int t,o;
   // freopen("E:/in.txt","r",stdin);
 //freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);
    for(o=1;o<=t;o++)
    {
        int x[Max],y[Max],z[Max],vx[Max],vy[Max],vz[Max];
        int i,j,k,n;
        scanf("%d",&n);
        for(i=1;i<=n;i++) scanf("%d%d%d%d%d%d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
        int a1=0,a2=0,a3=0,b1=0,b2=0,b3=0;
        for(i=1;i<=n;i++) { a1 += x[i]; b1 += vx[i]; }
        for(i=1;i<=n;i++) { a2 += y[i]; b2 += vy[i]; }
        for(i=1;i<=n;i++) { a3 += z[i]; b3 += vz[i]; }
        double a,b,c;
        a = 1.0*(b1*b1+b2*b2+b3*b3)/(n*n);
        b = 2.0*(a1*b1+a2*b2+a3*b3)/(n*n);
        c = 1.0*(a1*a1+a2*a2+a3*a3)/(n*n);
        //cout<<a<<' '<<b<<' '<<c<<endl;
        double time,dis;
        if(fabs(a-0.0) < eps) time = 0.0;
        else  time = -b/(2.0*a);
        if(time < 0.0) time = 0.0;
        dis = a*time*time+b*time+c;
        printf("Case #%d: %.8f %.8f\n",o,sqrt(fabs(dis)),fabs(time));
    }
    return EXIT_SUCCESS;
}
