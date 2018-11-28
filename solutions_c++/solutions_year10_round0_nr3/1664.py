#include<stdio.h>

int main()
{
  long long int t,T,r,R,k,N,E,g[1100];
  long long int a,b,s;
  long long int q,Eq[1100],Rq[1100],w1,w2;

  for(t=1,scanf(" %lld",&T);t<=T;t++)
  {
    scanf(" %lld %lld %lld",&R,&k,&N);
    for(a=0;a<N;a++)
    	scanf(" %lld",&g[a]);

    for(a=0;a<N;a++)
      Rq[a]=-1;

    for(a=0,q=0,E=0,r=1;r<=R;r++)
    {
      Eq[a]=E;
      Rq[a]=r;
      for(s=0,b=a;;b++)
      {
        if(b==N) b=0;
	if(s+g[b]>k || (b==a && s!=0)) break;
	s+=g[b];	
      }
      E+=s;
      a=b;
      if(q==0 && Rq[a]>0)
      {
        w1=r-Rq[a]+1;
	w2=(R-r)/w1;
	r+=w1*w2;
	E+=(E-Eq[a])*w2;
	q=1;
      }
    }

    printf("Case #%lld: %lld\n",t,E);
  }

  return(0);
}

