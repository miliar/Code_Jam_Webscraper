#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;

int val[15];
int foi[15];
int n;
int best[5555];
int go(int a)
{
  if(n==0)return 0;
  if(a==0)return inf;
  if(best[a]==-1)
    {
      int ret=0;
      for(int i=1;i<(1<<n);i++)
	{
	  int usa[15];
	  int p=0;
	  bool ok=true;
	  for(int j=0;ok && j<n;j++)
	    if( ((1<<j)&i) && ((1<<j)&a)==0)ok=false;
	    
	  if(!ok)continue;
	  for(int j=0;j<n;j++)
	    if((1<<j)&i)usa[p++]=val[j];
	  sort(usa,usa+p);
	  for(int k=1;ok && k<p;k++)
	    if(usa[k]!=usa[k-1]+1){ok=false;}

	  if(ok)
	    {
	      ret = max(ret,min(p,go(a^i)));

	    }
	}
      best[a]=ret;
    }
  return best[a];
}
int main () {
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      memset(best,-1,sizeof(best));
      scanf("%d",&n);
      
      for(int i=0;i<n;i++)
	scanf("%d",&val[i]);
      printf("Case #%d: %d\n",pp,go((1<<n)-1));
    }
  return 0;
}
