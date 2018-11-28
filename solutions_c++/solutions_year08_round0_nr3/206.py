#include <iostream>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

const double PI=acos(-1.0);
const double eps=1e-8;

int testCase,testNum;

double f,R,t,r,g;

double g2,r2,R2;

double holeArea,hitArea,totalArea;

inline double sqr (double x)
{
  return x*x;
}

double calcArea2 (double x0,double y0)
{
  double x2=sqrt(sqr(R2)-sqr(y0))-x0;
  double y2=sqrt(sqr(R2)-sqr(x0))-y0;
  double th=PI/2-asin(y0/R2)-asin(x0/R2);
  double r1=0.5*th*sqr(R2);
  double r2=0.5*x2*y0;
  double r3=0.5*y2*x0;
  return r1-r2-r3;
}

double calcArea (double x0,double y0)
{
  double x1=x0+g2;
  double y1=y0+g2;
  if (sqr(x0)+sqr(y0)>sqr(R2-eps))
    return 0.0;
  if (sqr(x1)+sqr(y1)<sqr(R2+eps))
    return sqr(g2);
  if (sqr(x0)+sqr(y1)>sqr(R2-eps))
    if (sqr(x1)+sqr(y0)>sqr(R2-eps))
      return calcArea2(x0,y0);
    else
    {
      double dy=sqrt(sqr(R2)-sqr(x1))-y0;
      return calcArea2(x0,y0+dy)+dy*g2;
    }
  else
    if (sqr(x1)+sqr(y0)>sqr(R2-eps))
    {
      double dx=sqrt(sqr(R2)-sqr(y1))-x0; 
      return calcArea2(x0+dx,y0)+dx*g2;
    }
    else
    {
      double dy=sqrt(sqr(R2)-sqr(x1))-y0;
      double dx=sqrt(sqr(R2)-sqr(y1))-x0;
      return calcArea2(x0+dx,y0+dy)+dx*g2+dy*g2-dx*dy;
    }
}

int main()
{
  cout<<setiosflags(ios::fixed)<<setprecision(6);
  cin>>testNum;
  for (testCase=1;testCase<=testNum;++testCase)
  {
    cin>>f>>R>>t>>r>>g;
    r2=r+f;
    g2=g-2*f;
    R2=R-t-f;
    double ans;
    if (g2<eps || R2<eps)
      ans=1.0;
    else
    {
      holeArea=0.0;
      for (double x=r2;x<R2;x+=g2+2*r2)
        for (double y=r2;y<R2;y+=g2+2*r2)
          holeArea+=calcArea(x,y);
      holeArea*=4;
      totalArea=PI*sqr(R);
      hitArea=totalArea-holeArea;
      ans=hitArea/totalArea;
    }
    cout<<"Case #"<<testCase<<": ";
    cout<<ans<<endl;
  }
}
