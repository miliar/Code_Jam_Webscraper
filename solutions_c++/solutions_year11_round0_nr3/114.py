#include <stdio.h>
#include <math.h>
#include <algorithm>
#define ll long long
using namespace std;
int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      int N;
      scanf("%d",&N);
      ll xorval=0;
      ll mina=1000000000000000ll;
      ll summ=0;
      for(int i=0;i<N;i++)
	{
	  ll v;
	  scanf("%lld",&v);
	  xorval^=v;
	  mina=min(v,mina);
	  summ+=v;
	}
      if(xorval!=0)
	printf("Case #%d: NO\n",t);
      else
	printf("Case #%d: %lld\n",t,summ-mina);
      
      
      
    }
}
