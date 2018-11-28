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
int n,m,ret;
int pot[55];
int last[55];
inline int calc(const int a){
  int v = 0;
  int at = a;
  int x = 0;
  while(at){
    x++;
    at/=10;
  }
  for(int i=1;i<x;i++){
    last[i] = (a%pot[i])*pot[x-i] + a/pot[i];
    if(last[i]>a && last[i]<=m){
      bool ok = true;
      for(int j=1;ok && j<i;j++)
        if(last[i]==last[j])ok=false;
      if(ok){
        ret++;
      }
    }
  }
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  pot[0]=1;
  for(int i=1;i<10;i++)
    pot[i]=10*pot[i-1];

  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d %d",&n,&m);
      ret = 0;
      for(int i=n;i<=m;i++)
        calc(i);
      printf("Case #%d: %d\n",pp,ret);
    }
  return 0;
}
