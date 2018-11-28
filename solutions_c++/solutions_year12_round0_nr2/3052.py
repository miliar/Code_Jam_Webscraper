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
int n,p,a[102] ;

int memo[102][102] ;
int solve(int k,int s)
{
 if(s < 0) return -INF ;
 if(k == n) return s == 0 ? 0 : -INF ;
 if(memo[k][s] != -1) return memo[k][s] ;
 int ret = -INF ;
 for(int i = 0;i <= 10;i++)
  for(int j = i;j <= 10;j++)
   for(int t = j;t <= 10;t++)
    if(i + j + t == a[k] && t - i <= 2)
     ret = max(ret,solve(k + 1,s - (t - i == 2 ? 1 : 0)) + (t >= p ? 1 : 0)) ;
 return memo[k][s] = ret ;
}

int main()
{
 int t ;
 cin >> t ;
 for(int tt = 1;tt <= t;tt++)
 {
  int s ;
  cin >> n >> s >> p ;
  for(int i = 0;i < n;i++) cin >> a[i] ;
  memset(memo,255,sizeof memo) ;
  int ret = solve(0,s) ;
  printf("Case #%d: %d\n",tt,ret) ;
 }
 return 0 ;
}
