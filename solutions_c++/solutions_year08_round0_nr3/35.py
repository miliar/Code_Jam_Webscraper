#include <cmath>
#include <iostream>
using namespace std;

inline double ad(double x) { return(0.5*x*sqrt(1-x*x) + 0.5*asin(x)); }

double sq(double l,double x,double y)
{
  double x1,x2;

  if (x>y) return sq(l,y,x);
  if ((x+l)*(x+l)+(y+l)*(y+l) <= 1) return l*l;

  // Critical range of x
  if ((x+l)*(x+l)+y*y > 1) x2 = sqrt(1-y*y); else x2 = x+l;
  if (x*x+(y+l)*(y+l) < 1) x1 = sqrt(1-(y+l)*(y+l)); else x1 = x;

  double t=ad(x2)-ad(x1)-(x2-x1)*y + l*(x1-x);

  if (0)
  {
  int N=10000; double lb=0, ub=0, dx=(x2-x1)/N;
  double y1=sqrt(1-x1*x1)-y; if (y1>l) y1=l;
  double y2=sqrt(1-x2*x2)-y; if (y2>l) y2=l;
  for(int i=0;i<N;i++)
  { 
    double xi=x1+dx*i; double yi=sqrt(1-xi*xi)-y; if (yi>l) yi=l;
    lb += yi; ub += yi;
  }

  lb-=y1/2; lb+=y2/2;

  lb*=dx; ub*=dx; lb+=l*(x1-x); ub+=l*(x1-x);

  if (t <= lb || t >= ub)  {fprintf(stderr,"Warning: instability at %lg,%lg: %lg <= %lg <= %lg\n",x,y,lb,t,ub); }
  }

  return t;
}

double doit(double f,double R,double t,double r,double g)
{
  // Remap to eroded grid
  double Re=R-t-f;
  double se=g+2*r;
  double ge=g-2*f;
  double re=r+f;

  if (Re<=0) return 1;
  if (ge<=0) return 1;

  // normalize
  se /= Re; ge /= Re; re /= Re; R /= Re; Re=1.0;

  double H=0.0;
  int q=(Re-re)/se;

  for(int i=0;i<=q;i++) for(int j=0;j<=q;j++)
  {
    double x=re+i*se,y=re+j*se;
    if (x*x+y*y > Re*Re) continue;
    H += sq(ge,x,y);
  }

  return 1.0 - 4.0*H/(M_PI*R*R);
}

int main()
{
int n;
double f,R,t,r,g;
double P;

scanf("%d",&n);

for(int loop=1;loop<=n;loop++)
{
  cin >> f >> R >> t >> r >> g;
  P = doit(f,R,t,r,g);
  printf("Case #%d: %1.6lf\n",loop,P);
}

}
