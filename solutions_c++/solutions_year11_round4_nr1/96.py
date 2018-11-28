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

#define EPS 1e-6

struct Way {
  double l, v;
  bool operator<(const Way &w) const { return v < w.v - EPS; }
};

double run(double len, double s1, double delta, double &t) {
  double t1 = min(len / (s1 + delta), t);
  t -= t1;
  len -= t1 * (s1 + delta);
  double t2 = len / s1;
  return t1 + t2;
}

void solve() {
  double x, s, r, t; int n;
  scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
  r -= s;

  vector<Way> w(n);
  for (int i = 0; i < n; i++) {
    double s, e;
    scanf("%lf%lf%lf", &s, &e, &w[i].v);
    w[i].l = e - s;
    x -= w[i].l;
  }
  Way nway; nway.l = x; nway.v = 0;
  w.pb(nway); n++;
  sort(w.begin(), w.end());

  double tim = 0;
  for (int i = 0; i < n; i++)
    tim += run(w[i].l, w[i].v + s, r, t);
  printf("%.18lf\n", tim);
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
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}
