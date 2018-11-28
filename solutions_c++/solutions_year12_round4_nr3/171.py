#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for(int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR(i, 0, n)
#define FORD(i, a, b) for(int i(a), _b(b); i >= _b; --i)
#define CL(a, v) memset(a, v, sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

template<class T1, class T2> void smin(T1& a, T2 b) { if (a > b) a = b; }
template<class T1, class T2> void smax(T1& a, T2 b) { if (a < b) a = b; }

const int INF = 1000000000;
const ll INF_LL = 1000000000000000000LL;

const int h = 2222;
int n, x[h], y[h];

bool solve(int ia, int ib, int d) {
  //cout << ia << ' ' << ib << ' ' << d << endl;
  FOR(i, ia, ib) if(x[i] > ib) return false;
  int y0 = y[ia] + (ia - ib);
  int u = ia + 1;
  bool ok = true;
  while (u != ib) {
    y[u] = y0 + d * (u - ia);
    if (x[u] - u > 1) ok = ok && solve(u, x[u], d+1);
    u = x[u];
  }
  return ok;
}

int main() {
  freopen("c-large.in", "r", stdin);  // -small-attempt0
  freopen("c-large.out", "w", stdout);  // -large
  int itest, ntest;
  for(itest = 1, scanf("%d", &ntest); itest <= ntest; ++itest) {
    scanf("%d", &n);
    REP(i, n-1) scanf("%d", x+i);
    REP(i, n-1) --x[i];
    bool ok = true;
    int u = 0;
    while(1) {
      y[u] = INF;
      if (u == n-1) break;
      if(x[u] - u > 1) ok = ok && solve(u, x[u], 1);
      u = x[u];
    }
    printf("Case #%d:", itest);
    if(!ok) printf(" Impossible");
    else {
      REP(i, n) printf(" %d", y[i]);
    }
    printf("\n");
  }
  return 0;
}
