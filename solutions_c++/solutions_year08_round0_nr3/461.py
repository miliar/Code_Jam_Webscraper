#include<stdio.h>
#include<vector>
#include<stdlib.h>
#include<math.h>

int main(void)
{
 int n=0;
 FILE *ff=fopen("C-small.in","r");
 fscanf(ff,"%d",&n);
 for(int i=0;i<n;i++)
 {
  double f,R,t,r,g,area=0;
  fscanf(ff,"%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
  double multiple=g+2*r;
  double increment=R/60000000.0;
  double innerInnerRadius=R-t-f;
  double iirSquared=innerInnerRadius*innerInnerRadius;
  double boxNum=0;
  double rightLimit=r+g+boxNum*multiple-f;
  double leftLimit= r+boxNum*multiple+f;
  if(innerInnerRadius>0)
  {
  for(double x=r+f;x<=(R-t-f);x+=increment)
  {
   if(x<rightLimit)
   {
    double topSquared=iirSquared-x*x;
    if(topSquared>0)
    {
     double top=sqrt(topSquared);
     double vertBoxNum=floor(top/multiple);
     double topLength=(top-(r+vertBoxNum*multiple+f));
     double nextX=x+increment;
     double xDist=increment;
     if(topLength>=(g-2*f))
     {
      area+=xDist*(vertBoxNum+1)*(g-2*f);
      continue;
     }
     double nextTopSquared=(iirSquared-nextX*nextX);
     if(topLength>0&&nextTopSquared>0)
     {
      double nextTop=sqrt(nextTopSquared);
      area+=0.5*xDist*(2*topLength-(top-nextTop))+xDist*vertBoxNum*(g-2*f);
     }
     else
      area+=xDist*vertBoxNum*(g-2*f);
    }
   }
   else
   {
    x=r+(++boxNum)*multiple+f;
    rightLimit=r+g+boxNum*multiple-f;
   }
  }
  }
  double answer=1-area/(3.141592*R*R/4);
  FILE *fout=fopen("C-small.out","a");
  fprintf(fout,"Case #%d: %lf\n",(i+1),answer);
  fclose(fout);
 }
 fclose(ff);
}
