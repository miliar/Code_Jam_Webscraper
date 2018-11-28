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
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define REP(v, hi) for (int v=0; v<(hi); v++)
#define REPD(v, hi) for (int v=((hi)-1); v>=0; v--)
#define FOR(v, lo, hi) for (int v=(lo); v<(hi); v++)
#define FORD(v, lo, hi) for (int v=((hi)-1); v>=(lo); v--)
 
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector <string> VS;

const int inf = 999999;

int N;
VI node,change;
VVI cache;

int go (int n, int v) {

  int &res = cache[n][v];
  if (res!=-1) return res;

  res=inf;
  if (n>=(N-1)/2) {
    if (node[n] == v) res=0;
    //    printf ("%i %i -> %i\n",n,v,res);
    return res;
  }

  REP(v1,2) REP(v2,2) REP(op,2) {
    int c1 = go(2*n+1,v1);
    int c2 = go(2*n+2,v2);
    int c3 = change[n] ? 1 : inf;
    if (op == node[n]) c3=0;

    //    if (n==3) printf ("%i %i %i %i -> %i %i %i\n",n,v1,v2,op,c1,c2,c3);
    if (op==0 && (v1||v2)==v) res <?= c1+c2+c3;
    if (op==1 && (v1&&v2)==v) res <?= c1+c2+c3;
  }

  //  printf ("%i(%i) -> %i\n",n,v,res);
  return res;
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    int V;
    scanf ("%i %i",&N,&V);
    node=change=VI(N,0);
    REP(i,(N-1)/2) scanf ("%i %i",&node[i],&change[i]);
    REP(i,(N+1)/2) scanf ("%i",&node[(N-1)/2+i]);

    cache=VVI(N,VI(2,-1));
    int res = go(0,V);
    printf ("Case #%i: ",run);
    if (res==inf)
      printf ("IMPOSSIBLE\n");
    else
      printf ("%i\n",res);
  }

  return 0;
}
