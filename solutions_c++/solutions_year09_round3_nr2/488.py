#include <cstdio>
#include <cmath>
using namespace std;

int Vx, Vy, Vz, X, Y, Z;
int zestawy, n;
long double epsilon=0.000000001L;

long double sqr(long double x)
{return (long double)(x*x);}

long double dist(long double t)
{
  return sqrt(sqr((long double)X+Vx*t)+sqr((long double)Y+Vy*t)+sqr((long double)Z+Vz*t));
}

int main()
{
  scanf("%d", &zestawy);
  for(int zes=0; zes<zestawy; ++zes)
  {
    scanf("%d", &n);
    Vx=0; Vy=0; Vz=0; X=0; Y=0; Z=0;
    int x, y, z, vx, vy, vz;
    for(int i=0; i<n; ++i)
    {
      scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
      X+=x; Y+=y; Z+=z;
      Vx+=vx; Vy+=vy; Vz+=vz;
    }
    long double ta=0., tb=20000., t=10000.;
    if(dist(ta)<=dist(ta+epsilon))
      {printf("Case #%d: %.8Lf %.8Lf\n", zes+1, dist(0.)/(long double)n, 0.); continue;}
    while(2.*epsilon<tb-ta)
    {
      t=(ta+tb)/2.0;
      if(dist(t)>=dist(t+epsilon)) ta=t;
      else tb=t;
    }
    printf("Case #%d: %.8Lf %.8Lf\n", zes+1, dist(t)/(long double)n, t);
  }
  return 0;
}
