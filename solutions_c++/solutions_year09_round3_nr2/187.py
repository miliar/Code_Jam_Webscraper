#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<set>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
#include<map>
#include<fstream>

#define all(c) c.begin(), c.end()
#define allr(c) c.rbegin(), c.rend()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define INF (int)1e9

using namespace std ;

int N ;
double x[600] , y[600] , z[600] , vx[600] , vy[600] , vz[600] ;
double sx , sy , sz , svx , svy , svz ; 

double f(double t)
{
   double out = 0.0 ;
   out += (sx + svx*t) * (sx + svx*t) ;
   out += (sy + svy*t) * (sy + svy*t) ;
   out += (sz + svz*t) * (sz + svz*t) ;
   return out ;
}


int main()
{
   freopen("B-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   int T ;
   cin >> T ;
   for(int run=1;run<=T;++run)
   {
      cin >> N ;
      sx = sy = sz = svx = svy = svz = 0.0 ;
      for(int i=0;i<N;++i) 
      {
         cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i] ;
         sx += x[i] ;
         sy += y[i] ;
         sz += z[i] ;
         svx += vx[i] ;
         svy += vy[i] ;
         svz += vz[i] ;
      }
      double left = 0.0 ;
      double right = 1e16 ;
      for(int i=0;i<250;++i)
      {
         double lthd = (left*2.0 + right) / 3.0 ;
         double rthd = (left + right*2.0) / 3.0 ;
         if( f(lthd) > f(rthd) ) left = lthd ;
         else right = rthd ;
      }
      double outt = (left+right) / 2.0 ;
      double outd = sqrt(f(outt))/N ;
      cout << "Case #" << run << ": " << outd << " " << outt << endl ;
   }
   //while(1) ;
   return 0 ;
}
