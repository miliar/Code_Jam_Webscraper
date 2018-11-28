using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define UNIQUE(x) x.erase(unique(ALL(x)),x.end())
#define REP(x, hi) for (int x=0; x<(hi); x++)
#define REPD(x, hi) for (int x=((hi)-1); x>=0; x--)
#define FOR(x, lo, hi) for (int x=(lo); x<(hi); x++)
#define FORD(x, lo, hi) for (int x=((hi)-1); x>=(lo); x--)
#define FORALL(it,x) for (typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<string> VS;

const int inf = 999999999;

/////////////////////////////////////////////////////////////////////////////////////////////////

void solve () {

  LL R,K,N;
  cin>>R>>K>>N;
  
  VLL x(N);
  REP(i,N) cin>>x[i];

  LL X=0;
  REP(i,N) X+=x[i];
  
  if (X<=K) {
    printf ("%lli",X*R);
    return;
  }

  VI y(N,-1),z(N,0);
  int t=0,i=0;
  LL res=0;
  
  while (y[i]==-1 || (R-t)%(t-y[i])!=0) {
    y[i]=t;
    z[i]=res;
    X=0;
    while (X+x[i]<=K) {
      X+=x[i];
      res+=x[i];
      i=(i+1)%N;
    }
    t++;
    if (t>=R) {
      printf ("%lli",res);
      return;
    }    
  }

  res += (R-t)/(t-y[i]) * (res-z[i]);
  printf ("%lli",res);
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i: ",run);
    solve();
    printf ("\n");
  }

  return 0;
}
