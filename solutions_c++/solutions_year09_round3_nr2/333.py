#include <iostream>
#include <math.h>
#include <ctime>
#include <cstdlib>
struct Point{
  int x,y,z,vx,vy,vz;
};
Point v[600];
int T,N;
double xx = 0.0f,yy = 0.0f,zz = 0.0f;
double vx = 0.0f,vy = 0.0f,vz = 0.0f;
void doit() {
  xx = 0.0f,yy = 0.0f,zz = 0.0f;
  vx = 0.0f,vy = 0.0f,vz = 0.0f;
  for (int i = 0;i<N;++i) {
    xx+=v[i].x;
    yy+=v[i].y;
    zz+=v[i].z;
    vx+=v[i].vx;
    vy+=v[i].vy;
    vz+=v[i].vz;
  }
  double a = vx*vx+vy*vy+vz*vz;
  double b = (vx*xx+vy*yy+vz*zz)*2;
  double t;
  if (fabs(a)<1e-8) t = 0.0f; else t = -b/2/a;
  if (fabs(t)<1e-8) t = 0.0f;
  if (t<0) t = 0.0f;
  double sx = xx+t*vx,sy = yy+t*vy,sz = zz+t*vz;
  double ans = sqrt(sx*sx+sy*sy+sz*sz+1e-12)/N;
  if (fabs(ans)<1e-8) ans = 0.0f;
  printf("%.8lf %.8lf\n",ans,t);
}

int main(void){ 
  freopen("fdin.txt","r",stdin);
  freopen("fdout.txt","w",stdout);
  scanf("%d",&T);
  int cas = 1;
  while (T--) {
    printf("Case #%d: ",cas);
    scanf("%d",&N);
    for (int i = 0;i<N;++i)
      scanf("%d%d%d%d%d%d",&v[i].x,&v[i].y,&v[i].z,&v[i].vx,&v[i].vy,&v[i].vz);
    doit();
    ++cas;
  }
  return 0;
}