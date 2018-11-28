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

int n;
vi ds, ls;
vi was;
vi wasl, wasr;
const int INF = 2e9;

int ops;
bool dfs(int id, int len) {
  ops++;
  if (len <= was[id]) return false;
  if (id == n) return true;

  was[id] = len;

  int l = lower_bound(ds.begin(), ds.end(), ds[id] - len) - ds.begin();
  int r = upper_bound(ds.begin(), ds.end(), ds[id] + len) - ds.begin();

  for (int i = l; i < r && i < wasl[i]; i++) {
    int newl = min(ls[i], abs(ds[i] - ds[id]));
    if (dfs(i, newl)) return true;
  }
  for (int i = max(l, wasr[id]); i < r; i++) {
    int newl = min(ls[i], abs(ds[i] - ds[id]));
    if (dfs(i, newl)) return true;
  }
  wasl[id] = min(wasl[id], l);
  wasr[id] = max(wasr[id], r);
  return false;
}

void solve() {
  scanf("%d", &n);
  ds = vi(n + 1);
  ls = vi(n + 1);
  for (int i = 0; i < n; i++)
    scanf("%d%d", &ds[i], &ls[i]);
  scanf("%d", &ds[n]);

  was = vi(n + 1, -1);
  wasl = vi(n + 1, n + 2);
  wasr = vi(n + 1, -1);
  if (dfs(0, ds[0])) printf("YES\n");
  else printf("NO\n");
  eprintf("ops=%d\n", ops);
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
