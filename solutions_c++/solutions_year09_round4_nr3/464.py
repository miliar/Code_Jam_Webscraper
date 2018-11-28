#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <cassert>
using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, (n))

int n, k, seen[200], p[200][200], a[200][200];

int cache[1 << 17], help[1 << 17];

int is_okay(int x, int y) {
  if (x == y) return 1;

  REP(i, k)
    if (p[x][i] == p[y][i]) return 0;

  FOR(i, 1, k) {
    if (p[x][i-1] > p[y][i-1] && p[x][i] < p[y][i]) return 0;
    if (p[x][i-1] < p[y][i-1] && p[x][i] > p[y][i]) return 0;
  }

  return 1;
}

int check(int b) {
  int & ret = help[b];
  if (ret != -1) return ret;

  REP(i, n) 
    if ((1 << i) & b)
      REP(j, i) 
	if ((1 << j) & b)
	  if (a[i][j] == 0) return ret = 0;
  return ret = 1;
}

int cal(int b) {
  if (b == 0) return 0;
  int & ret = cache[b];
  if (ret != -1) return ret;

  ret = 1000;
  for (int i = b; i > 0; i = b & (i - 1)) {
    if ((i & b) == i && check(i)) {
      ret = min(ret, cal(b - i) + 1);
    }
  }
  return ret;
}


int main() {
  int N;
  cin >> N;
  for (int C = 1; C <= N; ++C) {
    cin >> n >> k;
    REP(i, n) REP(j, k) cin >> p[i][j];
    REP(i, n) REP(j, n) a[i][j] = is_okay(i, j);
    memset(cache, -1, sizeof cache);
    memset(help, -1, sizeof help);
    cout << "Case #" << C << ": " << cal((1 << n) - 1) << endl;
  }
}
