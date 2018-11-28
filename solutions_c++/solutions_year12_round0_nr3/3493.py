#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <limits>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cmath>
#include <boost/lexical_cast.hpp>

// using
using namespace std;
using boost::lexical_cast;

// typedef
typedef vector<int> VI;
typedef vector<VI> VII;
typedef vector<string> VS;
typedef vector<long> VL;
typedef long long LL;
typedef vector<LL> VLL;

// container utils
#define PB push_back
#define PF push_front
#define GRT(x) greater<(x)>()
#define ASORT(x) sort((x).begin(), (x).end())
#define DSORT(x, y) sort((x).begin(), (x).end(), greater<(y)>())
#define FILL(x, y) fill((x).begin(), (x).end(), (y))
#define COPY(x, y) (y).clear(); \
  copy((x).begin(), (x).end(), back_inserter(y))

// repetition
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORL(i, a, b) for (long i = (a); i < (b); i++)
#define FORLL(i, a, b) for (LL i = (a); i < (b); i++)
#define REP(i, n) FOR(i, 0, n)
#define REPL(i, n) FORL(i, 0, n)
#define REPLL(i, n) FORLL(i, 0, n)

// output
#define YES cout << "YES" << endl
#define NO cout << "NO" << endl
#define P(x) cout << (x) << endl

// static const
static const double EPS = 1e-10;
static const double PI = 6.0 * asin(0.5);

// debug
#define DUMP(a) cerr << #a << " = " << (a) << endl
#define DUMP2(a, b) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << endl
#define DUMP3(a, b, c) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << ", " << #c << " = " << (c) << endl

typedef pair<int, int> PII;

void solve() {
  int t;
  string str1, str2, tmp;
  int a, b;
  int n, m;
  int ans = 0;
  set<PII> sp;

  cin >> t;

  REP(i, t) {
    ans = 0;
    sp.clear();
    cin >> a >> b;
    FOR(j, a, b) {
      n = j;
      str1 = lexical_cast<string>(n);
      FOR(k, 1, str1.size()) {
	str2 = str1.substr(str1.size() - k, k) + str1.substr(0, str1.size() - k);
	if (str2[0] == '0') continue;
	m = lexical_cast<int>(str2);
	if (m > n && m <= b) {
	  if (sp.find(PII(n, m)) == sp.end()) {
	    sp.insert(PII(n, m));
	    ans++;
	  }
	}
      }
    }
    cout << "Case #" << (i+1) << ": " << ans << endl;
  }
}

int main(int argc, char *argv[]) {
  solve();

  return 0;
}
