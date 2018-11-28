#include<iostream>
#include<set>
#include<map>
#include<string>
#include<stdio.h>
#include<sstream>
#include<algorithm>
#include<sstream>
#include<queue>
#include<cmath>
#include<string.h>
using namespace std ;
#define INF (int)1e9
#define MAXN 2005


int main()
{
 int runs ;
 cin >> runs ;
 for(int T = 1;T <= runs;T++)
 {
  int X,R,S,_t,N,s[MAXN],e[MAXN],p[MAXN] ;
  double t ;
  int order[MAXN] ;
  cin >> X >> S >> R >> _t >> N ;
  for(int i = 0;i < N;i++)
  {
   cin >> s[i] >> e[i] >> p[i] ;
  }
  
  s[N] = 0 ;
  e[N] = X ;
  p[N++] = 0 ;

//  cout << "here: " << R << " " << S << endl ;
    
  for(int i = 0;i < N;i++)
  {
   order[2 * i] = s[i] ;
   order[2 * i + 1] = e[i] ;
  }
   
  typedef pair<int,int> P ;
  multiset<P> intervals ;
  
  sort(order,order + 2 * N) ;
  for(int i = 0;i + 1 < 2 * N;i++)
  {
   int best = 0 ;
   for(int j = 0;j < N;j++)
    if(order[i] >= s[j] && order[i + 1] <= e[j])
     best = max(best,p[j]) ;
   intervals.insert(P(best + S,order[i + 1] - order[i])) ;
  }
  
  t = _t ;
//  cout << "here: " << R << " " << S << endl ;
  R -= S ;
  double ret = 0 ;
  while(!intervals.empty())
  {
   P cur = *intervals.begin() ;
   intervals.erase(intervals.begin()) ;
//   cout << cur.first << " " << cur.second << endl ;
   double runTime = min(1. * t, 1. * cur.second / (cur.first + R)) ;
//   cout << runTime << endl ;
//   cout << cur.first << " " << cur.second << " " << t << " " << runTime << " " << 1. * cur.second / (cur.first + R) << " " << R << endl ;
//   if(runTime < 0) 
//   cout << "yes: " << t << " " << " " << cur.first << " " << cur.second << endl ;
   ret += runTime ;
   ret += (cur.second - (cur.first + R) * runTime) / cur.first ;
   t -= runTime ;
  }
  printf("Case #%d: %.9lf\n",T,ret) ;
 }
 return 0 ;
}
