#include<cstdio>
#include<cmath>
#define EPS (1e-9)
using namespace std;

double f,R,t,r,g,rin;
double s,sum,a;
double xmin,xmax,ymin,ymax;

bool inside(double x, double y)
{ return (x*x+y*y<rin*rin); }

double tri(double x1, double y1, double x2, double y2, double x3, double y3)
{
  x1-=x3; y1-=y3; x2-=x3; y2-=y3;
  return fabs(0.5*(x1*y2-x2*y1));
}

double area()
{
  if(inside(xmax,ymax)) return (xmax-xmin)*(ymax-ymin);
  if(!inside(xmin,ymin)) return 0;
  double res=0;
  double x1,y1,x2,y2;
  if(inside(xmin,ymax))
  {
    x1=sqrt(rin*rin-ymax*ymax);
    y1=ymax;
    res+=tri(xmin,ymin,xmin,ymax,x1,y1);
  }
  else
  {
    x1=xmin;
    y1=sqrt(rin*rin-xmin*xmin);
  }
  if(inside(xmax,ymin))
  {
    x2=xmax;
    y2=sqrt(rin*rin-xmax*xmax);
    res+=tri(xmin,ymin,xmax,ymin,x2,y2);
  }
  else
  {
    x2=sqrt(rin*rin-ymin*ymin);
    y2=ymin;
  }
  res+=tri(xmin,ymin,x1,y1,x2,y2);
  double alfa=fabs(atan2(y1,x1)-atan2(y2,x2));
  res+=(rin*rin*0.5*alfa)-tri(x1,y1,x2,y2,0,0);
//printf("%.3lf %.3lf  %.3lf %.3lf  :  %.6lf\n",xmin,ymin,xmax,ymax,res);
  return res;
}

int main()
{
  int tt,nn;
  scanf("%d",&nn);
  for(tt=1;tt<=nn;tt++)
  {
    scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
    rin=R-t-f;
    if((2*f>g)||(rin<r)) { printf("Case #%d: 1.000000\n",tt); continue; }
    sum=0;
    a=0.5*acos(0)*R*R;
    int i=0,j=0;
    while(true)
    {
      xmin=(g+2*r)*i+(r+f);
      xmax=(g+2*r)*(i+1)-(r+f);
      ymin=(g+2*r)*j+(r+f);
      ymax=(g+2*r)*(j+1)-(r+f);
      s=area();
      sum+=s;
      if(s<EPS){
        if(j==0) break;
        j=0; i++;
      } else j++;
    }
    printf("Case #%d: %.10lf\n",tt,1-sum/a);
  }

}
