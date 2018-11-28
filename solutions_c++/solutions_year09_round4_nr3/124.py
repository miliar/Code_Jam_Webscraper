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

int N;
VVI c;
VI u,m;

int go (int n) {

  if (u[n]) return 0;
  u[n]=1;

  REP(i,N) if (c[n][i] && (m[i]==-1 || go(m[i]))) {
    m[i]=n;
    return 1;
  }

  return 0;
}

void solve () {

  int T;
  cin>>N>>T;

  VVI x(N,VI(T));
  REP(i,N) REP(j,T) cin>>x[i][j];

  c=VVI(N,VI(N,1));

  REP(i,N) REP(j,N) REP(t,T) 
    if (x[i][t] >= x[j][t]) c[i][j]=0;

  m=VI(N,-1);
  
  int res=0;
  REP(i,N) {
    u=VI(N,0);
    if (go(i)) res++;
  }

  cout<<N-res;
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
