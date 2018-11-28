#include <stdio.h>
#include <math.h>

bool sw[1000];
long long N,K;
long long f[35];
int main()
{
  int T;
  scanf("%d",&T);

  f[1]=1;
  for(int i=2;i<=32;i++)
    {
      f[i]=2*f[i-1]+1;
    }


  for(int t=1;t<=T;t++)
    {
      scanf("%lld %lld",&N,&K);
      if((K+1)%(f[N]+1)==0)
	{
	  printf("Case #%d: ON\n",t);
	}
      else
	{
	  printf("Case #%d: OFF\n",t);
	}
      
    }
}
