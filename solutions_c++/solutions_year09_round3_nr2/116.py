#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf

struct node
{
 double x,y,z;
 double vx,vy,vz;       
};
node fly[500];
int n;
double getdist(double t )
{
 double x=0,y=0,z=0;
 int i;
 for(i=0;i<n;i++) 
 {
   x = x + (fly[i].x + fly[i].vx*t);
   y = y + (fly[i].y + fly[i].vy*t);
   z = z + (fly[i].z + fly[i].vz*t);
 }
 x = x/n;
 y = y/n;
 z = z/n;
 re x*x+y*y+z*z;
}
int main() {
    
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    
    int t;
    sf("%d",&t);
    int kase=1;
    while(t--)
    {
     sf("%d",&n);
     int i;
     for(i=0;i<n;i++)
      sf("%lf %lf %lf %lf %lf %lf",&fly[i].x,&fly[i].y,&fly[i].z,&fly[i].vx,&fly[i].vy,&fly[i].vz);
     // check if constant over time
     double myval,myval2,myval3;
     myval=getdist(10);
     myval2 =getdist(15);
     myval3=getdist(20);
     if ( fabs(myval-myval2)<1e-9 && fabs(myval-myval3)<1e-9 )
     {
      // almost constant
      pf("Case #%d: %.9lf %.9lf\n",kase++,sqrt(myval),0);
      co;
     }
     // now tinary
     double lo=0,hi=1e9;
     int looper=1000;
     while ( looper--)
     {
       double lt = lo + (hi-lo)/3;
       double ut = lo + (hi-lo)/3*2;
       myval = getdist(lt);
       myval2 = getdist(ut);
       if ( myval2 > myval ) hi = ut;
       else lo=lt;
     }
     pf("Case #%d: %.9lf %.9lf\n",kase++, sqrt(myval),lo);
    }
    
    
	return 0;
}
