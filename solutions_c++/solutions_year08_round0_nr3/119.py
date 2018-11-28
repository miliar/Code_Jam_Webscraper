#include <iostream>
#include <cmath>
using namespace std;
const double pre=1e-7;
const double pi=3.14159265358;
double f,R,t,r,g,ans;
double r1,R1,g1;
int n;
double dis(double x,double y)
{
    return x*x+y*y;
}
int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("C-large.out","w",stdout);
    int i,j,k,l;
    double x,y,x1,y1,x2,y2;
    scanf("%d",&n);
    for (k=1;k<=n;k++)
    {
        ans=0;
        scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
        R1=R-t-f;
        g1=g-2*f;
        r1=f+r;
        if (g1<=0)
            ans=1;
        else
        {
            x=r1;
            y=r1;
            while ( dis( x , y )<=R1*R1 )
            {
                if (dis( x+g1 , y+g1 )<=R1*R1)
                    ans+=g1*g1;
                else 
                {
                     if ( dis(x+g1 ,y) <= R1*R1)
                     {
                          if (dis (x, y+g1)<=R1*R1)
                          {
                              y1=y+g1; x1=sqrt(R1*R1-y1*y1);
                              x2=x+g1; y2=sqrt(R1*R1-x2*x2);
                              ans+=g1*g1-(x2-x1)*(y1-y2)/2;
                              ans+=(atan(y1/x1)-atan(y2/x2))/2*R1*R1;
                              ans-=((x1*y1)+(x2-x1)*(y1+y2)-(x2*y2))/2;
                          }
                          else
                          {
                              x1=x; y1=sqrt(R1*R1-x1*x1);
                              x2=x+g1; y2=sqrt(R1*R1-x2*x2);
                              ans+=g1*(y1+y2-2*y)/2;
                              ans+=(atan(y1/x1)-atan(y2/x2))/2*R1*R1;
                              ans-=((x1*y1)+(x2-x1)*(y1+y2)-(x2*y2))/2;
                          }
                     }
                     else if (dis(x, y+g1)<=R1*R1)
                     {
                          y1=y+g1; x1=sqrt(R1*R1-y1*y1);
                          y2=y; x2=sqrt(R1*R1-y2*y2);
                          ans+=g1*(x1+x2-2*x)/2;
                          ans+=(atan(y1/x1)-atan(y2/x2))/2*R1*R1;
                          ans-=((x1*y1)+(x2-x1)*(y1+y2)-(x2*y2))/2;
                     }
                     else 
                     {
                         x1=x; y1=sqrt(R1*R1-x1*x1);
                         y2=y; x2=sqrt(R1*R1-y2*y2);
                         ans+=(x2-x1)*(y1-y2)/2;
                         ans+=(atan(y1/x1)-atan(y2/x2))/2*R1*R1;
                         ans-=((x1*y1)+(x2-x1)*(y1+y2)-(x2*y2))/2;
                     }
                }
                y=y+g1+r1*2;
                if (dis( x, y ) >R1*R1)
                {
                    y=r1;
                    x=x+g1+r1*2;
                }
                //cout<<x<<' '<<y<<endl;
            }
            ans=1-(ans*4)/(pi*(R)*(R));
        }
        printf("Case #%d: %.6lf\n",k,ans);
    }
    return 0;
}
