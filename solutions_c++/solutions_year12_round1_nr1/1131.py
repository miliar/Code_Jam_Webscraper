#include <stdio.h>
#include <iostream>
using namespace std;

const int MAXN=100000;

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  
  int T,i,j;

  scanf("%d",&T);
  for (i=1; i<=T; ++i)
    {
      double p[MAXN+1];
      int A,B,K;
      
      scanf("%d%d",&A,&B);
      p[0]=1;
      for (j=1; j<=A; ++j)
        {
          scanf("%lf",&p[j]);
          p[j]*=p[j-1];
        }
        
      double min=B+2;
      
      for (K=0; K<=A; ++K)
        {
          double t;
          
          t=p[A-K]*(K+K+B-A+1)+(1-p[A-K])*(K+K+B-A+1+B+1);
          if (t<min) min=t;
        }
        
      printf("Case #%d: %.6f\n",i,min);
    }

  fclose(stdin);
  fclose(stdout);
  
  return(0);
}
