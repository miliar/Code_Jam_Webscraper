#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main() {
  int tt;
  scanf("%d", &tt);
  for(int iii=1; iii<=tt; iii++) {
    int n;
    scanf("%d", &n);
    vector<int> x, y, z, vx, vy, vz;
    for(int i=0; i<n; i++) {
      int x_, y_, z_, vx_, vy_, vz_;
      scanf("%d %d %d %d %d %d", &x_, &y_, &z_, &vx_, &vy_, &vz_);
      x.push_back(x_);
      y.push_back(y_);
      z.push_back(z_);
      vx.push_back(vx_);
      vy.push_back(vy_);
      vz.push_back(vz_);
    }

    double bx=0.0;
    double by=0.0;
    double bz=0.0;

    double bvx=0.0;
    double bvy=0.0;
    double bvz=0.0;

    for(int i=0; i<n; i++) {
      bx+=x[i];
      by+=y[i];
      bz+=z[i];
      bvx+=vx[i];
      bvy+=vy[i];
      bvz+=vz[i];
    }
    bx/=(double)n;
    by/=(double)n;
    bz/=(double)n;
    bvx/=(double)n;
    bvy/=(double)n;
    bvz/=(double)n;


    double t=-(bvx*bx+bvy*by+bvz*bz)/(bvx*bvx+bvy*bvy+bvz*bvz);
    if((bvx*bvx+bvy*bvy+bvz*bvz)<=0.00001 || t<0.0) t=0.0;
    double d=sqrt((bx+bvx*t)*(bx+bvx*t)+(by+bvy*t)*(by+bvy*t)+(bz+bvz*t)*(bz+bvz*t));

    cout<<"Case #"<<iii<<": "<<d<<" "<<t<<endl;




  }

  return 0;
}

