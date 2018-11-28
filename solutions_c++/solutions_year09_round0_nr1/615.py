#include <string>
#include <vector>
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

int L, D, N;

char sl[6000][20];
int map[200][20];

void debug_map() {
  REP (i, 20) {
    int cnt = 0;
    REP (j, 200) cnt += map[j][i];
    if (cnt == 0) printf("-");
    if (cnt == 1) REP (j, 200) if (map[j][i]) printf("%c", j);
    if (cnt > 1) {printf("("); REP (j, 200) if (map[j][i] && j != '(' && j != ')') printf("%c", j); printf(")");}
  }
  printf("\n");
}
    
int main() {
  scanf("%d %d %d", &L, &D, &N);
  REP (i, D) scanf("%s", sl[i]);
  REP (test, N) {
    REP (j, 200) REP (k, 20) map[j][k] = 0;
    char slowo[600];
    scanf("%s", slowo);
    int z = 0;
    int pos = -1;
    int opened = 0;
    while (slowo[z]) {
      if (slowo[z] == '(') {pos++; opened = 1;}
      if (!opened) pos++;
      if (slowo[z] == ')') {opened = 0;}
      map[slowo[z]][pos] = 1;
      z++;
    }
//    debug_map();
    int cnt = 0;
    REP (j, D) {
      int l = 0;
      while (map[sl[j][l]][l] && l < L) l++;
      if (l == L) cnt++;
    }
    printf("Case #%d: %d\n", test+1, cnt);
  }
  return 0;
}

