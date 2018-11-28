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

typedef long long ll;

typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

const int MAXC = 1e9;
int n;
vi xs;
vi hs;

int getLgY(int x1, int x2, int y1, int y2, int x) {
  double y = y1 + double(y2 - y1) * (x - x1) / double(x2 - x1);
  return (int)(y - 1e-8);
}

void seth(int id, int nh) {
//  eprintf("  try(%d, %d)\n", id, nh);
  if (hs[id] >= 0) assert(hs[id] >= nh);
  else {
    hs[id] = nh;
//    eprintf("  hs[%d]=%d\n", id, nh);
  }
}

void go(int pos, int l, int r, int hl, int hr) {
  if (pos >= r) return;

  int maxh = getLgY(l, r, hl, hr, pos);
  if (pos < n - 1) {
    if (xs[pos] > r) throw 0;
  } else {
    seth(pos, maxh);
    return;
  }

  if (xs[pos] == r) {
    seth(pos, maxh);
    return go(pos + 1, pos, r, hs[pos], hr);
  }

//  eprintf("%d..%d\n", pos, xs[pos]);
  go(xs[pos], l, r, hl, hr);
  assert(hs[xs[pos]] >= 0);

//  eprintf("  now %d..%d\n", pos, xs[pos]);
  if (xs[pos] < n - 1) {
    r = xs[xs[pos]];
    hr = hs[xs[xs[pos]]];
    assert(hr >= 0);
  }
  seth(pos, getLgY(xs[pos], r, hs[xs[pos]], hr, pos));
  assert(hs[pos] <= maxh);
  go(pos + 1, pos, xs[pos], hs[pos], hs[xs[pos]]);
}

void solve() {
  scanf("%d", &n);
  xs = vi(n - 1);
  for (int i = 0; i + 1 < n; i++)
    scanf("%d", &xs[i]), xs[i]--;
  assert(xs[n - 2] == n - 1);

  hs = vi(n, -1);
  try {
    go(0, -1, n, MAXC, MAXC);
  } catch (...) {
    printf("Impossible\n");
    return;
  }
//  for (int i = 0; i < n; i++)
//    eprintf("%d%c", hs[i], "\n "[i + 1 < n]);
  for (int i = 0; i < n; i++)
    assert(hs[i] >= 0 && hs[i] <= 1e9);

  for (int i = 0; i + 1 < n; i++) {
    pair<double, int> cur(2e9, -1);
    for (int i2 = i + 1; i2 < n; i2++) {
      pair<double, int> cand(-double(hs[i2] - hs[i]) / (i2 - i), i2);
      cur = min(cur, cand);
    }
    if (cur.second != xs[i])
      eprintf("%d %d != %d\n", i, xs[i], cur.second);
    assert(cur.second == xs[i]);
  }
  for (int i = 0; i < n; i++)
    printf("%d%c", hs[i], "\n "[i + 1 < n]);
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

