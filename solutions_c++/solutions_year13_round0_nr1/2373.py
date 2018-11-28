#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <complex>
#include <numeric>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR (i, 0, n)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define FORE(e, v) for (int e = head[v]; e >= 0; e = E[e].next)
#define UN(a) sort(all(a)), (a).erase(unique(all(a)), (a).end())
#define CL(a, v) memset(a, v, sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int INF = 1000000000;
const ll INF_LL = 1000000000000000000LL;
const double pi = 2 * acos(0.0);

template<class T> void smin(T& a, T b) { if (a > b) a = b; }
template<class T> void smax(T& a, T b) { if (a < b) a = b; }
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template<class T> T sqr(T a) { return a * a; }

template<class T> void outp(const vector<T>& v) {
  REP(i, sz(v)) cout << v[i] << (i + 1 == sz(v) ? '\n' : ' ');
}
template<class T> void outp(T* v, int n) {
  REP(i, n) cout << *v++ << (i + 1 == n ? '\n' : ' ');
}

char a[9][9];

bool check(char c0, char c1, char c2, char c3, char d) {
  if (c0 != d && c0 != 'T') return false;
  if (c1 != d && c1 != 'T') return false;
  if (c2 != d && c2 != 'T') return false;
  if (c3 != d && c3 != 'T') return false;
  return true;
}

int main() {
  freopen("a-large.in", "r", stdin);  // -small-attempt0
  freopen("a-large.out", "w", stdout);  // -large
  int test, T;
  for (test = 1, scanf("%d", &T); test <= T; ++test) {
    REP(i, 4) scanf("%s", a+i);
    bool x = false, o = false;
    bool full = true;
    REP(i, 4) REP(j, 4) if (a[i][j] == '.') full = false;
    REP(i, 4) {
      x |= check(a[i][0], a[i][1], a[i][2], a[i][3], 'X');
      o |= check(a[i][0], a[i][1], a[i][2], a[i][3], 'O');
    }
    REP(j, 4) {
      x |= check(a[0][j], a[1][j], a[2][j], a[3][j], 'X');
      o |= check(a[0][j], a[1][j], a[2][j], a[3][j], 'O');
    }
    x |= check(a[0][0], a[1][1], a[2][2], a[3][3], 'X');
    o |= check(a[0][0], a[1][1], a[2][2], a[3][3], 'O');
    x |= check(a[0][3], a[1][2], a[2][1], a[3][0], 'X');
    o |= check(a[0][3], a[1][2], a[2][1], a[3][0], 'O');
    printf("Case #%d: ", test);
    if (x) {
      printf("X won\n");
    } else if (o) {
      printf("O won\n");
    } else if (full) {
      printf("Draw\n");
    } else {
      printf("Game has not completed\n");
    }
  }
  return 0;
}
