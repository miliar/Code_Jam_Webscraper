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
int o[2000002] ;
int main()
{
 int t ;
 cin >> t ;
 for(int tt = 1;tt <= t;tt++)
 {
  memset(o,0,sizeof o) ;
  int a,b,ret = 0 ;
  cin >> a >> b ;
  for(int i = a;i < b;i++)
  {
   int d = 0,dg[20] ;
   for(int k = i;k > 0;k /= 10) dg[d++] = k % 10 ;
   for(int k = 0;k + k < d;k++) swap(dg[k],dg[d - 1 - k]) ;
   for(int j = 1;j < d;j++)
   {
    int now = 0 ;
    for(int k = 0;k < d;k++) now = now * 10 + dg[(j + k) % d] ;
    if(now > i && now <= b && o[now] != i) { o[now] = i ; ret++ ; }
   }
  }
  printf("Case #%d: %d\n",tt,ret) ;
 }
 return 0 ;
}
