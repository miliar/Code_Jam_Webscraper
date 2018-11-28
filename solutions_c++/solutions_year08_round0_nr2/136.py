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

const int maxt = 24*60;

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {

    int T,na,nb;
    scanf ("%i\n%i %i\n",&T,&na,&nb);

    VI a(maxt+T,0), b(maxt+T,0);

    for (int i=0; i<na; i++) {
      int h1,m1,h2,m2;
      scanf ("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
      a[h1*60+m1]--;
      b[h2*60+m2+T]++;
    }

    for (int i=0; i<nb; i++) {
      int h1,m1,h2,m2;
      scanf ("%d:%d %d:%d\n",&h1,&m1,&h2,&m2);
      b[h1*60+m1]--;
      a[h2*60+m2+T]++;
    }

    int resa=0, nowa=0;
    for (int i=0; i<maxt; i++) resa <?= nowa += a[i];

    int resb=0, nowb=0;
    for (int i=0; i<maxt; i++) resb <?= nowb += b[i];
      
    printf ("Case #%i: %i %i\n",run,-resa,-resb);
  }

  return 0;
}
