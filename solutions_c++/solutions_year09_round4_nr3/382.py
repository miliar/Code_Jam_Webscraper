#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;

/* PREWRITTEN CODE */

#define ALL(x) x.begin(),x.end()
#define PB push_back


#define FOR(i,p,k) for (int i=p; i<k; i++)
#define REP(i,n) for (int i=0; i<n; i++)
#define SIZE(x) (int)x.size()
/* COMPETITION CODE */

int tab[200][200];
int cross[200][200];
int N, K;

int main () {
  int number_of_tests;
  scanf("%d", &number_of_tests);
  REP (test_number, number_of_tests) {
    printf("Case #%d:", test_number+1);
    scanf("%d %d", &N, &K);
    REP (i, N) REP (j, N) cross[i][j] = 0;
    REP (i, N) REP (j, K) scanf("%d", &tab[i][j]);
    REP (i, N) REP (j, i) REP (k, K-1) {
      if (tab[i][k] == tab[j][k]) cross[i][j] = 1;
      if (tab[i][k+1] == tab[j][k+1]) cross[i][j] = 1;
      if (tab[i][k] > tab[j][k] && tab[i][k+1] < tab[j][k+1]) cross[i][j] = 1;
      if (tab[i][k] < tab[j][k] && tab[i][k+1] > tab[j][k+1]) cross[i][j] = 1;
    }
    int best = 0;
    REP (mask, 1 << N) {
      int siz = 0;
      int ok = 1;
      REP (i, N) if (mask & (1<<i)) siz++;
      if (siz > best) REP (i, N) REP (j, i) if ((mask & (1<<i)) && (mask & (1<<j))) 
        if (!cross[i][j]) ok = 0;
      if (ok && siz > best) best = siz;
    }
    printf(" %d\n", best);
  }
  return 0;
}

