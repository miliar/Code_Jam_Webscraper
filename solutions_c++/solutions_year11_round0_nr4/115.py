#include <stdio.h>
#include <math.h>

double derang[10000];
double fact[10000];
double f[10000];
double dividefac(double val,int v)
{
  for(int i=1;i<=v;i++)
    val/=i;
  return val;
}
double getratio(int i)
{
  if(i<=40)
    return derang[i]/fact[i];
  else
    return 1.0/exp(1);
}
int main()
{
  
  derang[0]=1;
  derang[1]=0;
  for(int i=2;i<=40;i++)
    derang[i]=(i-1)*(derang[i-1]+derang[i-2]);
  fact[0]=1;
  for(int i=1;i<=40;i++)
    fact[i]=fact[i-1]*i;
  f[0]=0;
  f[1]=0;
  for(int i=2;i<=1000;i++)
    {

      f[i]=1;
      

      f[i]=1;
      for(int j=2;j<i;j++)
	f[i]+=getratio(j)*dividefac(f[j],i-j);
      f[i]/=(1.0-getratio(i));
      //if(i<=2)
      //	printf("%d %lf\n",i,f[i]);
    }
  //printf("%lf\n",f[50]);

  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      int N;
      scanf("%d",&N);
      int ct=0;
      for(int i=1;i<=N;i++)
	{
	  int n;
	  scanf("%d",&n);
	  if(n!=i)
	    ct++;
	}
      
      printf("Case #%d: %1.9f\n",t,f[ct]);
    }

}
