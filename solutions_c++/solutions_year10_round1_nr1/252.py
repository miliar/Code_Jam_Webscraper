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

int field[100][100];
int n, k;

void printField() {
  REP(y, n) {
    REP(x, n) {
      if (field[y][x] == 0) {
        putchar('.');
      } else if (field[y][x] == 1) {
        putchar('R');
      } else {
        putchar('B');
      }
    }
    puts("");
  }
}

bool check(int color) {
  REP(y, n) {
    int suc = 0;
    REP(x, n) {
      if (field[y][x] == color) {
        suc++;
        if (suc == k) { return true; }
      } else {
        suc = 0;
      }
    }
  }
  REP(x, n) {
    int suc = 0;
    REP(y, n) {
      if (field[y][x] == color) {
        suc++;
        if (suc == k) { return true; }
      } else {
        suc = 0;
      }
    }
  }
  int inix = 0;
  int iniy = 0;
  int dir = 0;
  const int dx[4] = { 1, 0, -1, 0 };
  const int dy[4] = { 0, 1, 0, -1 };
  REP(i, 4 * n - 4) {
    if (i != 0 && (i % (n - 1)) == 0) {
      dir++;
    }
    int suc = 0;
    int x = inix;
    int y = iniy;
    REP(j, 2 * n) {
      if (x < 0 || x >= n || y < 0 || y >= n) { break; }
      if (field[y][x] == color) {
        suc++;
        if (suc == k) { return true; }
      } else {
        suc = 0;
      }
      x++;
      y++;
    }
    suc = 0;
    REP(j, 2 * n) {
      if (x < 0 || x >= n || y < 0 || y >= n) { break; }
      if (field[y][x] == color) {
        suc++;
        if (suc == k) { return true; }
      } else {
        suc = 0;
      }
      x--;
      y++;
    }
    inix += dx[dir];
    iniy += dy[dir];
  }
  return false;
}

int main() {
  int test;
  int test_case = 0;
  scanf("%d", &test);
  while (test--) {
    test_case++;
    scanf("%d %d", &n, &k);
    MEMSET(field, 0);
    REP(y, n) REP(x, n) {
      char c;
      scanf(" %c ", &c);
      if (c == '.') {
        field[x][n - y - 1] = 0;
      } else if (c == 'R') {
        field[x][n - y - 1] = 1;
      } else {
        field[x][n - y - 1] = 2;
      }
    }
    REP(iter, n) {
      for (int y = n - 1; y > 0; y--) {
        REP(x, n) {
          if (field[y][x] == 0) {
            field[y][x] = field[y - 1][x];
            field[y - 1][x] = 0;
          }
        }
      }
    }
    bool red = check(1);
    bool blue = check(2);
    printf("Case #%d: ", test_case);
    if (red && blue) {
      puts("Both");
    } else if (red) {
      puts("Red");
    } else if (blue) {
      puts("Blue");
    } else {
      puts("Neither");
    }
  }
}
