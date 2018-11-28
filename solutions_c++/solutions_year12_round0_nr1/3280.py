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

char func(char c) {
  switch (c) {
  case 'a':
    return 'y';
  case 'b':
    return 'h';
  case 'c':
    return 'e';
  case 'd':
    return 's';
  case 'e':
    return 'o';
  case 'f':
    return 'c';
  case 'g':
    return 'v';
  case 'h':
    return 'x';
  case 'i':
    return 'd';
  case 'j':
    return 'u';
  case 'k':
    return 'i';
  case 'l':
    return 'g';
  case 'm':
    return 'l';
  case 'n':
    return 'b';
  case 'o':
    return 'k';
  case 'p':
    return 'r';
  case 'q':
    return 'z';
  case 'r':
    return 't';
  case 's':
    return 'n';
  case 't':
    return 'w';
  case 'u':
    return 'j';
  case 'v':
    return 'p';
  case 'w':
    return 'f';
  case 'x':
    return 'm';
  case 'y':
    return 'a';
  case 'z':
    return 'q';
  default:
    return c;
  }
}

void solve() {
  int n;
  //  ifstream ifs(in);
  string str;
  //  int i = 1;
  //  getline(ifs, str);
  //  n = str[0] - '0';
  getline(cin, str);
  n = boost::lexical_cast<int>(str);
  
  //  while (ifs && getline(ifs, str)) {
  REP(i, n) {
    getline(cin, str);
    cout << "Case #" << (i+1) << ": "; 
    REP(j, str.size()) {
      cout << func(str[j]);
    }
    cout << endl;
  }
}

int main(int argc, char *argv[]) {
  solve();

  return 0;
}
