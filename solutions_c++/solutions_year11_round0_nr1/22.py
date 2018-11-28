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
  int n;
  scanf("%d", &n);

  vector<pii> op;
  for (int i = 0; i < n; i++) {
    int x; char ty;
    scanf(" %c%d", &ty, &x);
    op.pb(mp(x, ty == 'B'));
  }
  vi p(2, 1);
  vi lti(2, 0);
  int ctim = 0;
  for (int i = 0; i < op.size(); i++) {
    int pos = op[i].first;
    int ty = op[i].second;
    int ntim = max(lti[ty] + abs(p[ty] - pos), ctim) + 1;
    ctim = ntim;
    p[ty] = pos;
    lti[ty] = ntim;
  }
  printf("%d\n", ctim);
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
    solve();
  }
  return 0;
}
