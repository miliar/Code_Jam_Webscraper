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
#define INF (int)1e9
#define MAXN 10002
int n,L,d[MAXN],l[MAXN] ;

int memo2[MAXN] ;
int solve(int k)
{
 if(k == n) return 0 ;
 if(memo2[k] != -1) return memo2[k] ;
 int ret = INF + 2 ;
 for(int i = k + 1;i <= n && d[i] - d[k] <= l[k];i++)
  if(solve(i) <= d[i] - d[k])
   ret = min(ret,d[i] - d[k]) ;
 return memo2[k] = ret ;
}


int main()
{
 int runs ;
 cin >> runs ;
 for(int t = 1;t <= runs;t++)
 {
  cin >> n ;
  for(int i = 1;i <= n;i++) cin >> d[i] >> l[i] ;
  cin >> L ;
  
  d[0] = 0 ;
  d[n + 1] = L ;
  n++ ;
  memset(memo2,255,sizeof memo2) ;
  int ret = solve(1) ;
  if(ret <= d[1] - d[0]) printf("Case #%d: YES\n",t) ;
  else printf("Case #%d: NO\n",t) ;
 }
 
 return 0 ;
}
