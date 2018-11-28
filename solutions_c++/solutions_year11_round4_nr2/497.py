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
typedef double dbl;
typedef pair<int, int> pii;

char buf[1002];

void updateSumPref( vector<vector<ll> >& pref )
{
  int h = sz(pref) - 1;
  int w = sz(pref[0]) - 1;

  REP(y, h)
    REP(x, w)
      pref[y + 1][x + 1] += pref[y][x + 1] + pref[y + 1][x] - pref[y][x];
}

inline ll getSum( vector<vector<ll> > const& pref, int sx, int sy, int w, int h )
{
  return pref[sy + h][sx + w]
             - pref[sy][sx + w] - pref[sy + h][sx] + pref[sy][sx];
}

int main()
{
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int T;
  scanf("%d", &T);
  REP(ti, T)
  {
    cerr << ti << endl;

    int h, w, d;
    scanf("%d%d%d", &h, &w, &d);

    vector<string> m(h);
    REP(y, h)
    {
      scanf("%s", buf);
      m[y] = buf;
    }
    vector<vector<int> > we(h, vector<int>(w));
    REP(y, h)
      REP(x, w)
        we[y][x] = m[y][x] - '0';

    vector<vector<ll> > pref(h + 1, vector<ll>(w + 1, 0));
    vector<vector<ll> > prefx(h + 1, vector<ll>(w + 1, 0));
    vector<vector<ll> > prefy(h + 1, vector<ll>(w + 1, 0));

    REP(y, h)
      REP(x, w)
        pref[y + 1][x + 1] = we[y][x];
    updateSumPref(pref);
    REP(y, h)
      REP(x, w)
        prefx[y + 1][x + 1] = we[y][x] * x;
    updateSumPref(prefx);
    REP(y, h)
      REP(x, w)
        prefy[y + 1][x + 1] = we[y][x] * y;
    updateSumPref(prefy);

    int ans = -1;
    int limK = min(w, h) + 1;
    FOR(K, 3, limK)
    {
//      sx + K <= w
      REP(sy, h - K + 1)
        REP(sx, w - K + 1)
        {
          ll sum  = getSum(pref, sx, sy, K, K);
          ll sumx2 = 2 * getSum(prefx, sx, sy, K, K) - (2 * sx + K - 1) * sum;
          ll sumy2 = 2 * getSum(prefy, sx, sy, K, K) - (2 * sy + K - 1) * sum;
          sumx2 += ll(we[sy][sx] + we[sy + K - 1][sx]) * (K - 1);
          sumx2 -= ll(we[sy][sx + K - 1] + we[sy + K - 1][sx + K - 1]) * (K - 1);

          sumy2 += ll(we[sy][sx] + we[sy][sx + K - 1]) * (K - 1);
          sumy2 -= ll(we[sy + K - 1][sx] + we[sy + K - 1][sx + K - 1]) * (K - 1);

          if (sumx2 == 0 && sumy2 == 0 && (ans == -1 || ans < K))
            ans = K;
        }
    }

    printf("Case #%d: ", ti + 1);
    if (ans == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", ans);
  }
  return 0;
}
