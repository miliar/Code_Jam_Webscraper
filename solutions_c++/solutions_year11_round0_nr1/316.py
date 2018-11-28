#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

struct Point {
  int t;
  int index;
  int o;
  int b;
  Point(int t, int index, int o, int b) : t(t), index(index), o(o), b(b) {;}
};

int n;
int seq[1000];
bool visit[110][110][110];

int main() {
  int test;
  int test_case = 0;
  scanf("%d", &test);
  while (test--) {
    test_case++;
    MEMSET(visit, false);
    scanf("%d", &n);
    REP(i, n) {
      char c;
      int index;
      scanf(" %c %d", &c, &index);
      seq[i] = index * (c == 'O' ? 1 : -1);
    }
    queue<Point> que;
    que.push(Point(0, 0, 1, 1));
    while (true) {
      Point p = que.front();
      que.pop();
      if (visit[p.o][p.b][p.index]) { continue; }
      visit[p.o][p.b][p.index] = true;
      if (p.index == n) {
        printf("Case #%d: %d\n", test_case, p.t);
        break;
      }
      for (int dx = -1; dx <= 1; dx++) {
        for (int dy = -1; dy <= 1; dy++) {
          int nindex = p.index;
          int nt = p.t + 1;
          int no = p.o + dx;
          int nb = p.b + dy;
          if (no <= 0 || no > 100 || nb <= 0 || nb > 100) { continue; }
          if (dx == 0 && no == seq[p.index]) { nindex++; }
          if (dy == 0 && nb == -seq[p.index]) { nindex++; }
          que.push(Point(nt, nindex, no, nb));
        }
      }
    }
  }
}
