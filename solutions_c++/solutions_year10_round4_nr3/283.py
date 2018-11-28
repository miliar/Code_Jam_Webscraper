#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

int field[2][110][110];

bool check(int t) {
  REP(y, 101) REP(x, 101) {
    if (field[t][y][x]) { return true; }
  }
  return false;
}

int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    MEMSET(field, 0);
    test_case++;
    int r;
    scanf("%d", &r);
    REP(i, r) {
      int x1, y1, x2, y2;
      scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
      FOREQ(x, x1, x2) {
        FOREQ(y, y1, y2) {
          field[0][y][x] = 1;
        }
      }
    }
    int ans = 0;
    while (check(ans & 1)) {
      int now = ans & 1;
      int next = (ans + 1) & 1;
      FOREQ(y, 1, 101) FOREQ(x, 1, 101) {
        if (field[now][y - 1][x] && field[now][y][x - 1]) {
          field[next][y][x] = 1;
        } else if (field[now][y][x] && (field[now][y - 1][x] || field[now][y][x - 1])) {
          field[next][y][x] = 1;
        } else {
          field[next][y][x] = 0;
        }
      }
      ans++;
    }
    printf("Case #%d: %d\n", test_case, ans);
  }
}
