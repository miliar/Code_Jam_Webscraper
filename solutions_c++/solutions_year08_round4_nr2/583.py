#include<vector>
#include<stdio.h>
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

double x[1005] , y[1005] , z[1005] , p[1005] ;
int N ;
double r[1005] ;

bool ok(double m)
{
   int i , j ;
   double tp1 , tp2 ;
   for(i=0;i<N;++i) for(j=i+1;j<N;++j)
   {
      tp1 = ((x[i]-x[j])*(x[i]-x[j])) + ((y[i]-y[j])*(y[i]-y[j])) + ((z[i]-z[j])*(z[i]-z[j])) ;
      tp1 += (2*(x[i]-x[j])*(y[i]-y[j])) + (2*(x[i]-x[j])*(z[i]-z[j])) + (2*(y[i]-y[j])*(z[i]-z[j])) ;
      tp2 = (m*p[i]*m*p[i]) + (m*p[j]*m*p[j]) ;
      tp2 *= tp2 ;
      if(tp1 > tp2) return false ;
   }
   return true ;
}



int main()
{
   int T ; 
   int r ;
   int i ;
   double low , high , mid ;
   ifstream fin("input.txt") ;
   ofstream fout("output.txt") ;
   fin >> T ;
   for(r=1;r<=T;++r)
   {
      fin >> N ;
      for(i=0;i<N;++i) fin >> x[i] >> y[i] >> z[i] >> p[i] ;
      low = 0.0 ;
      high = 1e18 ;
      for(i=0;i<500;++i)
      {
         mid = low + (high-low)/2.0 ;
         if(ok(mid)) high = mid ;
         else low = mid ;
         //cout << mid << endl ;
      }
      fout << "Case #" << r << ": " << low << endl ;
   }
   getchar() ;
   getchar() ;
   return 0 ;
}
