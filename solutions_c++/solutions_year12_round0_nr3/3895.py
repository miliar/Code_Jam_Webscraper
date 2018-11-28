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

void solve() {
  int l, r;
  scanf("%d%d", &l, &r);
  int ans = 0;

  vi lwas(r + 1, 0);
  int cver = 0;

  for (int a = l; a + 1 <= r; a++) {
    if ((a - l) % 100000 == 0)
      eprintf("%d/%d\n", a - l, r - l);
    cver++;

    char s[16];
    int len = 0;
    {
      int x = a;
      for (; x; x /= 10) s[len++] = '0' + x % 10;
      s[len] = 0;
      reverse(s, s + len);
    }
    for (int i = 1; i < len; i++) {
      rotate(s, s + 1, s + len);
      if (s[0] == '0') continue;

      int x;
      sscanf(s, "%d", &x);
      if (x <= a || x < l || x > r) continue;
      if (lwas[x] >= cver) continue;
      lwas[x] = cver;
      ans++;
    }
  }
  printf("%d\n", ans);
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
  char buf[100];
  fgets(buf, sizeof buf, stdin);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}

