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


int n;
huge boards[111];
huge best[20000500];
int main ()
{
  int tt;
  scanf("%d",&tt);
  // printf("oi\n");

  for(int pp=1;pp<=tt;pp++)
    {
      huge len;
      huge mx=0;
      huge val=0;
      // printf("oi\n");
      // return 0;
      scanf("%lld %d",&len,&n);
      for(int i=0;i<n;i++)
	{
	  scanf("%lld\n",&boards[i]);
	 
	}
      sort(boards,boards+n);
      if(n==1)
	val=n*boards[0]*boards[0]+1;
      else
	val=n*boards[n-2]*boards[n-1]+1;
      // return 0;
      //printf("%lld\n%",val);
      for(int i=0;i<=val;i++)
	best[i]=hugeinf;
      best[0]=0;
      for(int i=0;i<n;i++)
	{
	  for(int j=boards[i];j<=val;j++)
	    {
	      best[j]=min(best[j],1+best[j-boards[i]]);
	    }
	}
      // huge val=n*mx;
      huge ret=hugeinf;
      for(int i=1;i<=val;i++)
	{
	  //huge bla=len-i;

		  if(best[i]<hugeinf && best[len%i]<hugeinf)
		    {
		      ret = min(ret,len/i*best[i]+best[len%i]);
		      
		    }  
	   	
	}      
      
      //      printf("%lld\n",best[100]);
      if(ret>=hugeinf)
	printf("Case #%d: IMPOSSIBLE\n",pp);
      else
	printf("Case #%d: %lld\n",pp,ret);
    }
  return 0;
}
