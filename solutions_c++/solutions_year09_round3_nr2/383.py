#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>
#include <math.h>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)

using namespace std;

int main(){
  int CN;
  cin >> CN;
  cout << fixed << setprecision(8);
  For1(CI,CN){
    int N;
    cin >> N;
    double x,y,z,vx,vy,vz;
    double tx,ty,tz,tvx,tvy,tvz;
    x=y=z=vx=vy=vz=0.0;
    For(i,N){
      cin >> tx >> ty >> tz >> tvx >> tvy >> tvz;
      x+=tx;
      y+=ty;
      z+=tz;
      vx+=tvx;
      vy+=tvy;
      vz+=tvz;
    }
    x/=N;
    y/=N;
    z/=N;
    vx/=N;
    vy/=N;
    vz/=N;

    double v2= (vx*vx+vy*vy+vz*vz);
    double t;
    if(v2>0.0){
     t=-(x*vx+y*vy+z*vz)/v2;
     if(t<0.0)
       t=0.0;
    }
    else{
      t=0.0;
    }

    double xx,yy,zz;
    xx=x+t*vx;
    yy=y+t*vy;
    zz=z+t*vz;
    double d=sqrt(xx*xx+yy*yy+zz*zz);

    d=fabs(d);
    t=fabs(t);

    cout << "Case #" << CI << ": " << d << " " << t << endl;
  }
}
