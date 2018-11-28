#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include<cstdlib>
#include<cstring>
#include<string>


using namespace std;

#define pb push_back
#define sz size
#define all(a)  a.begin(),a.end()
#define SZ(v) ((int)(v).size())
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}


typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;
typedef long long  ll;

int main()
{
   int tt=0,test=0;
   cin>>tt;
   while(tt--)
   {
      double x=0,y=0,z=0,vx=0,vy=0,vz=0,d=0,t;
      double n;
      scanf("%lf",&n);
      double x1,y1,z1,vx1,vy1,vz1;
      for(int i=0;i<n;i++)
      {
         scanf("%lf %lf %lf %lf %lf %lf",&x1,&y1,&z1,&vx1,&vy1,&vz1);
         x+=x1;y+=y1;z+=z1;vx+=vx1;vy+=vy1;vz+=vz1;
      }
      
      if(vx*vx + vy*vy + vz*vz==0){d=(x*x + y*y + z*z)/(n*n); t=0;}
      else{
      t=(-1.0)*(x*vx + y*vy + z*vz)/(vx*vx + vy*vy + vz*vz);
       if(t<0){ d=(x*x + y*y + z*z)/(n*n);t=0;}
       else
           d=((x+t*vx)*(x+t*vx) + (y+t*vy)*(y+t*vy) + (z+t*vz)*(z+t*vz))/(n*n);  
     }
      
      cout << "Case #" << ((test)+1) << ": " << sqrt(fabs(d)) <<' '<< t << endl;
      
      test++;
   }     
    //cout<<sqrt(-3)<<endl;     
   
      
      
   return 0;
}   
