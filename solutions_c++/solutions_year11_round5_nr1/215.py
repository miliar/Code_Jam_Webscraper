#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

struct P {
  double x, y;
  P(double _x = 0, double _y = 0) : x(_x), y(_y) {}
  void read() {
    cin >> x >> y;
  }
};

P p[256];

bool cmp_l(const P & a, const P & b) {
  return a.x < b.x;
}

bool cmp_r(const P & a, const P & b) {
  return a.x > b.x;
}

double area(const P* s, const P *e) {
  double ans = 0;
  const P * r = s;
  while (r != e) {
    const P * n = r + 1;
    if (n == e) n = s;
    ans += r->x * n->y - r->y * n->x;
    ++r;
  }
  return ans;
}

P calc(P a, P b, double x) {
  return P(x, (x - a.x) * (b.y - a.y) / (b.x-a.x) + a.y);
}

void solve () {
  int W, L, U, G;
  cin >> W >> L >> U >> G;

  memset(p, 0, sizeof(p));
  
  for (int i = 0; i < L; ++i)
    p[i].read();

  for (int i = 0; i < U; ++i)
    p[i + L].read();

  sort(p, p + L, cmp_l);
  sort(p + L, p + L + U, cmp_r);
  double dt = area(p, p + L + U) / G;
  double ls = 0;
  for (int i = 1; i < G; ++i) {
    std::vector<P> ps;
    double e = dt * i;
    double l = ls, r = W;
    while (r - l > 1e-7) {
      double m = (l + r) / 2;
      ps.clear();
      for (int i = 0; i < L; ++i)
	if (p[i].x < m) {
	  ps.push_back(p[i]);
	  if (p[i + 1].x >= m) {
	    ps.push_back(calc(p[i], p[i +1], m));
	    break;
	  }
	} 
      for (int i = 0; i < U; ++i) {
	if (p[i + L].x >= m) {
	  if (p[i + L +1].x < m) {
	    ps.push_back(calc(p[i + L], p[i + L +1], m));
	  }
	} else ps.push_back(p[i + L]);
      }
      //for (int i = 0; i < ps.size(); ++i) {
      //cout << ps[i].x << "," << ps[i].y << " ";
      //      } cout << endl;
      if (area(&ps[0], &ps[0] + ps.size()) < e) l = m; else r = m;
    }
    ls = l;
    printf("%.7f\n", ls);
  }
}


int main() {
  freopen("input.txt", "r", stdin);
  int T, tc = 0;
  cin >> T;
  while (T--) {
    printf("Case #%d:\n", ++tc);
    solve();
    printf("\n");
  }
  return 0;
}
