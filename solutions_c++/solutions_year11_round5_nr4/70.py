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

bool check(ll x) {
  ll r = sqrt(x);
  return r * r == x;
}

const int MAXL = 125;
char s[MAXL + 1];

void solve() {
  scanf("%s", s);
  ll num = 0;
  ll msk = 0;
  ll off = 1;
  for (int i = strlen(s) - 1; i >= 0; i--, off <<= 1) {
    if (s[i] == '?') msk |= off;
    else if (s[i] == '1') num |= off;
  }

  for (ll cur = msk;; cur = (cur - 1) & msk) {
    if (check(num | cur)) {
      ll res = num | cur;
      string sres = "";
      for (; res; res >>= 1)
        sres = string(1, '0' + (res & 1)) + sres;
      printf("%s\n", sres.c_str());
      return;
    }
    if (!cur) break;
  }
  assert(false);
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
