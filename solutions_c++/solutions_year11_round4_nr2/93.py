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

const int MAXW = 2000;
char buf[MAXW + 1];

struct pii {
  ll a, b;
  pii() : a(0), b(0) {}
  pii(ll _a, ll _b) : a(_a), b(_b) {}
  pii operator+(const pii &p) const { return pii(a + p.a, b + p.b); }
  pii operator-(const pii &p) const { return pii(a - p.a, b - p.b); }
  bool operator==(const pii &p) const { return a == p.a && b == p.b; }
};
typedef vector<pii> vpii;

template<typename T> class SumSqr {
  vector<vector<T> > ss;

  public:
  SumSqr() {}
  SumSqr(const vector<vector<T> > &f) {
    ll h = sz(f);
    ll w = sz(f[0]);
    ss = vector<vector<T> >(h + 1, vector<T>(w + 1));
    for (ll y = 0; y < h; y++) {
      for (ll x = 0; x < w; x++)
        ss[y + 1][x + 1] = ss[y + 1][x] + ss[y][x + 1] - ss[y][x] + f[y][x];
    }
  }

  T get(ll x1, ll y1, ll x2, ll y2) {
    x2++, y2++;
    return ss[y2][x2] - ss[y1][x2] - ss[y2][x1] + ss[y1][x1];
  }
};

void solve() {
  int h, w, d;
  scanf("%d%d%d", &h, &w, &d);

  vector<vpii> f(h, vpii(w));
  vector<vector<ll> > fw(h, vector<ll>(w, 0));
  for (int y = 0; y < h; y++) {
    scanf(" %s", buf);
    for (int x = 0; x < w; x++) {
      ll curw = d + buf[x] - '0';
      fw[y][x] = curw;
      f[y][x] = pii(curw * x, curw * y);
//      eprintf("%2d%c", curw, "\n "[x + 1 < w]);
    }
  }
  
  SumSqr<pii> sums(f);
  SumSqr<ll> sumsw(fw);

  ll ans = -1;
  for (int y = 0; y < h; y++)
    for (int x = 0; x < w; x++)
      for (int sz = 2; x + sz < w && y + sz < h; sz++) {
        pii sum = sums.get(x, y, x + sz, y + sz);
        ll sumw = sumsw.get(x, y, x + sz, y + sz);
        const int xs[] = { x, x + sz };
        const int ys[] = { y, y + sz };
        for (int a = 0; a < 2; a++)
        for (int b = 0; b < 2; b++) {
          sum = sum   - f [ys[b]][xs[a]];
          sumw = sumw - fw[ys[b]][xs[a]];
        }
        sum.a *= 2;
        sum.b *= 2;
        if (sum == pii((2 * x + sz) * sumw, (2 * y + sz) * sumw))
          ans = max(ans, (ll)sz + 1);
      }
  if (ans < 0)
    printf("IMPOSSIBLE\n");
  else
    printf("%I64d\n", ans);
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
