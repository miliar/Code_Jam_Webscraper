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

int howmany[20];
char welcome[20] = "welcome to code jam";

int main() {
  int N;
  scanf("%d\n", &N);
  REP (test, N) {
    char str[600];
    int pos = 0;
    while (1) {
      if (scanf("%c", &str[pos]) < 1) break;
      if (str[pos++] == '\n') break;
    }
    str[pos] = 0;
    pos = 0;
    REP (i, 20) howmany[i] = 0;
    howmany[0] = 1;
    while (str[pos]) {
      REP (i, 19) if (str[pos] == welcome[i]) {
        howmany[i+1] += howmany[i];
        howmany[i+1] %= 10000;
      }
      pos++;
    }
    printf("Case #%d: %04d\n", test+1, howmany[19]);
  }
  return 0;
}