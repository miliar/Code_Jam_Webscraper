/* headers {{{1 */
#include <cassert>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <complex>
#include <iostream>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

/* defines {{{1 */
#define debug(x) cerr << __LINE__ << ": " << #x << " = " << (x) << "\n"
#define debugf(x...) fprintf(stderr, x)
#define mp make_pair
#define pb push_back
#define A first
#define B second
#define X real()
#define Y imag()
#define foreach(i, v) for (typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

typedef long long ll;
const int inf = 1 << 29; const ll llinf = (ll)inf * (ll)inf;

/* funcs {{{1 */
template<class T> inline int sz(const T& v) { return (int)v.size(); }

template<class T> inline T gcd(T a, T b) { return (b == 0) ? a : gcd(b, a % b); }
template<class T> inline T cross(complex<T> a, complex<T> b) { return a.X * b.Y - b.X * a.Y; }
template<class T> inline int cross_sign(complex<T> a, complex<T> b) { 
  double t = (double)a.X * b.Y - (double)b.X * a.Y; 
  return (abs(t) < 1e-9) ? 0 : (t > 0); 
}
template<class T1, class T2> struct conv_impl { inline static T1 conv(T2 x) { stringstream ss; ss << x; T1 y; ss >> y; return y; } };
template<class T2> struct conv_impl<string, T2> { inline static string conv(T2 x) { stringstream ss; ss << x; return ss.str(); } };
template<class T1, class T2> inline T1 conv(T2 x) { return conv_impl<T1, T2>::conv(x); }
template<class T> inline vector<T> split(string x, string y=" \n\t") { 
  vector<T> r; 
  for (int i = 0; i <= sz(x); ) { 
    int j = x.find_first_of(y, i); 
    if (j < 0) j = sz(x); 
    r.pb(conv<T>(x.substr(i, j - i))); 
    i = j + 1;
  }
  return r; 
}
template<class T> inline vector<T> tokenize(string x, string y=" \n\t") { 
  vector<T> r; 
  for (int i = x.find_first_not_of(y); 0 <= i && i <= sz(x); ) { 
    int j = x.find_first_of(y, i); 
    if (j < 0) j = sz(x); 
    r.pb(conv<T>(x.substr(i, j - i))); 
    i = x.find_first_not_of(y, j);
  }
  return r; 
}
/* end }}}1 */

const int MAXP = 11, MAX2P = 1<<10;
int p, miss[MAX2P], cost[MAXP][MAX2P];

int dp[MAXP][MAX2P][MAX2P][MAXP];

inline void imp(int& what, const int with) {
  if (what > with)
    what = with;
}

void solve_case() {
  scanf("%d", &p);
  for (int i = 0; i < 1<<p; i++)
    scanf("%d", &miss[i]);

  for (int i = 1; i <= p; i++)
    for (int j = 0; j < 1<<(p-i); j++)
      scanf("%d", &cost[i][j]);

  memset(dp, 31, sizeof(dp));

  for (int i = 0; i < 1<<p; i++)
    for (int j = miss[i]; j >= 0; j--)
      dp[0][i][0][j] = 0;

  for (int level = 1; level <= p; level++) {
    for (int match = 0; match < 1<<(p-level); match++) {
      int left_win_play = 0;
      for (int loser = 0; loser < 1<<(level - 1); loser++)
        left_win_play = max(left_win_play,  
              dp[level - 1][match * 2 + 1][loser][0]);

      int left_win_skip = 0;
      for (int loser = 0; loser < 1<<(level - 1); loser++)
        left_win_skip = max(left_win_skip, dp[level - 1][match * 2 + 1][loser][1]);

      int right_win_play = 0;
      for (int loser = 0; loser < 1<<(level - 1); loser++)
        right_win_play = max(right_win_play,
              dp[level - 1][match * 2][loser][0]);

      int right_win_skip = 0;
      for (int loser = 0; loser < 1<<(level - 1); loser++)
        right_win_skip = max(right_win_skip, dp[level - 1][match * 2][loser][1]);

      for (int winner = 0; winner < 1<<(level - 1); winner++) {
        for (int remaining = 0; remaining <= p; remaining++)
          imp(dp[level][match][winner][remaining],
            dp[level - 1][match * 2][winner][remaining]
              + left_win_play + cost[level][match]);
      }

      for (int winner = 0; winner < 1<<(level - 1); winner++) {
        for (int remaining = 1; remaining <= p; remaining++)
          imp(dp[level][match][winner][remaining - 1],
            dp[level - 1][match * 2][winner][remaining]
              + left_win_skip);
      }

      const int flag = 1<<(level - 1);

      for (int winner = 0; winner < 1<<(level - 1); winner++) {
        for (int remaining = 0; remaining <= p; remaining++)
          imp(dp[level][match][flag | winner][remaining],
            dp[level - 1][match * 2 + 1][winner][remaining]
              + right_win_play + cost[level][match]);
      }

      for (int winner = 0; winner < 1<<(level - 1); winner++) {
        for (int remaining = 1; remaining <= p; remaining++)
          imp (dp[level][match][flag | winner][remaining - 1],
            dp[level - 1][match * 2 + 1][winner][remaining]
              + right_win_skip);
      }
    }
  }

  /*
  for (int level = 0; level <= p; level++)
    for (int match = 0; match < 1<<(p-level); match++)
      for (int winner = 0; winner < 1<<level; winner++)
        for (int remaining = 0; remaining <= p; remaining++)
          printf("%d %d %d %d: %d\n", level, match, match * (1<<level) + winner, remaining, dp[level][match][winner][remaining]);
  */

  int ans = 0;
  for (int i = 0; i < 1<<p; i++)
    ans = max(ans, dp[p][0][i][0]);

  printf("%d\n", ans);
}

void base_init() {
}

const bool newline_after_case = false;

/* main {{{1 */
int main() {
  base_init(); 
  int t; 
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    printf("Case #%d:%s", i, newline_after_case ? "\n" : " "); 
    solve_case();
  }
  return 0;
}
/* end }}}1 */


