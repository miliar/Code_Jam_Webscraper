#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
  int T;
  cin>>T;
  for(int t=1;t<=T;t++) {
    int N;
    cin>>N;
    long int x,vx,y,vy,z,vz;
    x=vx=y=vy=z=vz=0;
    for(int i=0;i<N;i++) {
      int a,b,c,d,e,f;
      cin>>a>>b>>c>>d>>e>>f;
      x+=a;
      y+=b;
      z+=c;
      vx+=d;
      vy+=e;
      vz+=f;
    }
    double tmin = 0.0;
    if (vx*vx + vy*vy+vz*vz > 0.0) {
      tmin = -(double)(x*vx+y*vy+z*vz)/(vx*vx + vy*vy+vz*vz);
    }
    if (tmin <= 0.0) tmin=0.0;
    double dmin = sqrt((x+tmin*vx)*(x+tmin*vx) + (y+tmin*vy)*(y+tmin*vy) + (z+tmin*vz)*(z+tmin*vz))/N;
    printf("Case #%d: %0.08lf %0.08lf\n", t, dmin, tmin);
  }
  return 0;
}
