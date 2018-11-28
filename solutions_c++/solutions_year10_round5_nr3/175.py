#include <assert.h>
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


queue<int> greater2;
map<int, int> hotd;

void testc(int tc)
{
  int c;
  scanf("%i ", &c);
  hotd.clear();
  while(!greater2.empty())
    greater2.pop();
  FOR(i,0,c)
    {
      int p,v;
      scanf("%i %i ", &p, &v);
      if (v>=2) greater2.push(p);
      hotd[p]=v;
    }

  ll steps=0;
  while(!greater2.empty())
    {
      int x=greater2.front();      greater2.pop();

      if (hotd[x]<2) continue;
      DEB("do a move at %i\n",x);
      
      hotd[x]-=2;
      hotd[x+1]++;
      hotd[x-1]++;

      for (int i=x-1;i<=x+1;i++)
        if (hotd[i]>=2)
          greater2.push(i);

      steps++;
    }
  
  printf("Case #%i: %lli\n", tc, steps);
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);
  
  return 0;
}
