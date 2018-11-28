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


int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      bool fudeu = false;
      huge n;
      huge p1,p2;
      scanf("%lld %lld %lld",&n,&p1,&p2);


      huge hoje; 
      if(p1>0)
	{
	  hoje = 100/(__gcd(100ll,p1));
	  p1 = p1/(__gcd(100ll,p1));
	}
      else 
	{
	  hoje = 1;
	  p1 = 0;
	}

      if(hoje>n)
	{
	  fudeu = true;
	}
      else
	{
	  fudeu = true;
	  huge res =  p2*hoje - p1*100;
	  // printf("%lld %lld\n",p1,hoje);
	  for(int i=0;i<=10000;i++)
	    {
	      huge at = res + p2*i;
	      if(at%100 == 0 && at>=0 && at/100<=i)
		{
		  fudeu = false;
		  break;
		}
	    }
	  
	}
      printf("Case #%d: ",pp);
      if(fudeu)
	printf("Broken\n");
      else
	printf("Possible\n");
    }
  return 0;
}
