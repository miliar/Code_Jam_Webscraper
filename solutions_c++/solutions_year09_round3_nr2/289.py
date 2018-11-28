#include<iostream>
#include<cmath>
using namespace std;
const double EPS=1e-8;

struct Point3D
{
   double x,y,z;
}O,XX;
struct Line3D{
  Point3D a,b;
}L;
inline double sqrlen(const Point3D &p)
{  return p.x*p.x+p.y*p.y+p.z*p.z;
}
inline Point3D subt(const Point3D &u,const Point3D &v)
{
   Point3D ret;
   ret.x = u.x - v.x;
   ret.y = u.y - v.y;
   ret.z = u.z - v.z;
   return ret;
}
inline double dmult(const Point3D &u,const Point3D &v)
{
   return u.x*v.x+u.y*v.y+u.z*v.z;

}
Point3D ptoline(const Point3D &p,const Line3D &l)
{
   Point3D ab = subt(l.b,l.a);
   double t= -dmult(subt(p,l.a),ab)/sqrlen(ab);
   ab.x*=t;
   ab.y*=t;
   ab.z*=t;
   return subt(l.a,ab);

}
double VX,VY,VZ;
double X,Y,Z,ax,ay,az,avx,avy,avz,time1;
double gao(void)
{  double ret=0;
   
   if(VX!=0)
     return (XX.x-L.a.x)/VX;
    if(VY!=0)
     return (XX.y-L.a.y)/VY;
      if(VZ!=0)
     return (XX.z-L.a.z)/VZ; 
   return -1;
}
int main()
{
  
  O.x=O.y=O.z=0; 
  int t,T,N,i;
  scanf("%d",&T);
   for(t=1;t<=T;++t)
   {
      scanf("%d",&N);
      X=Y=Z=VX=VY=VZ=0;
     for(i=0;i<N;++i)
       { scanf("%lf%lf%lf%lf%lf%lf",&ax,&ay,&az,&avx,&avy,&avz);
         X+=ax;
         Y+=ay;
         Z+=az;
         VX+=avx;
         VY+=avy;
         VZ+=avz;
        }
        X/=N;
        Y/=N;
        Z/=N;
        VX/=N;
        VY/=N;
        VZ/=N;
       // printf("%lf,%lf,%lf %lf,%lf,%lf\n",X,Y,Z,VX,VY,VZ);
        L.a.x=X;
        L.a.y=Y;
        L.a.z=Z;
        L.b.x=X+VX;
        L.b.y=Y+VY;
        L.b.z=Z+VZ;
        XX=ptoline(O,L);
        time1=gao();
        if(time1>=0)
          printf("Case #%d: %.8lf %.8lf\n",t,sqrt(sqrlen(XX)),time1);
        else
          printf("Case #%d: %.8lf %.8lf\n",t,sqrt(sqrlen(subt(L.a,O))),0.0);
        

   }
}
