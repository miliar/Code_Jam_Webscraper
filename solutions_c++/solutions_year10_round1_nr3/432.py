#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iomanip>
#include <memory>
#include <cstring>
#include <climits>
#include <cassert>
#include <list>
using namespace std;

#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define DBGN(x) cout << #x << " = " << x << endl;
#define DBG(x) cout << #x << " = " << x << ", ";
#define DBGARR(x, n) REP(i, n) cout << #x << '[' << i << "] = " << x[i] << endl;
#define DBGTBL(x, a, b) REP(i, a) REP(j, b) cout << #x << '[' << i << "][" << j << "] = " << x[i][j] << endl;

#define FIN "test.in"
#define FOUT "test.out"

int gcd(int a, int b) {
  while (b) {
    a %= b;
    swap(a, b);
  }
  return a;
}

bool one_game(int a, int b) {
  if (a < b) {
    swap(a, b);
  }
  // gcd(a, b) == 1, a > b
  if (b == 1) {
    return true;
    // (1, 1) next move
  }
  if (a / b >= 2) {
    return true; // we have choice
  }
  return !one_game(b, a - b);
}

bool is_win(int a, int b) {
  if (a < b) {
    swap(a, b);
  }
  if (a == b)
    return false;
  if (a % b == 0) {
    return true;
  }
  int n = gcd(a, b);
  bool res = one_game(a / n, b / n);
  return res;
}

#define M 1000
int dp[M][M];

bool is_win_dp(int a, int b) {
  if (!dp[a][b]) {
    bool found_lost = false;
    int aa = a;
    while (true) {
      aa -= b;
      if (aa < 0) break;
      if (!is_win_dp(aa, b)) {
        found_lost = true;
      }
    }
    int bb = b;
    while (true) {
      bb -= a;
      if (bb < 0) {
        break;
      }
      if (!is_win_dp(a, bb)) {
        found_lost = true;
      }
    }
    if (found_lost) {
      dp[a][b] = 2; // win
    } else {
      dp[a][b] = 1; // lost
    }
  }
  return (dp[a][b] == 2);
}

long long doit(int A1, int A2, int B1, int B2) {
  memset(dp, 0, sizeof(dp));
    REP(i, M) {
      dp[i][0] = dp[0][i] = 2;
    }

  long long res = 0;
  FOR(a, A1, A2) FOR(b, B1, B2) {
    /*
    if (is_win(a, b) != is_win_dp(a, b)) {
      cout << a << ' ' << b << ' ' << is_win(a, b) << ' ' << is_win_dp(a, b) << endl;
    }
    */
    if (is_win(a, b)) {
      ++res;
    }
  }
  return res;
}

int main()
{
  freopen(FIN, "r", stdin);
  freopen(FOUT, "w", stdout);

  int tests;
  cin >> tests;
  REP(z, tests) {
    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;
    cout << "Case #" << z + 1 << ": ";
    cout << doit(a1, a2, b1, b2);
    cout << endl;
  }

  fclose(stdin);
  fflush(stdout);
  fclose(stdout);
  return 0;
}
