//Authored by dolphinigle
//Google Code Jam Qual 1
//May 21

#include <vector>
#include <list>
#include <map>
#include <set>

#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>

#define FORN(X,Y) for (int (X) = 0;(X) < (Y);++(X))
#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

#define REP(X,Y,Z) for (int (X) = (Y);(X) < (Z);++(X))
#define RESET(Z,Y) memset(Z,Y,sizeof(Z))

#define SZ(Z) ((int)Z.size())
#define ALL(W) W.begin(), W.end()
#define PB push_back

#define MP make_pair
#define A first
#define B second

#define INF 1023123123
#define EPS 1e-8

#define MX(Z,Y) Z = max((Z),(Y))
#define MN(X,Y) X = min((X),(Y))

#define FORIT(X,Y) for(typeof((Y).begin()) X = (Y).begin();X!=(Y).end();X++)

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vint;
typedef vector<ll> vll;

int main() {

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    printf("Case #%d: ", itc + 1);
    int n; double dist;
    cin >> n >> dist;

    vector< db > hotdogs;
    FORN(i, n) {
      db pos; int ven;
      cin >> pos >> ven;
      while (ven) {
        hotdogs.PB(pos);
        --ven;
      }
    }

    sort(ALL(hotdogs));

    double kHuge = 1000000000.0 * 1000000000.0 * 1000000000.0;

    n = SZ(hotdogs);

    double best = kHuge;
    double lbound = 0.0;
    double ubound = kHuge;

    while (abs(ubound - lbound) > 1e-10) {
      double mid = (ubound + lbound) / 2.0;

      int ok = 1;
      double lastpos = -kHuge;

      FORN(i, n) {
        if (hotdogs[i] + mid < lastpos + dist) {
          ok = 0;
          break;
        }
        lastpos = max(lastpos + dist, hotdogs[i] - mid);
      }

      if (ok) {
        best = mid;
        ubound = mid;
      } else {
        lbound = mid;
      }
    }

    printf("%.10lf\n", best);

  }

  return 0;
}

