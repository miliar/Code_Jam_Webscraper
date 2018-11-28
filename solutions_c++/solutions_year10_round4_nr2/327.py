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
int cost[2050][2050];
int need[2050];
int p;



int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d",&p);
      for(int i=0;i<(1<<p);i++)
	{
	  scanf("%d",&need[i]);
	  need[i]=p-need[i];
	}
      for(int i=0;i<p;i++)
	{
	  for(int j=0;j<(1<<((p-1)-i));j++)
	    {
	      scanf("%d\n",&cost[i][j]);
	    }
	}
      bool fim=false;
      int tira=0;
     
      for(int nivel=p;nivel>0;nivel--)
	{
	  int k=0;
	  for(int i=0;i<(1<<(p-nivel));i++)//num de pedacos
	    {
	      bool tem=false;
	      for(int x=0;x<(1<<(nivel));x++)//tam do pedaco
		{
		  if(need[k]>0)
		    tem=true;
		  k++;
		}
	      if(tem)
		{
		  tira++;
		  k-=(1<<nivel);
		  for(int x=0;x<(1<<(nivel));x++)//tam do pedaco
		    {
		      need[k]-=1;
		      k++;
		    }
		}
	    }
	  
	}
      printf("Case #%d: %d\n",pp,tira);
    }
  return 0;
}
