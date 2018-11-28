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
typedef vector <string> VS;
 
int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {

    int P,K,L;
    scanf ("%i %i %i",&P,&K,&L);

    vector<int> n(L);
    REP(i,L) scanf ("%i",&n[i]);

    sort(n.rbegin(),n.rend());

    long long res=0;
    REP(i,L) res += (i/K+1) * n[i];
      
    printf ("Case #%i: %lli\n",run, res);
  }

  return 0;
}
