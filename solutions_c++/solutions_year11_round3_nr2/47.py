#include"stdio.h"
long long dist[1000002],savings[1000002];
int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
  {
    int numBoosters,n,c;
    long long timeInit;
    scanf("%d%Ld%d%d\n",&numBoosters,&timeInit,&n,&c);
    long long sum=0;
    for(int x=0;x<c;x++)
    {
      scanf("%Ld",&dist[x]);
      long long lastSum=sum;
      sum+=dist[x]*2;
      if(sum<=timeInit)savings[x]=0;
      else if(lastSum<timeInit)savings[x]=(sum-timeInit)>>1;
      else
      {
	savings[x]=dist[x];
      }
    }
    for(int x=c;x<n;x++)
    {
      dist[x]=dist[x-c];
      long long lastSum=sum;
      sum+=dist[x]*2;
      if(sum<=timeInit)savings[x]=0;
      else if(lastSum<timeInit)savings[x]=(sum-timeInit)>>1;
      else
      {
	savings[x]=dist[x];
      }
    }
    int savedFreq[10005];
    for(int x=0;x<10005;x++)
    {
      savedFreq[x]=0;
    }
    for(int x=0;x<n;x++)
    {
      savedFreq[savings[x]]++;
    }
    long long saved=0;
    for(int x=10004;x;x--)
    {
      if(numBoosters==0)break;
      if(savedFreq[x]<=numBoosters)
      {
	numBoosters-=savedFreq[x];
	saved+=savedFreq[x]*x;
      }
      else
      {
	saved+=numBoosters*x;
	numBoosters=0;
      }
    }
    printf("Case #%d: %Ld\n",t,sum-saved);
    fflush(stdout);
  }
}