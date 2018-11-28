//Authored by dolphinigle
//Google Code Jam Prelim
//May 7 2011

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

db dyn[1002][1002]; //a b jml dari a ambil b

int yesinitial = 1;
db combination(ll people,ll need) {
	if (yesinitial) {
		FORN(i,1002) FORN(j,1002) dyn[i][j] = -2.0;
		yesinitial = 0;
		}
	if (dyn[people][need] > -1.0) return dyn[people][need];
	if (need == 0) return 1.0;
	if (people == need) return 1.0;
	if (people < need) return 0.0;
	dyn[people][need] = combination(people-1,need) + combination(people-1,need-1);
	return dyn[people][need];
	}

double chance[1050][1050]; // a barang, b lokasinya cocok

double dp[1050];

int n;

double solve(int ok) {
  if (ok == n) return 0.0;
  if (dp[ok] > -1.0) return dp[ok];
  dp[ok] = 0.0;
  int shuffle = n - ok;
  double rebound = chance[shuffle][0];
  double otherwise = 0.0;
  REP(i, 1, shuffle+1) otherwise += chance[shuffle][i] * (solve(ok + i) + 1.0);
  return dp[ok] = (otherwise + rebound) / (1.0 - rebound);
}


db rfact[1050];

db derange[1050];

double derangementProbability(int no) {
  if (derange[no] > -1.0) return derange[no];
  db ret = 0.0;
  db sign = 1.0;
  for (int i = 0; i <= no; ++i) {
    ret += sign * rfact[i];
    sign *= -1.0;
  }
  return derange[no] = ret;
}

int main() {

  FORN(i, 1050) derange[i] = -2.0;

  rfact[0] = 1.0;
  for (int i = 1; i < 1050; ++i) {
    rfact[i] = rfact[i-1] / (db)i;
  }

  FORN(i, 1050) {
    chance[i][i] = rfact[i];
    for (int j = i-1; j >= 0; --j) {
      chance[i][j] = derangementProbability(i-j) * rfact[j];
    }
  }

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    cout << "Case #" << itc+1 << ": ";
    cin >> n;
    FORN(i, 1050) dp[i] = -2.0;
    int ok = 0;
    FORN(i, n) {
      int buf;
      cin >> buf;
      if (buf == i+1) ok++;
    }
    printf("%.6lf\n", solve(ok));

  }


  return 0;
}

