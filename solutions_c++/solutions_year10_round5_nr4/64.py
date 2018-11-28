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

int foi[15][30];
int sum,base;
huge ret;

void go(int aaa,int ant)
{
  if(aaa==0)
    {
      ret++;
      return;
    }
  for(int x=1;x<min(ant,aaa+1);x++)
    {
      int aux=x;
      int dig=0;
      bool ok=true;
      while(aux>0)
	{
	  int t=aux%base;
	  aux/=base;
	  if(foi[t][dig])ok=false;
	  foi[t][dig]++;
	  dig++;
	}
      if(ok)go(aaa-x,x);
      
      aux=x;
      dig=0;
      while(aux>0)
	{
	  int t=aux%base;
	  aux/=base;
	  foi[t][dig]--;
	  dig++;
	}
      
    } 
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      //  int sum,base;
      memset(foi,0,sizeof(foi));
      scanf("%d %d",&sum,&base);
      // int foi[10][3]={0};
      ret=0;
      go(sum,sum+1);

      printf("Case #%d: %lld\n",pp,ret);
    }
  return 0;
}
