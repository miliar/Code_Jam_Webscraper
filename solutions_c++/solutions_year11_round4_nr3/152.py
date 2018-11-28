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

const int maxn = 3111111;
int lista[maxn];
int qte=0;
int eh[maxn];
void acha()
{
  for(huge i=2;i<=maxn;i++)
    {
      if(eh[i]==0)
	{
	  lista[qte++]=i;
	  for(huge j=i*i;j<=maxn;j+=i)
	    eh[j]=1;
	}
    }
}

int v[1111];
int main()
{
  acha();
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      huge n;
      scanf("%lld",&n);
      huge maior=0,menor=0;
      huge saldo=0;
      for(int i=0;i<qte;i++)
	{
	  huge at = n;
	  if(at<lista[i])break;
	  while(at>=lista[i])
	    {
	      saldo ++;
	      at/=lista[i];
	    }
	  saldo-=1;
	}
      
      if(n==1)saldo=-1;
      printf("Case #%d: ",pp);
      printf("%lld\n",saldo+1);
    }
  return 0;
}
