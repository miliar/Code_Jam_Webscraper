#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

int main( )
{
  int T,N;

  freopen("out.txt","w",stdout);
  cin>>T;
 for(int t=1;t<=T;t++)
 {
   cin>>N;
   int x,y,z,vx,vy,vz;
   double sumx=0,sumy=0,sumz=0,svx=0,svy=0,svz=0,a,b,c,time,dis;
   for(int i=0;i<N;i++)
   {
       cin>>x>>y>>z>>vx>>vy>>vz;
       sumx+=x;
       sumy+=y;
       sumz+=z;
       svx+=vx;
       svy+=vy;
       svz+=vz;
   }
  /* sumx/=N;
   sumy/=N;
   sumz/=N;
   svx/=N;
   svy/=N;
   svz/=N;
   */
   a=svx*svx+svy*svy+svz*svz;
   b=2*(sumx*svx+sumy*svy+svz*sumz);
   c=sumx*sumx+sumy*sumy+sumz*sumz;
   if(a==0)
   {
    time=0;
    dis=sqrt(c)/N;
   }
   else if(a>0)
   {
    // time=-b/a/2;
     if((a>0&&b>0)||(a<0&&b<0))
     {
         time=0;
         dis=sqrt(c)/N;
        // cout<<"what"<<t<<endl;
     }
     else
     {
     time=-b/a/2;
     dis=sqrt(c-b*b/a/4)/N;
     }
   }

    cout<<"Case #"<<t<<": ";
    printf("%.8lf %.8lf\n",dis,time);

 }

   return 0;
}
