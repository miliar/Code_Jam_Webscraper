#include<iostream>
#include<set>
#include<map>
#include<string>
#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<queue>
#include<cmath>
#include<string.h>
using namespace std ;
int n,w,l,r[1002],id[1002] ;
double x[1002],y[1002] ;


bool solve(int k)
{
 if(k >= n) return true ;
 for(int i = 0;i < 10;i++)
 {
  double xa = ((1LL * rand() * rand()) % (w * 10000LL)) / 10000. ;
  double ya = ((1LL * rand() * rand()) % (l * 10000LL)) / 10000. ;
  bool valid = true ;
  for(int j = 0;valid && j < k;j++)
  {
   double xb = x[id[j]],yb = y[id[j]] ;
   double dist = sqrt((xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)) ;
   if(dist < r[k] + r[j]) valid = false ;
  }
  if(valid)
  {
   x[id[k]] = xa ; y[id[k]] = ya ;
   if(solve(k + 1)) return true ;
  }
 }
 return false ;
}

int main()
{
 int runs ;
 cin >> runs ;
 for(int t = 1;t <= runs;t++)
 {
  cin >> n >> w >> l ;
  for(int i = 0;i < n;i++) cin >> r[i] ;
  for(int i = 0;i < n;i++) id[i] = i ;
  for(int i = 0;i < n;i++)
   for(int j = i + 1;j < n;j++)
    if(r[i] < r[j])
    {
     swap(r[i],r[j]) ;
     swap(id[i],id[j]) ;
    }
  x[id[0]] = 0 ; y[id[0]] = 0 ;
  if(n > 1)
  {
   x[id[1]] = w ;
   y[id[1]] = l ;
  }
  bool ret = solve(2) ;
  printf("Case #%d:",t) ;
  if(!ret) printf(" Impossible\n") ;
  else
  {
   for(int i = 0;i < n;i++) printf(" %.4lf %.4lf",x[i],y[i]) ;
   printf("\n") ;
  }
 }
 return 0 ;
}
