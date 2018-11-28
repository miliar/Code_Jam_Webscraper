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
const int desloca = 1100001;
const int maior=2500505;
int tem[2500505];
huge saida;
int n;
int go(int a)
{
  //  if(a-desloca<10)printf("%d\n",a-desloca);
  if(tem[a]<2)return a+1;
  int x=tem[a]/2;
  saida+=x;
  tem[a-1]+=x;
  tem[a+1]+=x;
  tem[a]=tem[a]%2;
  if(tem[a-1]>1)
    return a-1;
  return a+1;
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d",&n);
      memset(tem,0,sizeof(tem));
      int start=inf;
      for(int i=0;i<n;i++)
	{
	  int a,b;
	  int qte;
	  scanf("%d %d",&a,&qte);
	  // val[i].a=val[i].b=a;
	  //val[i].qte=qte;
	  tem[a+desloca]=qte;
	  start=min(start,a+desloca);
	}
      saida=0;
      while(start<maior)
	{
	  start=go(start);


	}
      printf("Case #%d: %lld\n",pp,saida);
    }
  return 0;
}
