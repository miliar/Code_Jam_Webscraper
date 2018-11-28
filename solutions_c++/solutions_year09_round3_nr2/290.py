#include <cstdio>
#include <cmath>
using namespace std;

main()
{
   int T;
   scanf("%d",&T);
   for(int t=0;t < T; t++)
   {
     double a=0.0,b=0.0,c=0.0,d=0.0,e=0.0,f=0.0;
     int N;
     scanf("%d",&N);
     for(int i=0; i < N; i++)
     {
      int x,y,z,vx,vy,vz;
      scanf("%d %d %d %d %d %d",&x,&y,&z,&vx,&vy,&vz);
      a+=x;b+=vx;
      c+=y;d+=vy;
      e+=z;f+=vz;
     }   
     a/=N;b/=N;c/=N;d/=N;e/=N;f/=N;
     double ot=0.0;
     double den=b*b+d*d+f*f;
     if(den != 0.0)
     ot=-(a*b+c*d+e*f)/den;
     
     ot= ot >= 0.0 ? ot : 0.0;
     
     double ox=a+b*ot,oy=c+d*ot,oz=e+f*ot;
     double dist=sqrt(ox*ox + oy*oy + oz*oz);
     printf("Case #%d: %.8lf %.8lf\n",t+1,dist,ot);
  
   }

}
