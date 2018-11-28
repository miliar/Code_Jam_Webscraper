#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

struct pt {
  double x, y;
  pt() : x(0), y(0) {}
  pt(double _x, double _y) : x(_x), y(_y) {}
  pt operator-(const pt &p2) const { return pt(x - p2.x, y - p2.y); }
  double operator*(const pt &p2) const { return x * p2.y - y * p2.x; }
};

#define EPS 1e-7

pt cross(pt p1, pt p2, double x) {
  if (p1.x >= p2.x - EPS) swap(p1, p2);
  if (x < p1.x - EPS && x < p2.x - EPS) throw 0;
  if (x > p1.x + EPS && x > p2.x + EPS) throw 0;
  double vx = p2.x - p1.x;
  double vy = p2.y - p1.y;
  return pt(x, p1.y + (x - p1.x) * vy / vx);
}

double getsq(const vector<pt> &pts, double x2) {
  int n = sz(pts) - 1;
  vector<pt> npts(0);

  for (int i = 0; i < n; i++) {
    pt p1 = pts[i], p2 = pts[i + 1];
    bool i1 =  p1.x <= x2 + EPS;
    bool i2 =  p2.x <= x2 + EPS;
    if (i1 != i2) {
      try {
        npts.pb(cross(p1, p2, x2));
      } catch (...) {}
    }
    if (i2)
      npts.pb(p2);
  }

  if (!sz(npts)) return 0;
  npts.pb(npts[0]);
  double sq = 0;
  for (int i = 0; i + 1 < sz(npts); i++) {
    sq += npts[i] * npts[i + 1];
//    eprintf("  %.2lf %.2lf\n", npts[i].x, npts[i].y);
  }
  return fabs(sq) / 2;
}

void solve() {
  double w;
  int n1, n2, cnt;
  scanf("%lf%d%d%d", &w, &n1, &n2, &cnt);

  vector<pt> pts(0);
  for (int st = 0; st < 2; st++) {
    int n = st == 0 ? n1 : n2;
    vector<pt> cpt(n);
    for (int i = 0; i < n; i++)
      scanf("%lf%lf", &cpt[i].x, &cpt[i].y);
    if (st == 1)
      reverse(cpt.begin(), cpt.end());
    for (int i = 0; i < n; i++)
      pts.pb(cpt[i]);
  }

  pts.pb(pts[0]);
  int n = sz(pts);
  double sq = getsq(pts, w);
  eprintf("sq=%.8lf, psq=%.8lf\n", sq, sq / cnt);

  vector<double> res(cnt - 1);
  double x2 = w;
  for (int i = 0; i < sz(res); i++) {
    double l = 0, r = x2;
    double nsq = sq * (i + 1) / cnt;
    for (int step = 0; step < 500; step++) {
      double m = (l + r) / 2;
      if (getsq(pts, m) < nsq) l = m;
      else r = m;
    }
    res[i] = l;
/*    eprintf("fefr=========================== %.2lf\n", l);
    getsq(pts, l);
    exit(0);*/
  }
  for (int i = 0; i < sz(res); i++)
    printf("%.18lf\n", res[i]);
}

int main(int argc, char* argv[]) {
  {
    string fname = "std";
    if (argc >= 2) {
      fname = argv[1];
      if (fname.length() >= 3 && string(fname, fname.length() - 3) == ".in")
        fname = string(fname, 0, fname.length() - 3);
    }
    freopen((fname + ".in").c_str(), "r", stdin);
    freopen((fname + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d:\n", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}
