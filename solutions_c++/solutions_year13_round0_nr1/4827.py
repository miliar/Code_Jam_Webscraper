#include <cstdio>
using namespace std;

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define FOR(i, p, k) for(int i = (p); i <= (k); ++i)
#define FORD(i, p, k) for(int i = (p); i >= (k); --i)
#define FOREACH(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)

char B[6][6];

bool check(char p) {
  REP(r, 4) {
    bool row = true, col = true;
    REP(c, 4) {
      row &= B[r][c] == p || B[r][c] == 'T';
      col &= B[c][r] == p || B[c][r] == 'T';
    }
    if (row || col) return true;
  }
  
  bool d1 = true, d2 = true;
  REP(i, 4) {
    d1 &= B[i][i] == p || B[i][i] == 'T';
    d2 &= B[i][3 - i] == p || B[i][3 - i] == 'T';
  }
  return d1 || d2;
}

bool has_empty() {
  REP(r, 4) REP(c, 4) if (B[r][c] == '.') return true;
  return false;
}

void solve() {
  char P[] = {'X', 'O'};
  REP(p, 2) {
    if (check(P[p])) {
      printf("%c won\n", P[p]);
      return;
    }
  }
  if (has_empty()) printf("Game has not completed\n");
  else printf("Draw\n");
}

int main() {
  int Z; scanf("%d", &Z);
  FOR(t, 1, Z) {
    REP(r, 4) scanf("%s", B[r]);
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
