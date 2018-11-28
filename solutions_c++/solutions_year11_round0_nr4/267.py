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



int val[1111];
int foi[1111];
int main()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      int n;
      memset(foi,0,sizeof(foi));
      scanf(" %d",&n);
      for(int i=1;i<=n;i++)
	scanf(" %d",&val[i]);
      double ret = 0;
      for(int i=1;i<=n;i++)
	{
	  int k=0;
	  if(foi[i])continue;
	  int p = val[i];
	  while(foi[p]==0)
	    {
	      foi[p]=1;
	      k++;
	      p = val[p];
	    }
	  if(k>1) ret += k;
	}
      printf("Case #%d: %lf\n",pp,ret);
    }
  return 0;
}
