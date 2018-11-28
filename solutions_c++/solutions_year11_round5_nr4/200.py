#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define ll long long
char S[1000];

ll isps(ll x)
{
  ll xs=(ll)sqrt((double)x);
  for(ll xx=max(0ll,xs-10);xx<=xs+1;xx++)
    if(xx*xx==x)
      return 1;
  return 0;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      scanf("%s",&S);
      printf("Case #%d: ",t);


      int N=strlen(S);
      int numq=0;
      ll base=0;
      for(int i=0;i<N;i++)
	{
	  numq+=(S[i]=='?');
	  if(S[i]!='?')
	    {
	      ll b=S[i]-'0';
	      base+=(b<<(N-i-1));
	      //printf("%d\n",i);
	    }
	}
      //printf("%lld %d\n",base,N);
      for(int i=0;i<(1ll<<numq);i++)
	{
	  ll is=base;
	  ll mask=i;
	  for(int j=0;j<N;j++)
	    if(S[j]=='?')
	      {
		if((mask&1))
		  is+=(1ll<<(N-j-1));
		mask>>=1;
	      }
	  // printf("%lld\n",is);
	  if(isps(is))
	    {
	      //printf("%lld\n",is);
	      for(int j=0;j<N;j++)
		printf("%lld",(is>>(N-j-1))&1);
	      printf("\n");
	      break;
	    }
	}
	
    }
     
	
}
