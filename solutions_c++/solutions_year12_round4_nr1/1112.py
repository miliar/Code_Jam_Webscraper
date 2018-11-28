#include <vector>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>

using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define mem(a, val) memset((a), val, sizeof(a))
#define inf    1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi acos(-1.0)
#define sqr(a) ((a)*(a))
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef vector< pair<int, int> > vpii;
typedef long long LL;
typedef pair<int, int> pii;

int d[100100];
int dd[100100];
int ll[100100];

int main() {
/*  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);/**/

  int T, x, y;
  scanf("%d", &T);
  rep(tt, T) {
    int n, D;
    scanf("%d", &n);
    rep(i, n) {
      scanf("%d%d", &x, &y);
      dd[i] = x;
      ll[i] = y;
    }
    scanf("%d", &D);
    mem(d, 0);

    bool res = false;
    priority_queue<pii> q;

    d[0] = dd[0];
    q.push(mp(d[0], 0));
    int v, dv, from, to;
    while(!q.empty() && !res) {
      dv = q.top().X;
      v = q.top().Y;
      q.pop();
      if (d[v] != dv) continue;

      from = upper_bound(dd, dd + n, dd[v] - dv - 1) - dd;
      to = upper_bound(dd, dd + n, dd[v] + dv) - dd;
      for(int i = from; i < to; ++i)
        if (d[i] < min(ll[i], abs(dd[i] - dd[v]))) {
          d[i] = min(ll[i], abs(dd[i] - dd[v]));
          if (dd[i] + d[i] >= D) res = true;
          q.push(mp(d[i], i));
        }
    }
//    rep(v, n) printf(":: %d: %d\n", v, d[v]);
    rep(i, n) if (dd[i] + d[i] >= D) res = true;

    printf("Case #%d: %s\n", tt + 1, res ? "YES" : "NO");
  }

  return 0;
}
