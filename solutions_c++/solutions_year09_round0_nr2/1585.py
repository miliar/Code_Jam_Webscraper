#include <iostream>
#include <algorithm>
#include <vector>
#include <complex>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <bitset>
#include <queue>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef complex<double> C;

const double pi = 3.141592653589793238462643383279;
const double napier = 2.718281828459045235360287471352;
const C eye = C(0, 1);

#define FOR(i,n) for (unsigned i = 0; i < (n); ++i)
#define REP(i,n) for (unsigned i = 1; i <= (n); ++i)
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).begin(), (v).end()

const int INF = 10000000;

int T, W, H;

int altitude[102][102];
int label[102][102];

typedef pair<int, int> NODE;
vector<NODE> g[101][101];

void solve()
{
  REP (w, W) REP (h, H) g[w][h] = vector<NODE>();

  REP (w, W) REP (h, H) {
    NODE p = make_pair(-1, -1);
    int lowest = altitude[w][h];
    for (int dh = -1; dh <= 1; ++dh) {
      for (int dw = -1; dw <= 1; ++dw) {
        if (dh * dh + dw * dw == 1) {
          int ww = w + dw;
          int hh = h + dh;
          int a = altitude[ww][hh];
          if (a < lowest) {
            p = make_pair(ww, hh);
            lowest = a;
          }
        }
      }
    }
    if (p.first != -1) {
      g[w][h].push_back(p);
      g[p.first][p.second].push_back(make_pair(w, h));
    }
  }

  REP (w, W) REP (h, H) label[w][h] = -1;

  int cnt = 0;
  REP (h, H) REP (w, W) {
    if (label[w][h] >= 0)
      continue;
    label[w][h] = cnt++;
    queue<NODE> q;
    q.push(make_pair(w, h));
    while (!q.empty()) {
      NODE x = q.front(); q.pop();
      FOR (i, g[x.first][x.second].size()) {
        NODE y = g[x.first][x.second][i];
        if (label[y.first][y.second] < 0){
          label[y.first][y.second] = label[w][h];
          q.push(y);
        }
      }
    }
  }
}

int main()
{
  cin >> T;
  FOR (i, T) {
    cout << "Case #" << i + 1 << ":" << endl;
    cin >> H >> W;

    FOR (w, W + 2) FOR (h, H + 2)
      altitude[w][h] = INF;

    REP (h, H) REP (w, W)
      cin >> altitude[w][h];

    solve();

    REP (h, H) {
      string sep;
      REP (w, W) {
        cout << sep << (char)('a' + label[w][h]);
        sep = " ";
      }
      cout << endl;
    }
  }

  return 0;
}
