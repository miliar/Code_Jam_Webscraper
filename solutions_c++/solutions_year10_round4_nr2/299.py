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

int P,M;
VI miss;
VI cost;
VVI cache;

int go (int m, int n) {
 
  if (m>=M) {
    m-=M;
    if (n>miss[m]) return inf;
    return 0;
  }

  if (cache[m][n]!=-1) return cache[m][n];

  cache[m][n] = inf;
  cache[m][n] <?= go(2*m+1,n+1) + go(2*m+2,n+1);
  cache[m][n] <?= go(2*m+1,n)   + go(2*m+2,n) + cost[m];

  return cache[m][n];
}
	
void solve () {

  cin>>P;
  M=(1<<P)-1;
  
  miss=VI(1<<P);
  REP(i,miss.SZ) cin>>miss[i];
  cost=VI(M);
  REP(i,P) 
    REP(j,1<<(P-1-i)) cin>>cost[(1<<(P-1-i))+j-1];
  
  cache=VVI(M,VI(P+1,-1));
  cout<<go(0,0);  
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
