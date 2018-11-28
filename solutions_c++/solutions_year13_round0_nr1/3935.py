#include <algorithm>
#include <bitset>
#include <cctype>
#include <cerrno>
#include <clocale>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cwchar>
#include <cwctype>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <ostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i,m,n) for(long long i = m; i < n; ++i)
#define re return
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define eps 1e-7
#define FOR(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef vector<vll> vvll;
typedef vector<vii> vvii;

const ll INF = 1000000000000;
const double PI = 4 * atan(1.0);
bool XX(char s0, char s1, char s2, char s3) {
  return (s0 == 'X' || s0 == 'T') && (s1 == 'X' || s1 == 'T')
      && (s2 == 'X' || s2 == 'T') && (s3 == 'X' || s3 == 'T');
}
bool OO(char s0, char s1, char s2, char s3) {
  return (s0 == 'O' || s0 == 'T') && (s1 == 'O' || s1 == 'T')
      && (s2 == 'O' || s2 == 'T') && (s3 == 'O' || s3 == 'T');
}
int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int num = 1; num < T + 1; ++num) {
    vs st(5);
    rep(i,0,4)
      cin >> st[i];
    int stat = 0;
    for (int i = 0; i < 4; ++i) {
      if (XX(st[i][0], st[i][1], st[i][2], st[i][3])
          || XX(st[0][i], st[1][i], st[2][i], st[3][i]))
        stat = 1;
      if (OO(st[i][0], st[i][1], st[i][2], st[i][3])
          || OO(st[0][i], st[1][i], st[2][i], st[3][i]))
        stat = 2;
    }
    if (XX(st[0][0], st[1][1], st[2][2], st[3][3])
        || XX(st[0][3], st[1][2], st[2][1], st[3][0]))
      stat = 1;
    if (OO(st[0][0], st[1][1], st[2][2], st[3][3])
        || OO(st[0][3], st[1][2], st[2][1], st[3][0]))
      stat = 2;
    if (stat == 1) {
      cout << "Case #" << num << ": X won" << endl;
    } else if (stat == 2) {
      cout << "Case #" << num << ": O won" << endl;
    } else {
      bool hehe = false;
      for (int i = 0; i < 4; ++i)
        if (st[i].find('.') != string::npos)
          hehe = true;
      if (hehe) {
        cout << "Case #" << num << ": Game has not completed" << endl;
      } else {
        cout << "Case #" << num << ": Draw" << endl;
      }
    }
  }
  return 0;
}
