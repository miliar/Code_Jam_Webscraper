#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
const int maxn = 12345;
huge best[maxn];
int foi[maxn];
int n;
huge tam[maxn][2];
huge go(int a){
  if(a==0)return tam[a][0];
  if(best[a]==-inf){
    huge ret = -999999;
    for(int i=0;i<a;i++){
      huge d = tam[a][0]-tam[i][0];
      huge x = go(i);
      if(x>=d){
        ret = max(ret, min(d,(huge) tam[a][1]));
      }
    }
    best[a]=ret;
  }
  return best[a];
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d",&n);
      for(int i=0;i<n;i++)
        scanf("%lld %lld",&tam[i][0],&tam[i][1]);
      scanf("%lld",&tam[n][0]);
      tam[n][1]=0;
      n++;
      for(int i=0;i<n+100;i++)
        best[i]=-inf;

      printf("Case #%d: %s\n",pp,go(n-1)>=0?"YES":"NO");
    }
  return 0;
}
