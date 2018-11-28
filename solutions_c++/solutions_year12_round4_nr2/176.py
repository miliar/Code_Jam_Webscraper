#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())
#define sqr(x) ((x) * (x))

typedef long long ll;

typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

struct pt {
  double x, y;
  pt(double _x = 0, double _y = 0) : x(_x), y(_y) {}
  pt operator+(const pt &p2) const { return pt(x + p2.x, y + p2.y); }
  pt operator-(const pt &p2) const { return pt(x - p2.x, y - p2.y); }
  double dist2() const { return x * x + y * y; }
};

int n, w, h;
vector<pt> res;
vi rs;

#define EPS 1e-10
bool good(const pt &p) { return 0 <= p.x && p.x <= w && 0 <= p.y && p.y <= h; }
vector<pt> cross(double a, double b, double c, double r) {
  double d2 = a * a + b * b;
  assert(d2 > EPS);
  pt cent(-a * c / d2, -b * c / d2);
//  eprintf("%.18lf\n", fabs(a * cent.x + b * cent.y + c));
//  assert(fabs(a * cent.x + b * cent.y + c) < EPS);

  double len = fabs(c / sqrt(d2));
  if (len > r + EPS) return vector<pt>();
  else if (len >= r - EPS) return vector<pt>(1, cent);
  len = sqrt(r * r - len * len);
  pt vec(-b * len / sqrt(d2), a * len / sqrt(d2));
//  assert(fabs(vec.x * a + vec.y * b) < EPS);
//  assert(fabs(vec.dist2() - len * len) < EPS);

  vector<pt> res;
  res.pb(cent + vec);
  res.pb(cent - vec);
/*  for (int i = 0; i < sz(res); i++) {
    assert(fabs(res[i].dist2() - r * r) < EPS);
    assert(fabs(a * res[i].x + b * res[i].y + c) < EPS);
  }*/
  return res;
}
vector<pt> cross(double r1, const pt &p2, double r2) {
  return cross(2 * p2.x, 2 * p2.y, -r1 * r1 + r2 * r2 - p2.x * p2.x - p2.y * p2.y, r1);
}
vector<pt> cross(const pt &p1, double r1, const pt &p2, double r2) {
  vector<pt> res = cross(r1, p2 - p1, r2);
  for (int i = 0; i < sz(res); i++)
    res[i] = res[i] + p1;
  return res;
}
vector<pt> cross(double a, double b, double c, const pt &p1, double r) {
  vector<pt> res = cross(a, b, c - p1.x * a - p1.y * b, r);
  for (int i = 0; i < sz(res); i++)
    res[i] = res[i] + p1;
  return res;
}

bool good(int a, int maxi) {
  if (res[a].x < 0 || res[a].x > w || res[a].y < 0 || res[a].y > h)
    return false;

  for (int b = 0; b < maxi; b++) if (a != b) {
    if ((res[a] - res[b]).dist2() < sqr(ll(rs[a] + rs[b])) - EPS)
      return false;
  }
  return true;
}

bool go(int i) {
  if (i >= n) return true;
  if (i == 0) {
    res[i] = pt(0, 0);
    return go(i + 1);
  }
  for (int a = 0; a < i; a++) {
    for (int b = a + 1; b < i; b++) {
      vector<pt> pts = cross(res[a], rs[a] + rs[i], res[b], rs[b] + rs[i]);
      for (int i2 = 0; i2 < sz(pts); i2++) {
        res[i] = pts[i2];
        if (good(i, i + 1))
          if (go(i + 1)) return true;
      }
    }
    const double as[] = { 1, 1, 0, 0 };
    const double bs[] = { 0, 0, 1, 1 };
    const double cs[] = { 0, -w, 0, -h };
    for (int b = 0; b < 4; b++) {
      vector<pt> pts = cross(as[b], bs[b], cs[b], res[a], rs[a] + rs[i]);
      for (int i2 = 0; i2 < sz(pts); i2++) {
        res[i] = pts[i2];
        if (good(i, i + 1))  {
          if (go(i + 1)) return true;
        }
      }
    }
  }
  return false;
}

void solve() {
  scanf("%d%d%d", &n, &w, &h);
  vector<pii> szs(n);
  for (int i = 0; i < n; i++)
    scanf("%d", &szs[i].first), szs[i].second = i;
  sort(szs.begin(), szs.end(), greater<pii>());
  rs = vi(n);
  for (int i = 0; i < n; i++)
    rs[i] = szs[i].first;

  res = vector<pt>(n, pt(-1, -1));
  bool ans = go(0);
  assert(ans);
//  for (int i = 0; i < n; i++)
//    eprintf("%.2lf %.2lf\n", res[i].x, res[i].y);

  for (int i = 0; i < n; i++)
    assert(good(i, n));
  vi out(n, -1);
  for (int i = 0; i < n; i++)
    out[szs[i].second] = i;
  for (int i = 0; i < n; i++)
    printf("%.18e %.18e%c", res[out[i]].x, res[out[i]].y, "\n "[i + 1 < n]);
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "std";
    if (argc >= 2) fn = argv[1];
    if (endsWith(fn, ".in")) fn = string(fn, 0, fn.length() - 3);
    freopen((fn + ".in").c_str(), "r", stdin);
    freopen((fn + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    eprintf("Case #%d:\n", TN);
    printf("Case #%d: ", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Catched exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
