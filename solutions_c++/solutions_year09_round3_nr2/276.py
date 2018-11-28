#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <cmath>

using namespace std;
/*
struct NODE{
   double x,y,z,vx,vy,vz;
};
NODE d[1000];
*/
int n; 
int main()
{
    int kase;
    int i,j,k;
    freopen("B-large.in","r",stdin);  freopen("p2.out","w",stdout);
    double x,y,z,vx,vy,vz,ax,bx,ay,by,az,bz,t1,t2,ansd,anst,a,b,c,x1,x2;
    cin>>kase;
    for(i=1;i<=kase;i++) {
       cout<<"Case #"<<i<<": ";
       cin>>n;
       ax=bx=ay=by=az=bz=0.00;
       for(j=1;j<=n;j++) {
          cin>>x>>y>>z>>vx>>vy>>vz;
          ax+=x;  bx+=vx;
          ay+=y;  by+=vy;
          az+=z;  bz+=vz;
       }
       //cout<<ax<<" "<<ay<<" "<<az<<endl;
       //cout<<bx<<" "<<by<<" "<<bz<<endl;
       t1=(ax*bx+ay*by+az*bz);
       a=bx*bx+by*by+bz*bz;  b=2*t1;  c=ax*ax+ay*ay+az*az;
       double delta;
       //cout<<"a"<<a<<endl;
       if(a==0) {
         if(b>=0) {
            anst=0;
            ansd=sqrt(c)/n;
         }
         else {
            anst=(-c)/b;
            ansd=0;
         }
       }else{
       delta=b*b-4*a*c;
       //cout<<"delta="<<delta<<endl;
       if(delta<=0) {
         anst=-b/2.0/a;
         if(anst<=0) {
            anst=0;
            ansd=sqrt(c)/n;
         }
         else {
           ansd=sqrt(c-b*b/4.0/a)/n;
           //cout
         }
       }else{
          x1=(-b-sqrt(delta))/(4*a*c);
          x2=(-b+sqrt(delta))/(4*a*c);
          if(x2<=0) {
             anst=0;
             ansd=sqrt(c)/n;
             //cout<<"111";
          }else{
             if(x1<0) {
                anst=x2;
                ansd=0;
                //cout<<"222";
             }else {
                anst=x1;
                ansd=0;
                //cout<<"333";
             }
          }
       }//else
       }//else
       //cout<<ansd<<" "<<anst<<endl;
       printf("%.8lf %.8lf\n",ansd,anst);
    }
    return 0;
}
