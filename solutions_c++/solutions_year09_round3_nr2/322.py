#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>
#define div 1000
using namespace std;
int T;
vector<double> x;
vector<double> y;
vector<double> z;
vector<double> vx;
vector<double> vy;
vector<double> vz;
double t;
double dis;        //18218752807250280.00000000
                   //7888778035031515.00000000
                   //13190852921685932.00000000
                   //18218752807250280
                   //5923225128607066.00000000
                   //6376702644831916
void solve()
{

     double A1 = 0;
     double B1 = 0;
     double A2 = 0;
     double B2 = 0;
     double A3 = 0;
     double B3 = 0;
     for(int i=0;i<x.size();i++)
     {
             A1 += vx[i]/div;
             A2 += vy[i]/div;
             A3 += vz[i]/div;

             B1 += x[i]/div; 
             B2 += y[i]/div;
             B3 += z[i]/div;       
     }
     double D = A1*A1+A2*A2+A3*A3;
     if( abs(D)<=0.000001 ) { t=0; }
     else t = -(B1*A1+B2*A2+B3*A3)/D;
     if( t<=0 )
     {
  //      printf("t<0\n") ;
        t = 0;
     }
     double d1 = 0;
     double d2 = 0;
     double d3 = 0;
     for(int i=0;i<x.size();i++)
     {
             d1 += x[i] + vx[i]*t;  
             d2 += y[i] + vy[i]*t;
             d3 += z[i] + vz[i]*t;      
     }
     int n = x.size();
     double d = (d1*d1 + d2*d2 + d3*d3)/(n*n);
     dis = sqrt(d);
     
     
}

int main(int argc, char *argv[])
{
   freopen("B-large.in","r",stdin);
 //    freopen("B-large-practice (1).in","r",stdin);
    freopen("out1.txt","w",stdout);
      
    int N;

    scanf("%d",&N);

    int CASE = 1;
    while(N--)
    {
          scanf("%d",&T);
          x.clear();
          y.clear();
          z.clear();
          vx.clear();
          vy.clear();
          vz.clear();
          for(int i=0;i<T;i++)
          {
                 double _x,_y,_z,_vx,_vy,_vz; 
                 scanf("%lf%lf%lf%lf%lf%lf",&_x,&_y,&_z,&_vx,&_vy,&_vz);
                 x.push_back(_x);
                 y.push_back(_y);
                 z.push_back(_z);
                 vx.push_back(_vx);
                 vy.push_back(_vy);
                 vz.push_back(_vz);         
          }    
          solve();
    
          printf("Case #%d: %.8lf %.8lf\n",CASE,dis,t);
          CASE++;     
    }

    return 0;
}
