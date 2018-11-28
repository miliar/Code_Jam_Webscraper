#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <iostream>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define debug(...) fprintf(stderr, __VA_ARGS__)
#define sz(a) (int)((a).size())
#define all(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;

typedef vector <pair <int, pii> > vp;

#define maxn 1010
int T;
double x[maxn], y[maxn];
int r[maxn];
int W, L, N;

vector <pair <int, vp> > rs;

int rx[maxn], ry[maxn];

void shift(pair <int, vp> &v, int dx, int dy) {
  for (int i = 0; i < sz(v.y); i++) {
    v.y[i].y.x += dx;
    v.y[i].y.y += dy;
  }
}

void add(pair <int, vp> &v1, const pair <int, vp> &v2) {
  for (int i = 0; i < sz(v2.y); i++) {
    v1.y.pb(v2.y[i]);
  }
}

void proc(pair <int, vp> &v) {
  for (int i = 0; i < sz(v.y); i++) {
    int id = v.y[i].x;
    rx[id] = v.y[i].y.x + r[id] / 2;
    if (rx[id] > W) rx[id] -= r[id] / 2;
    ry[id] = v.y[i].y.y + r[id] / 2;
    if (ry[id] > L) ry[id] -= r[id] / 2;
  }
}


int main() {
  scanf("%d", &T);
  for (int q = 1; q <= T; q++) {
    scanf("%d %d %d", &N, &W, &L);
    for (int i = 0; i < N; i++) {
      scanf("%d", &r[i]);
      r[i] *= 2;
    }

    rs.clear();

    for (int i = 0; i < N; i++) {
      vp tmp;
      tmp.pb(mp(i, pii(0, 0)));
      rs.pb(mp(r[i], tmp));
    }

    sort(all(rs));
    reverse(all(rs));

    for (;;) {
      for (int i = 0; i < sz(rs); i++) {
        debug("%d%c", rs[i].x, " \n"[i + 1 == sz(rs)]);
      }

      if (sz(rs) < 4) break;
      if (rs[sz(rs) - 4].x + rs[sz(rs) - 3].x > min(L, W)) {
        break;
      }
      pair <int, vp> a = rs[sz(rs) - 4],
                     b = rs[sz(rs) - 3],
                     c = rs[sz(rs) - 2],
                     d = rs[sz(rs) - 1];
      rs.resize(sz(rs) - 4);
      int r1 = a.x, r2 = b.x;
      shift(b, r1, 0);
      shift(c, 0, r1);
      shift(d, r1, r1);

      a.x += r2;
      add(a, b);
      add(a, c);
      add(a, d);
      rs.pb(a);

      reverse(all(rs));
      sort(all(rs));
      reverse(all(rs));
    }

    int dx = 0, dy = 0;
    for (int i = 0; i < sz(rs); i++) {
      shift(rs[i], dx, dy);
      proc(rs[i]);
      if (W < L) {
        dy += rs[i].x;
      } else {
        dx += rs[i].x;
      }
    }

    debug("checking case %d\n", q);
    for (int i = 0; i < N; i++) {
      for (int j = i + 1; j < N; j++) {
        assert(abs(rx[i] - rx[j]) >= r[i] /2 + r[j] / 2 || abs(ry[i] - ry[j]) >= r[i] /2 + r[j] / 2);
      }
    }

    printf("Case #%d:", q);
    for (int i = 0; i < N; i++) {
      printf(" %d %d", rx[i], ry[i]);
      assert(rx[i] <= W && ry[i] <= L);
    }
    puts("");
  }
  

  return 0;
}
