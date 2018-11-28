#include <cstdio>
#include <cmath>
#include <string>
#include <stdlib.h>
#include <iostream>
using namespace std;

const double eps = 1e-10;
const double delta = 1e-7;
const double pi = acos(-1);
inline double min(double a,double b){return a<b?a:b;}
inline double max(double a,double b){return a>b?a:b;}
const long N =70000,M=1005;
const double INF= 1e10;
long n,K=1;
double f,r,R,t,g;
inline void swap(double &a,double &b){double tt;tt=a,a=b,b=tt;}
double dist(double sx,double sy,double tx,double ty)
{return sqrt((sx-tx)*(sx-tx)+(sy-ty)*(sy-ty));}
void Init()
{
    scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
    g-=2*f;
    r+=f;
    t+=f;
}
void Solve()
{
    double s1,s2,ty,tx,dd,ar;
    double X,Y,X1,X2,Y1,Y2,ans;
    printf("Case #%ld: ",K++);
    if(g<=0){printf("1.000000\n");return;}
    s1=(R)*(R)*pi;
  //  printf("R: %lf g:%lf r:%lf\n",R,g,r);
  //  printf("t: %lf , f: %lf\n",t,f);
    R-=t;
    s2=0;
    X=r;
   // printf("R: %lf %lf %lf\n",R,g,r);
    long f1,f2;
    for(X=r;X<R;X+=(g+r*2))
    {
        ty=sqrt(R*R-X*X);
        for(Y=r;Y<R;Y+=(g+r*2))
        {
         //   printf("%lf %lf : %lf %lf\n",X,Y,X+g,Y+g);
            tx=sqrt(R*R-Y*Y);
            if(dist(X,Y,0,0)>R)break;
            if(dist(X+g,Y+g,0,0)<=R){s2+=g*g;continue;}
        //    if(dist(X+g,Y,0,0)>=R)f1=1;
         //   else f1=2;
         //   if(dist(X,Y+g,0,0)>=R)
            if(X+g<=tx)
            {
               // printf("1 : \n");
                if(Y+g<=ty)
                {
                    Y1=Y+g;X1=sqrt(R*R-Y1*Y1);
                    X2=X+g;Y2=sqrt(R*R-X2*X2);
                    s2+=g*g;
                    s2-=(Y1-Y2)*(X2-X1)/2;
                    dd=dist(X1,Y1,X2,Y2);
                    ar=asin(dd/(2.0*R));
                    s2+=R*R*ar-dd*R*cos(ar)/2;
                }
                else
                {
                    X1=X;X2=X+g;
                    Y1=sqrt(R*R-X1*X1);
                    Y2=sqrt(R*R-X2*X2);
                    s2+=g*(Y1-Y+Y2-Y)/2;
                    dd=dist(X1,Y1,X2,Y2);
                    ar=asin(dd/(2.0*R));
                    s2+=R*R*ar-dd*R*cos(ar)/2;
                }
            }
            else
            {
              //  printf("2 : \n");
                if(Y+g<=ty)
                {
                    Y1=Y+g;Y2=Y;
                    X1=sqrt(R*R-Y1*Y1);
                    X2=sqrt(R*R-Y2*Y2);
                    s2+=g*(X1-X+X2-X)/2;
                    dd=dist(X1,Y1,X2,Y2);
                    ar=asin(dd/(2.0*R));
                    s2+=R*R*ar-dd*R*cos(ar)/2;
                }
                else
                {
                    X1=X;X2=sqrt(R*R-Y*Y);
                    Y1=sqrt(R*R-X*X);
                    Y2=sqrt(R*R-X2*X2);
                   // printf("%lf %lf , %lf %lf\n",X1,Y1,X2,Y2);
                    s2+=(Y1-Y)*(X2-X)/2;
                //    printf("s2 1 : %lf\n",s2);
                    dd=dist(X1,Y1,X2,Y2);
                    ar=asin(dd/(2.0*R));
                    s2+=R*R*ar-dd*R*cos(ar)/2;
                 //   printf("s2 2 : %lf : %lf %lf\n",s2,R*R*ar/2,dd*R*cos(ar)/2);
                }
            }
        }
    }

    ans=(s1-s2*4)/s1;
    printf("%.6lf\n",ans);

}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long T;scanf("%ld",&T);

    while(T--)
    {
        Init();
        Solve();
    }
    return 0;
}
