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
    printf("Case #%d:\n", itc + 1);

    int n;
    cin >> n;

    vector<string> sc;
    FORN(i, n) {
      string buf;
      cin >> buf;
      sc.PB(buf);
    }

    vint wins(n, 0);
    vint games(n, 0);

    FORN(i, n) {
      FORN(j, n) {
        if (sc[i][j] == '1') {
          ++wins[i];
        }
        if (sc[i][j] != '.') {
          ++games[i];
        }
      }
    }

    vector<double> wps(n, 0);
    FORN(i, n) wps[i] = (db)wins[i] / (db)games[i];

    vector<double> owps(n, 0);

    FORN(i, n) {
      double sum = 0.0;
      FORN(j, n) if (sc[i][j] != '.') {
        sum += (db)(wins[j] - (sc[i][j] == '0')) / (db)(games[j] - 1);
      }
      sum /= (db)games[i];
      owps[i] = sum;
    }

    vector<double> oowps(n, 0);
    FORN(i, n) {
      double sum = 0.0;
      FORN(j, n) if (sc[i][j] != '.') sum += owps[j];
      sum /= (db)games[i];
      oowps[i] = sum;
    }

    FORN(i, n) {
      printf("%.9lf\n", 0.25 * wps[i] + 0.5 * owps[i] + 0.25 * oowps[i]);
    }
  }

  return 0;
}

