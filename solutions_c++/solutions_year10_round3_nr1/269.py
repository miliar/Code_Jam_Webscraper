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
#define DEB(x...) fprintf(stderr,x);
//#define DEB

using namespace std;

#define MAXN 1005
PLL segs[MAXN];
int n;
bool testc(int nr)
{
  scanf("%i ", &n);
  ll a,b;

  FOR(i,0,n)
    scanf("%lli %lli ", &segs[i].first, &segs[i].second);


  sort(segs, segs+n);

  ll cnt=0;
  FOR(i,0,n)
    FOR(j,i+1,n)
    if (segs[j].second < segs[i].second)
      cnt++;
  printf("Case #%i: %lli\n", nr, cnt);
}


int main()
{
  int t;
  scanf("%i ",&t);
  FOR(i,0,t)
    testc(i+1);

  
  return 0;
}
