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
struct Level {
  double len, p;
  int id;
  bool operator<(const Level &l2) const {
    double t1 = (1 - p) * len + p * (1 - l2.p) * (len + l2.len);
    double t2 = (1 - l2.p) * l2.len + l2.p * (1 - p) * (l2.len + len);

    if (fabs(t1 - t2) < EPS) return id < l2.id;
    return t1 < t2;

/*    bool v1 = t1 < t2;
    bool v2 = len + p * l2.len < l2.len + l2.p * len;
    assert(v1 == v2);
    return t1 < t2;*/
  }
};

void solve() {
  int n;
  scanf("%d", &n);
  vector<Level> ls(n);
  for (int i = 0; i < n; i++)
    scanf("%lf", &ls[i].len), ls[i].id = i;
  for (int i = 0; i < n; i++)
   scanf("%lf", &ls[i].p), ls[i].p = 1 - ls[i].p / 100.0;

  sort(ls.begin(), ls.end());
  for (int i = 0; i < sz(ls); i++)
    printf("%d%c", ls[i].id, "\n "[i + 1 < sz(ls)]);
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
