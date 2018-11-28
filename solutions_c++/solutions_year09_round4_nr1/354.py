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
int pos[55];

int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      scanf("%d",&n);
      
      for(int i=1;i<=n;i++)
	{
	  int p=0;
	  char c;
	  int j;
	  for(j=1;j<=n;j++)
	    {
	      scanf(" %c",&c);
	      if(c=='1')
		p=j;
	      
	    }
	  pos[i]=p;
	  // printf("%d\n",pos[i]);
	}
      int ret=0;
      for(int i=1;i<=n;i++)
	{
	  int t;
	  if(pos[i]<=i)continue;
	  for(int j=i+1;j<=n;j++)
	    if(pos[j]<=i)
	      {
		t=0;
		for(int k=j;k>i;k--)
		  {
		    swap(pos[k],pos[k-1]);
		    t++;
		  }
		break;
	      }
	  ret+=t;
	}
      printf("Case #%d: %d\n",pp,ret);
    }

  return 0;
}
