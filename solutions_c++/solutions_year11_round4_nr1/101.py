#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);
const int max_n = 1024;

int I, T;
int X, S, R, n;
Real tot, ans;

struct Walkway {
  Walkway(int xx, int yy, int ww): x(xx), y(yy), w(ww) {}
  Walkway() {}
  int x, y, w;
};
bool operator<(const Walkway &a, const Walkway &b) {
  return a.x < b.x;
}
bool by_speed(const Walkway &a, const Walkway &b) {
  return a.w < b.w;
}

vector<Walkway> a;
Walkway b[max_n];

void input() {
  scanf("%d %d %d %Lf %d", &X, &S, &R, &tot, &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d %d %d", &b[i].x, &b[i].y, &b[i].w);
  }
}

void solve() {
  sort(b, b + n);
  a.clear();
  int x = 0;
  int i = 0;
  while (x < X) {
    if (i < n && x == b[i].x) {
      a.push_back(Walkway(b[i].x, b[i].y, S + b[i].w));
      x = b[i].y;
      ++i;
    } else if (i < n) {
      a.push_back(Walkway(x, b[i].x, S));
      x = b[i].x;
    } else {
      a.push_back(Walkway(x, X, S));
      x = X;
    }
  }
  sort(a.begin(), a.end(), by_speed);
  int m = (int)a.size();

#if 0
  for (i = 0; i < m; ++i)
    fprintf(stderr, "%d %d %d\n", a[i].x, a[i].y, a[i].w);
#endif

  ans = 0;
  for (i = 0; i < m; ++i) {
    Real t = (Real)(a[i].y - a[i].x) / (a[i].w + R - S);
    if (t <= tot + o) {
      ans += t;
      tot -= t;
    } else if (tot > o) {
      ans += tot + (Real)(a[i].y - a[i].x - tot * (a[i].w + R - S)) / a[i].w;
      tot = 0;
    } else {
      ans += (Real)(a[i].y - a[i].x) / a[i].w;
    }
  }
}

void output() {
  printf("Case #%d: %.10Lf\n", I + 1, ans);
}

int main() {
  scanf("%d", &T);
  for (I = 0; I < T; ++I) {
    input();
    solve();
    output();
  }
	return 0;
}

