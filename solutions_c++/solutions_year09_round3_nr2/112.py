#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int n;
const double eps = 1e-10;
double x,y,z,vx,vy,vz;
double ans,at;
double ax,ay,az,avx,avy,avz;
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T,K;
    K=1;
    scanf("%d",&T);
    int i,j,k;
    while(T--)
    {
        scanf("%d",&n);
        ax=ay=az=0;
        avx=avy=avz=0;
        for(i=0;i<n;i++)
        {
            scanf("%lf%lf%lf%lf%lf%lf",&x,&y,&z,&vx,&vy,&vz);
            ax+=x;
            ay+=y;
            az+=z;
            avx+=vx;
            avy+=vy;
            avz+=vz;
        }
        double a,b,c,d;
        a=(avx*avx+avy*avy+avz*avz);
        b=2*(avx*ax+avy*ay+avz*az);
        c=ax*ax+ay*ay+az*az;
            if(fabs(a)<eps||a>=0&&b>=0||a<=0&&b<=0)
            {
                ans = sqrt(c)/n;
                at = 0.;
            }
            else
            {

                at = -b/(2*a);
                ans = a*at*at + b*at + c;
                if(ans<eps)ans =0.;
               // printf("%lf %lf\n",ans,at);
                ans = sqrt(ans)/n;
                //printf("X %lf\n",sqrt(ans));
            }
            //printf("%d : %lf %lf\n",i,tmp,tp);
//            if(i==0||tmp<ans-eps||fabs(tmp-ans)<eps&&tp<at)
//            {
//                ans = tmp;
//                at = tp;
//            }
        printf("Case #%d: %lf %lf\n",K++,ans,at);
    }
    return 0;
}
