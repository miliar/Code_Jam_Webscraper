#include <stdio.h>
#include <math.h>

long long int frequency[10000];
long long int P,K,L,numtestcases,lowestavailplace[100000];
long long int jopt,kopt,lowestplace,highestfreq;
bool doneit[100000];
long long int lowerstavailplace;
int main(int argc,char *argv[])
{
  FILE *fp;
  fp=fopen(argv[1],"r");
  fscanf(fp,"%d",&numtestcases);
  
  for(int cases=1;cases<=numtestcases;cases++)
    {
      fscanf(fp,"%lld",&P);
      fscanf(fp,"%lld",&K);
      fscanf(fp,"%lld",&L);
      for(long long int i=1;i<=L;i++)
	{
	fscanf(fp,"%lld",&frequency[i]);
	doneit[i]=0;
	}
      long long int lowestfreq=1000001;
      for(long long int i=1;i<=K;i++)
	lowestavailplace[i]=1;
      long long int count=0;
      for(long long int i=1;i<=L;i++)
	{
	  highestfreq=-1;
	  for(long long int j=1;j<=L;j++)
	    {
	      if(frequency[j]>highestfreq && !doneit[j])
		{
		  highestfreq=frequency[j];
		  jopt=j;
		}
	    }
	  doneit[jopt]=1;
	  //place in the lowersavailplace
	  lowestplace=100000;
	  for(long long int k=1;k<=K;k++)
	    {
	      if(lowestavailplace[k]<lowestplace)
		{
		  kopt=k;
		  lowestplace=lowestavailplace[k];
		}
	    }
	  lowestavailplace[kopt]++;
	  count+=lowestplace*highestfreq;
	}
      printf("Case #%d: %lld\n",cases,count);
    }
  
}
