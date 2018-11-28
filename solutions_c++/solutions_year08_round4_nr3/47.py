#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
using namespace std;
 
#define all(c) ((c).begin()), ((c).end()) 
#define iter(c) __typeof((c).begin())
#define present(c, e) ((c).find((e)) != (c).end()) 
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)
 
const double EPS = 1E-9;
const double INF = 1E20;
const double ROOT2 = sqrt(2.0);

typedef long long ll;
 

int N;
int X[1010], Y[1010], Z[1010], P[1010];

void kaiten(double &x, double &y) {
  static double si = sin(M_PI / 4.0), co = cos(M_PI / 4.0);

  double tx = x, ty = y;
  x = si * tx - co * ty;
  y = co * tx + si * ty;
}

bool ok(int z, double v) {
  double minx = -INF, maxx = INF;
  double miny = -INF, maxy = INF;

  for (int i = 0; i < N; i++) {
    double lim = v * P[i] - abs(Z[i] - z);
    if (lim < -EPS) return false;
    
    // なんと座標を45度回転
    double x = X[i];
    double y = Y[i];
    kaiten(x, y);
    
    double r = lim / ROOT2;
    minx >?= x - r; maxx <?= x + r;
    miny >?= y - r; maxy <?= y + r;
  }

  if (minx - EPS < maxx && miny - EPS < maxy) return true;
  else return false;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    scanf("%d", &N);

    vector<int> evz;

    rep (i, N) {
      cin >> X[i] >> Y[i] >> Z[i] >> P[i];
      evz.pb(Z[i]);
    }

    sort(all(evz));
    evz.erase(unique(all(evz)), evz.end());

    double lb = 0.0, ub = 1E20;
    while (ub - lb > EPS) {
      double mid = (ub + lb) / 2.0;

      for (int i = 0; i < evz.size(); i++) {
        if (ok(evz[i], mid)) {
          ub = mid;
          goto done;
        }
      }

      lb = mid;
      continue;

    done:
      ;
    }
    
    printf("Case #%d: %.10f\n", t, lb);
  }
}
