#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string>
#include <list>
#include <stack>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <list>
#define INF 0x3fffffff


typedef long long ll;
#define PII pair<int, int>
#define PLL pair<ll, ll>
#define PDD pair<double, double>
#define PIL pair<int, ll>
#define PLI pair<ll, int>
#define PID pair<int, double>
#define PDI pair<double, int>
#define PLD pair<ll, double>
#define PDL pair<double, ll>

#define PQ(x) priority_queue< x >  //highest first
#define PQR(x) priority_queue< x , vector< x > , greater < x > > //lowest first
#define V(x) vector< x > 
#define L(x) list< x > 
#define MP make_pair
#define PB push_back
#define IT(x) for (typeof((x).begin()) it = (x).begin() ; it != (x).end() ; it++)
#define IT2(x) for (typeof((x).begin()) it2 = (x).begin() ; it2 != (x).end() ; it2++)
#define FOR(i, a, b) for (int i = (a) ; i< (b) ; i++)
//#define DEB(x...) fprintf(stderr,x);
#define DEB

using namespace std;

#define MAXN 1005

ll g[MAXN];
ll sum[MAXN];
int jmp[MAXN];
ll total;

bool visit[MAXN];
int loopstart;
void loop(int cur)
{
  if (visit[cur])
    loopstart=cur;
  else
    {
      visit[cur]=true;
      loop(jmp[cur]);
    }
}

ll testc()
{
  int N;
  ll R,k;
  total=0;
  scanf("%lli %lli %i ", &R, &k, &N);
  FOR(i,0,N) scanf("%lli ", g+i);
  FOR(i,0,N) total+=g[i];
  FOR(i,0,N)
    {
      visit[i]=0;
      sum[i]=0;
      int j=i;
      while(sum[i] + g[j]<=k)
        {
          sum[i]+=g[j];
          if (sum[i]==total) break;

          j=(j+1)%N;
        }
      jmp[i]=j;
      DEB("jmp[%i]=%i\n", i, j);
    }

  loop(0);
  ll len=0,cost=0,res=0;
  int cur=0;


  //start
  for(;;)
    {
      if (!R) break;
      if (cur==loopstart) break;
      res+=sum[cur];
      cur=jmp[cur];
      R--;
    }

  if (!R) return res;

  //loop
  do{
    len++;
    cost+=sum[cur];
    cur=jmp[cur];
  }while(cur!=loopstart);

  ll x=R/len;
  res+=x*cost;
  R=R-x*len;

  //end
  cur=loopstart;
  while(R--)
    {
      res+=sum[cur];
      cur=jmp[cur];
    }
  return res;
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    printf("Case #%i: %lli\n",i+1, testc());
  
  return 0;
}
