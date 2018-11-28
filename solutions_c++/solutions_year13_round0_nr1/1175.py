#include <algorithm>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define REP(i, n) for(int i=0; i<(int)n; ++i)
#define FOR(i, c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(),(c).end()
#define each(i, c) FOR(i, c)

#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

const int N = 4;
char g[N][N];

const int X = (1 << 1);
const int O = (1 << 2);

int f(vector<char> v)
{
  int T = count(v.begin(), v.end(), 'T');
  unless (T <= 1) return 0;
  if (count(v.begin(), v.end(), 'X') + T == 4) return X;
  if (count(v.begin(), v.end(), 'O') + T == 4) return O;
  return 0;
}

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  while (t--) {
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        cin >> g[i][j];
      }
    }

    int n = 0;
    {
      vector<char> v;
      v.push_back(g[0][0]);
      v.push_back(g[1][1]);
      v.push_back(g[2][2]);
      v.push_back(g[3][3]);
      n |= f(v);
    }
    {
      vector<char> v;
      v.push_back(g[0][N-1]);
      v.push_back(g[1][N-2]);
      v.push_back(g[2][N-3]);
      v.push_back(g[3][N-4]);
      n |= f(v);
    }
    for (int i = 0; i < N; ++i) {
      vector<char> v;
      for (int j = 0; j < N; ++j) {
        v.push_back(g[i][j]);
      }
      n |= f(v);
    }
    for (int j = 0; j < N; ++j) {
      vector<char> v;
      for (int i = 0; i < N; ++i) {
        v.push_back(g[i][j]);
      }
      n |= f(v);
    }
    static int tc = 0;
    cout << "Case #" << ++tc << ": " << flush;
    if (0) ;
    else if (n == X) cout << "X won" << endl;
    else if (n == O) cout << "O won" << endl;
    else if (n == 0) {
      if (count(&g[0][0], &g[N - 1][N - 1] + 1, '.')) cout << "Game has not completed" << endl;
      else cout << "Draw" << endl;
    }
  }
  return 0;
}
