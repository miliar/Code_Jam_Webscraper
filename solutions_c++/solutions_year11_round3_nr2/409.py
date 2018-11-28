#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <cstdlib>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <utility>
#include <cctype>
#include <list>
#include <map>
#include <limits.h>
#include <signal.h>

#define FOR(i, a, b) for ( i = a; i <= b; i++ )
#define ROF(i, a, b) for ( i = a; i >= b; i-- )
#define ALL(v) (v).begin(), (v).end()
#define MAX(a, b) ((a) >= (b) ? (a) : (b))
#define MIN(a, b) ((a) <= (b) ? (a) : (b))
#define ABS(a) ((a) < (0) ? (a)*(-1) : (a))
#define SWAP(a, b) typeof(a) T; T=a; a=b; b=T;

using namespace std;
using namespace __gnu_cxx;

long long dista[1000002],Saves[1000002];

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
      scanf("%Ld",&dista[x]);
      long long lastSum=sum;
      sum+=dista[x]*2;
      if(sum<=timeInit)Saves[x]=0;
      else if(lastSum<timeInit)Saves[x]=(sum-timeInit)>>1;
      else
      {
	Saves[x]=dista[x];
      }
    }
    
    for(int x=c;x<n;x++)
    {
      dista[x]=dista[x-c];
      long long lastSum=sum;
      sum+=dista[x]*2;
      if(sum<=timeInit)Saves[x]=0;
      else if(lastSum<timeInit)Saves[x]=(sum-timeInit)>>1;
      else
      {
	Saves[x]=dista[x];
      }
    }
    
    int savedFreq[10005];
    
    for(int x=0;x<10005;x++)
    {
      savedFreq[x]=0;
    }
    for(int x=0;x<n;x++)
    {
      savedFreq[Saves[x]]++;
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
