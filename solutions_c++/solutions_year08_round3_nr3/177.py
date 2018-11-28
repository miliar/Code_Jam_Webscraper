#include <stdio.h>
#include <math.h>

long long int A[1000000];
long long int n,m,X,Y,Z,numtestcases;
long long int array[1000000];
long long int numposs[1000000];
long long int isposs[1000000];
long long int findit(long long int position,long long int lastpos);

int main(int argc,char *argv[])
{
  FILE *fp;
  fp=fopen(argv[1],"r");
  fscanf(fp,"%lld",&numtestcases);
  
  for(long long int casee=1;casee<=numtestcases;casee++)
    {
      fscanf(fp,"%lld",&n);
  
      fscanf(fp,"%lld",&m);
      fscanf(fp,"%lld",&X);
      fscanf(fp,"%lld",&Y);
      fscanf(fp,"%lld",&Z);
      //printf("%lld %lld %lld %lld %lld\n",n,m,X,Y,Z);

      for(long long int i=0;i<=m-1;i++)
	fscanf(fp,"%lld",&A[i]);

      for(long long int i=0;i<=n-1;i++)
	{
	  //printf("%lld\n",A[i%m]);
	  array[i+1]=A[i%m];
	  A[i%m]=(Z+Z+X*A[i%m]+Y*(i+1))%Z;
	}
      //for(int i=1;i<=n;i++)
		// printf("%lld ",array[i]);
      // printf("\n");
      for(long long int i=0;i<=n;i++)
	{
	numposs[i]=0;
	isposs[i]=0;
	}
      array[0]=-1;
      array[n+1]=2000000000;
      printf("Case #%lld: %lld\n",casee,(findit(numposs[0],n+1)-1)%1000000007);
      //printf("Over\n");
      
      

    }


  
}

long long int findit(long long int position,long long int lastpos)
{
  if(position==lastpos)
    return 1;
  if(isposs[position])
    return numposs[position];
  long long int count=0;
  
  for(long long int i=position+1;i<=lastpos;i++)
    {
      if(array[i]>array[position])
	count+=findit(i,lastpos);
    }
  isposs[position]=1;
  numposs[position]=(count%1000000007);
  return numposs[position];
}
