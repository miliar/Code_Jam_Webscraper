#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

main()
{
   int num;
   scanf("%d",&num);
   for(int q=0;q < num; q++)
   {
     double a=0.0,b=0.0,c=0.0,d=0.0,e=0.0,f=0.0;
     
     int n;
     scanf("%d",&n);
     for(int i=0; i < n; i++)
     {
      int x,y,z,vx,vy,vz;
      scanf("%d %d %d %d %d %d",&x,&y,&z,&vx,&vy,&vz);
      a+=x;b+=vx;
      c+=y;d+=vy;
      e+=z;f+=vz;
     }   
     a=a/n;
     b=b/n;
     c=c/n;
     d=d/n;
     e=e/n;
     	f=f/n;
     
     double denomi=b*b+d*d+f*f;
     double rt=0.0;
     
     if(denomi != 0.0)
     rt=-(a*b+c*d+e*f)/denomi;
    
    	if(rt<0.0) rt=0.0;
    	  
        
     double rx=a+b*rt;
     double ry=c+d*rt;
     double rz=e+f*rt;
     double dist=sqrt(rx*rx + ry*ry + rz*rz);
     printf("Case #%d: %.8lf %.8lf\n",q+1,dist,rt);
  
   }

}
