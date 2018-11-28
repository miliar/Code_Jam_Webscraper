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


int main()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      int n,p[2]={1,1};
      int f[2]={0,0};
      scanf("%d",&n);
      int r = 0;
      for(int i=0;i<n;i++)
	{
	  char c;
	  int t,x;
	  scanf(" %c %d",&c,&t);
	  x = (c=='O')?0:1;
	  if(f[x]>=abs(p[x]-t))
	    {
	      r+=1;//aperta;
	      f[x^1]+=1;
	    }
	  else
	    {
	      r+=1+abs(p[x]-t)-f[x];
	      f[x^1]+=1+abs(p[x]-t)-f[x];
	    }
	  p[x]=t;
	  f[x]=0;
	}
      printf("Case #%d: %d\n",pp,r);
    }
  return 0;
}
