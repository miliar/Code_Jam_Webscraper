#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

long long dist[1000002],save[1000002];
int main()
{
  int T;
  scanf("%d",&T);
  for(int tc=1;tc<=T;tc++)
  {
    int l,n,c;
    long long t;
    scanf("%d%lld%d%d\n",&l,&t,&n,&c);
    long long sum=0;
    for(int i=0;i<c;i++)
    {
      scanf("%lld",&dist[i]);
      long long ls=sum;
      sum+=dist[i]*2;
      if(sum<=t)save[i]=0;
      else if(ls<t)save[i]=(sum-t)>>1;
      else
      {
	save[i]=dist[i];
      }
    }
    for(int i=c;i<n;i++)
    {
      dist[i]=dist[i-c];
      long long ls=sum;
      sum+=dist[i]*2;
      if(sum<=t)save[i]=0;
      else if(ls<t)save[i]=(sum-t)>>1;
      else
      {
	save[i]=dist[i];
      }
    }
    int sfq[10005];
    for(int i=0;i<10005;i++)
    {
      sfq[i]=0;
    }
    for(int i=0;i<n;i++)
    {
      sfq[save[i]]++;
    }
    long long saved=0;
    for(int i=10004;i;i--)
    {
      if(l==0)break;
      if(sfq[i]<=l)
      {
	l-=sfq[i];
	saved+=sfq[i]*i;
      }
      else
      {
	saved+=l*i;
	l=0;
      }
    }
    printf("Case #%d: %Ld\n",tc,sum-saved);
 
  }
}
