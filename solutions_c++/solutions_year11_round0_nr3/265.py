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
      int n;
      int soma=0,menor=inf,x=0;
      scanf("%d",&n);
      for(int i=0;i<n;i++)
	{
	  int a;
	  scanf("%d",&a);
	  soma+=a;
	  menor=min(a,menor);
	  x^=a;
	}
      if(x==0)
	printf("Case #%d: %d\n",pp,soma-menor);
      else
	printf("Case #%d: NO\n",pp);
    }

  return 0;
}
