#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>

#define FOR(i, m, n) for (int i=m; i<n; i++)

using namespace std;

int sup[30][30];
int op[30][30];
int uvnitr[30];
int C, D, N;
int pole[120]; int pocet = 0;

int main() {
  int vstupy; scanf("%d", &vstupy);
  FOR (qq, 0, vstupy) {
    char c1, c2, c3; pocet = 0;
    FOR (i, 0, 30) FOR (j, 0, 30) { sup[i][j] = -1; op[i][j] = -1; }
    FOR (i, 0, 30) uvnitr[i] = 0;
    scanf("%d", &C);
    FOR (i, 0, C) {
      scanf(" %c%c%c", &c1, &c2, &c3);
      sup[c1-'A'][c2-'A'] = c3-'A';
      sup[c2-'A'][c1-'A'] = c3-'A';
    }
    scanf("%d", &D);
    FOR (i, 0, D) {
      scanf(" %c%c", &c1, &c2);
      op[c1-'A'][c2-'A'] = 1;
      op[c2-'A'][c1-'A'] = 1;
    }
    scanf("%d", &N);
    FOR (i, 0, N) {
      scanf(" %c", &c1); int a = c1-'A';
      do {
        if (pocet>0 && sup[pole[pocet-1]][a]!=-1) {
           uvnitr[pole[pocet-1]]--; a = sup[pole[pocet-1]][a]; pocet--; continue;
        }
        FOR (j, 0, 26) {
          if (uvnitr[j]>0 && op[j][a]==1) {
            pocet = 0;
            FOR (k, 0, 26) uvnitr[k] = 0;
            goto ven;
          }
        }
        pole[pocet++] = a; uvnitr[a]++; break;
      }while(1);
ven: ;
    }
    printf("Case #%d: [", qq+1);
    FOR (i, 0, pocet) {
      printf("%c", pole[i]+'A');
      if (i+1<pocet)
        printf(", ");
    }
    printf("]\n");
  }
  return 0;
}
