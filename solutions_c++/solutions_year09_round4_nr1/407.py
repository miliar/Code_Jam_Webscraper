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

int tab[60];
int N;
int res;

void mama (int k, int l) {
  res += 1;
  tab[k] ^= tab[l];
  tab[l] ^= tab[k];
  tab[k] ^= tab[l];
}

int main () {
  int number_of_tests;
  scanf("%d", &number_of_tests);
  REP (test_number, number_of_tests) {
    res = 0;
    printf("Case #%d:", test_number+1);
    scanf("%d", &N);
    char buf[500];
    REP (i, N) {
      scanf("%s", buf);
      tab[i] = 0;
      REP (j, N) if (buf[j] == '1') tab[i] = j;
    }
    for (int i = 0; i < N; i++) {
      int best = i;
      while (tab[best] > i) best++;
      while (best > i) {
        mama(best, best-1);
        best -= 1;
      }
    }
    printf(" %d\n", res);
  }
  return 0;
}

