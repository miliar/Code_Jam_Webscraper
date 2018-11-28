//Authored by dolphinigle
//GCJ Q3 2011
//Jun 4 2011

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

int IsPrime(ll number) {
  if (number <= 1LL) return 0;
	for (ll i = 2LL;i * i <= number;i = (i == 2LL ? 3LL : i + 2LL)) {
		if (number % i == 0LL) return 0;
		}
	return 1;
	}
//IsPrime(1) == 0

ll GreatestCommonDivisor(ll abc,ll def) {
  if (abc < 0LL || def < 0LL) return GreatestCommonDivisor(abs(abc), abs(def));
	if (abc < def) return GreatestCommonDivisor(def,abc);
	if (!def) return abc;
	return GreatestCommonDivisor(def,abc % def);
}

ll numbers[1050];

int main() {

  int ntc;
  cin >> ntc;
  FORN(itc, ntc) {
    printf("Case #%d: ", itc+1);

    ll n;
    cin >> n;

    if (n == 1LL) {
      cout << 0 << endl;
      continue;
    }

    ll minnum = 0LL;

    ll maxnum = 0LL;
    for (int i = 1; i <= n; ++i) {
      if (i == 1) {
        ++maxnum;
        continue;
      }
      if (IsPrime(i)) {
        ++minnum;
        ++maxnum;
        int num = i;
        while (num*i <= n) {
          ++maxnum;
          num *= i;
        }
      }
    }

    cout << maxnum - minnum << endl;
  }

  return 0;
}
