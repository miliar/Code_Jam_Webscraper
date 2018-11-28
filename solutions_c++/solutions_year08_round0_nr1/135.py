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

    int N;
    scanf ("%i\n",&N);
    map<string,int> m;
    REP(i,N) {
      char x[10000];
      fgets(x,10000,stdin);
      m[x]=i;
    }

    int S;
    scanf ("%i\n",&S);
    VI n(S);
    REP(i,S) {
      char x[10000];
      fgets(x,10000,stdin);
      n[i]=m[x];
    }

    int res=0;
    VI u(N,0);
    int nu=0;
    
    REP(i,S) {
      if (u[n[i]]) continue;
      u[n[i]]=1;
      nu++;

      if (nu==N) {
	res++;
	u=VI(N,0);
	u[n[i]]=1;
	nu=1;
      }
    }

    printf ("Case #%i: %i\n",run, res);
  }

  return 0;
}
