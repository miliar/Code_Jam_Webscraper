#include <cstdio>
#include <cmath>
using namespace std;

double sqr(double a) { return a*a;};

int main()
{
        freopen("out.put","w",stdout);
        int ntest;
        double x[600],y[600],z[600],vx[600],vy[600],vz[600];
        int i;
        scanf("%d",&ntest);

        for(int test = 0;test < ntest;test++)
        {
                int n;
                scanf("%d",&n);
                for(i=0;i<n;i++)
                {
                        scanf("%lf%lf%lf%lf%lf%lf",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
                }

                double sx=0,sy=0,sz=0,svx=0,svy=0,svz=0;
                for(i=0;i<n;i++)
                {
                                sx += x[i];
                                sy += y[i];
                                sz += z[i];
                                svx += vx[i];
                                svy += vy[i];
                                svz += vz[i];
                } 
                double t;
                if(fabs(svx*svx + svy*svy + svz*svz) < 1e-6) t = 0;
                else t = -1.0*(sx*svx + sy*svy + sz*svz)/(svx*svx + svy*svy + svz*svz);
                
                if(t<=0) t = 0;

                double d = sqrt(sqr((sx + t * svx)/n) + sqr((sy + t * svy)/n) + sqr((sz + t * svz)/n)); 
                
                printf("Case #%d: %lf %lf\n",test+1,d,t);
        }


        
                                
        return 0;
}