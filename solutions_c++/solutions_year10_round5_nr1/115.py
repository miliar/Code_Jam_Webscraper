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
const int maxa = 1000003;
int eh[maxa];
int lista[maxa];
int qte=0;
int n,d;
void gera()
{
  for(int i=2;i<maxa;i++)
    {
      if(eh[i]==0)
	{
	  lista[qte++]=i;
	  //printf("%d\n",i);
	  for(int k=2*i;k<maxa;k+=i)
	    eh[k]=1;
	}    
    }
}
int pot(int a)
{
  int r=1;
  for(int i=0;i<a;i++)
    r*=10;
  return r;
}
int main ()
{
  int tt;
  gera();
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      //   printf("%d\n",qte);
      int ent[11];
      scanf("%d %d",&d,&n);
      int maior=pot(d);
      int menor=0;
      for(int i=0;i<n;i++)
	{
	  scanf("%d",&ent[i]);
	  menor=max(menor,ent[i]);
	}
      int acho=-1;
      for(int i=0;i<qte;i++)//chuta primo
	{
	  int primo=lista[i];
	  if(primo<=menor)
	    continue;
	  if(primo>=maior)
	    break;
	  // printf("%d\n",primo);
	  for(int j=0;j<primo;j++)//chuta a
	    {
	      bool ok=true;
	      int b;
	     
	      b = ((ent[1]-ent[0]*j)%primo+primo)%primo;
	      // if(j==1)printf("%d\n",b);
	      for(int k=0;k<n-1;k++)
		{
		  if(ent[k+1]!=(ent[k]*j+b)%primo)
		    {ok=false;break;}
		}
	      if(ok)
		{
		  if(acho==-1)
		    acho = (ent[n-1]*j+b)%primo;
		  else if(acho!=(ent[n-1]*j+b)%primo)
		    {
		      //  printf("%d %d %d\n",primo,j);
		      acho=-2;
		    }		
		}
	    }
	}
      printf("Case #%d: ",pp);
      if(n==1 || acho==-2 || acho==-1)
	printf("I don't know.\n");
      else
	printf("%d\n",acho);

    }
  return 0;
}
