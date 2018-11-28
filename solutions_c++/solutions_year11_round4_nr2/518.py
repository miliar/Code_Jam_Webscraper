#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

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

void solve();
int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    printf("Case #%d: ", test_case);
    //puts("");
    solve();
  }
}

int h, w;
ll d;
ll field[600][600];
ll sum[600][600];
ll xsum[600][600];
ll ysum[600][600];

void solve() {
  scanf("%d %d %lld", &h, &w, &d);
  MEMSET(field, 0);
  MEMSET(sum, 0);
  MEMSET(xsum, 0);
  MEMSET(ysum, 0);
  REP(y, h) {
    REP(x, w) {
      int v;
      scanf("%1d", &v);
      field[y + 1][x + 1] = v + d;

      sum[y + 1][x + 1] = field[y + 1][x + 1] + sum[y + 1][x] + sum[y][x + 1] - sum[y][x];
      xsum[y + 1][x + 1] = (x + 1) * field[y + 1][x + 1] + xsum[y + 1][x] + xsum[y][x + 1] - xsum[y][x];
      ysum[y + 1][x + 1] = (y + 1) * field[y + 1][x + 1] + ysum[y + 1][x] + ysum[y][x + 1] - ysum[y][x];
    }
  }
  int ans = 0;

  // odd
  FOREQ(y, 1, h) {
    FOREQ(x, 1, w) {
      FOREQ(k, 1, 1000) {
        if (x - k <= 0 || x + k > w || y - k <= 0 || y + k > h) { break; }
        int left = x - k - 1;
        int right = x + k;
        int top = y - k - 1;
        int bottom = y + k;
        ll s1 = sum[bottom][right] - sum[bottom][left] - sum[top][right] + sum[top][left];
        ll s2 = xsum[bottom][right] - xsum[bottom][left] - xsum[top][right] + xsum[top][left];
        ll s3 = ysum[bottom][right] - ysum[bottom][left] - ysum[top][right] + ysum[top][left];

        s1 -= field[y + k][x + k] +
              field[y - k][x + k] +
              field[y + k][x - k] +
              field[y - k][x - k];
        s2 -= (x + k) * field[y + k][x + k] +
              (x + k) * field[y - k][x + k] +
              (x - k) * field[y + k][x - k] +
              (x - k) * field[y - k][x - k];
        s3 -= (y + k) * field[y + k][x + k] +
              (y - k) * field[y - k][x + k] +
              (y + k) * field[y + k][x - k] +
              (y - k) * field[y - k][x - k];
        assert(s1 >= 0);
        assert(s2 >= 0);
        assert(s3 >= 0);

        s2 -= x * s1;
        s3 -= y * s1;
        if (s2 == 0 && s3 == 0) { ans = max(ans, k * 2 + 1); }
      }
    }
  }

  // even
  FOREQ(y, 0, h) {
    FOREQ(x, 0, w) {
      FOREQ(k, 2, 1000) {
        if (x + 2 * k > w || y + 2 * k > h) { break; }
        int left = x;
        int right = x + 2 * k;
        int top = y;
        int bottom = y + 2 * k;
        ll s1 = sum[bottom][right] - sum[bottom][left] - sum[top][right] + sum[top][left];
        ll s2 = xsum[bottom][right] - xsum[bottom][left] - xsum[top][right] + xsum[top][left];
        ll s3 = ysum[bottom][right] - ysum[bottom][left] - ysum[top][right] + ysum[top][left];

        s1 -= field[y + 2 * k][x + 2 * k] +
              field[y + 1][x + 2 * k] +
              field[y + 2 * k][x + 1] +
              field[y + 1][x + 1];
        s2 -= (x + 2 * k) * field[y + 2 * k][x + 2 * k] +
              (x + 2 * k) * field[y + 1][x + 2 * k] +
              (x + 1) * field[y + 2 * k][x + 1] +
              (x + 1) * field[y + 1][x + 1];
        s3 -= (y + 2 * k) * field[y + 2 * k][x + 2 * k] +
              (y + 1) * field[y + 1][x + 2 * k] +
              (y + 2 * k) * field[y + 2 * k][x + 1] +
              (y + 1) * field[y + 1][x + 1];

        assert(s1 >= 0);
        assert(s2 >= 0);
        assert(s3 >= 0);

        s2 *= 2;
        s3 *= 2;

        s2 -= (2 * x + 2 * k + 1) * s1;
        s3 -= (2 * y + 2 * k + 1) * s1;
        if (s2 == 0 && s3 == 0) { ans = max(ans, k * 2); }
      }
    }
  }

  if (ans == 0) {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%d\n", ans);
  }
}
