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

const int MAXV = 10000;

bool can(const vi &a, int len) {
  int n = sz(a);
  vi has(MAXV + 10, 0);
  vb used(n, false);
  for (int i = 0; i < n; i++) if (!used[i]) {
    if (has[a[i]]) { has[a[i]]--; has[a[i] + 1]++; used[i] = true; continue; }

//    eprintf("i=%d, a[i]=%d\n", i, a[i]);
    int val = a[i];
    for (int i2 = i; i2 < n && val <= a[i] + len - 1; i2++) {
      if (!used[i2] && a[i2] == val) {
//        eprintf(" add i2=%d, a[i2]=%d\n", i2, a[i2]);
        used[i2] = true;
        val++;
      }
    }
    if (val < a[i] + len) return false;
    has[val]++;
  }

  return true;
}

void solve() {
  int n;
  scanf("%d", &n);

  vi a(n);
  for (int i = 0; i < n; i++) scanf("%d", &a[i]);
  sort(a.begin(), a.end());

  #ifdef DEBUG
  bool pval = true;
  for (int x = 0; x <= n; x++) {
    bool cval = can(a, x);
    assert(pval >= cval);
    pval = cval;
  }
  #endif

  int L = 0, R = n + 1;
  while (L + 1 < R) {
    int M = (L + R) / 2;
    if (can(a, M)) L = M;
    else R = M;
  }
  printf("%d\n", L);
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
