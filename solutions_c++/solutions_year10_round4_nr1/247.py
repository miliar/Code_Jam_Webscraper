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

#define REP(i, n) for (ll i = 0; i < (ll)(n); i++)
#define FOR(i, s, n) for (ll i = (s); i < (ll)(n); i++)
#define FOREQ(i, s, n) for (ll i = (s); i <= (ll)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (ll i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())

int k;
int field[500][500];
int OFFSETX = 210;
int OFFSETY = 210;

ll square(ll x) { return x * x; }

inline int GET(int x, int y) {
  return field[y + OFFSETY][x + OFFSETX];
}
inline void SET(int x, int y, int value) {
  field[y + OFFSETY][x + OFFSETX] = value;
}

bool check(int discard, int dir) {
  int localk = k - discard;
  OFFSETY = 210;
  OFFSETX = 210;
  if (dir == 0 || dir == 2) {
    if (dir == 0) {
      OFFSETX += discard;
    } else {
      OFFSETX -= discard;
    }
    FOREQ(y, -(localk - 1), (localk - 1)) {
      REP(i, localk - abs(y)) {
        int x = -(localk - abs(y) - 1) + i * 2;
        //cout << discard << " " << localk << " " << dir << " " << x << " " << y << " " << GET(x, y) << " " << GET(-x, y) << endl;
        assert(GET(x, y) != -1);
        if (GET(x, y) != GET(-x, y)) { return false; }
      }
    }
  } else {
    if (dir == 1) {
      OFFSETY += discard;
    } else {
      OFFSETY -= discard;
    }
    FOREQ(y, -(localk - 1), (localk - 1)) {
      REP(i, localk - abs(y)) {
        int x = -(localk - abs(y) - 1) + i * 2;
        assert(GET(x, y) != -1);
        if (GET(x, y) != GET(x, -y)) { return false; }
      }
    }
  }

  OFFSETY = 210;
  OFFSETX = 210;
  return true;
}

int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    OFFSETY = 210;
    OFFSETX = 210;
    MEMSET(field, -1);
    scanf("%d", &k);
    FOREQ(y, -(k - 1), (k - 1)) {
      REP(i, k - abs(y)) {
        int v;
        scanf("%d", &v);
        int x = -(k - abs(y) - 1) + i * 2;
        SET(x, y, v);
      }
    }
    ll xsize = 100;
    ll ysize = 100;
    REP(i, 1000) {
      if (check(i, 0)) {
        xsize = min(xsize, i);
        break;
      }
    }
    REP(i, 1000) {
      if (check(i, 2)) {
        xsize = min(xsize, i);
        break;
      }
    }
    REP(i, 1000) {
      if (check(i, 1)) {
        ysize = min(ysize, i);
        break;
      }
    }
    REP(i, 1000) {
      if (check(i, 3)) {
        ysize = min(ysize, i);
        break;
      }
    }
    //cout << xsize << " " << ysize << endl;
    ll ans = square(xsize + ysize + k) - k * k;
    assert(ans >= 0);
    printf("Case #%d: %lld\n", test_case, ans);
  }
}
