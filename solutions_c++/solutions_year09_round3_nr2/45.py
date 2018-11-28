#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

typedef __int64 lint;

int main()
  {
  double eps=(1e-12);
  int T;

  scanf("%d ",&T);
  for(int t=0;t<T;++t)
    {
    int N;
    scanf("%d ",&N);
    double sx=0,sy=0,sz=0,svx=0,svy=0,svz=0;
    for(int i=0;i<N;++i)
      {
      double x,y,z, vx,vy,vz;
      //cin >> x >> y >> z >> vx >> vy >> vz;
      scanf("%lf %lf %lf %lf %lf %lf ",&x,&y,&z,&vx,&vy,&vz);
      sx+=x;
      sy+=y;
      sz+=z;

      svx+=vx;
      svy+=vy;
      svz+=vz;
      }

    sx/=N;sy/=N;sz/=N;
    svx/=N;svy/=N;svz/=N;

    double time=0;
    if (fabs(svx)<eps && fabs(svy)<eps && fabs(svz)<eps)
      time=0;
    else
      {
      time=-(sx*svx+sy*svy+sz*svz)/(svx*svx+svy*svy+svz*svz);
      if (time<0) time=0;
      }

    double x1=sx+svx*time;
    double y1=sy+svy*time;
    double z1=sz+svz*time;

    double d=sqrt(x1*x1+y1*y1+z1*z1);

    printf("Case #%d: %.10f %.10f\n",t+1,d,time);
    }

  return 0;
  }