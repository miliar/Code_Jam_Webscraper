#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cmath>

#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

#define sz(c) ((int)(c).size())
#define pb push_back
#define mp make_pair

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPC(i, c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, s, n) for (int i = (s); i < (n); ++i)
#define ALL(c) (c).begin(), (c).end()

using namespace std;
typedef long long ll;
typedef long double dbl;
typedef pair<int, int> pii;

void solve()
{
  int n;
  cin >> n;
  vector<string> in(n);
  REP(i, n)
    cin >> in[i];
  vector<int> wins(n, 0), games(n, 0);
  REP(y, n)
    REP(x, n)
      if (in[y][x] != '.')
      {
        wins[y] += (in[y][x] == '1');
        games[y]++;
      }

  vector<dbl> owp(n, 0);
  REP(y, n)
  {
    REP(x, n)
      if (in[y][x] != '.')
        owp[y] += dbl(wins[x] - (in[y][x] == '0')) / (games[x] - 1);
    owp[y] /= games[y];
  }

  vector<dbl> oowp(n, 0);
  REP(y, n)
  {
    REP(x, n)
      if (in[y][x] != '.')
        oowp[y] += owp[x];
    oowp[y] /= games[y];
  }

  cout.precision(20);
  REP(y, n)
  {
//    cerr << dbl(wins[y]) / games[y] << endl;
    cout << fixed << (0.25 * dbl(wins[y]) / games[y] + 0.5 * owp[y] + 0.25 * oowp[y]) << endl;
  }
}

int main()
{
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int T;
  cin >> T;
  REP(ti, T)
  {
    cout << "Case #" << (ti + 1) << ":\n";
    solve();
  }

  return 0;
}
