#include<stdio.h>
#include<stdlib.h>
int main()
{
  FILE *fp;
  fp = fopen("C-small-attempt0.in","r");
  if(fp == NULL)
  {
    exit(0);
  }
  int T,R,k,N;
  fscanf(fp,"%d",&T);
  int count = T-1;
  int tCount = T;
  while( tCount > 0 )
  {
    fscanf(fp,"%d%d%d",&R,&k,&N);
    int g[N];
    int temp = N;
    int sum,gSum=0;
    int p;
    int hello,group= 1;
    while(temp>0)
    {
      fscanf(fp,"%d",&g[N-temp]);
      temp--;
    }
   
    for(int i = 0; i< R;i++)
    {
      sum = g[0];
      hello = g[0];
      group = 1;
      if(sum > k){
	gSum = 0;
	printf("Case #%d: %d\n",(T-count),gSum);
	count--;
	tCount--;
	break;
      }
      else{
	for(p = 0;p<N-1;p++){
	  g[p]=g[p+1];
	}
	g[p]=hello;
	while(sum <= k ){
	sum = sum + g[0];
	  if(sum<=k && group < N){
	    group++;
	    hello = g[0];
	    for(p = 0;p<N-1;p++){
	    g[p]=g[p+1];
	    }
	    g[p]=hello;
	  }
	  else{
	    sum = sum - g[0];
	    break;
	  }
	}
      }
      gSum = gSum + sum;
  }
  printf("Case #%d: %d\n",(T-count),gSum);
  count--;
  tCount--;
  }
  return 1;
} 
