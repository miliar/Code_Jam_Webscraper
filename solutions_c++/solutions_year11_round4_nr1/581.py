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
typedef pair<ll, ll> pll;

inline bool myLess( pll const& a, pll const& b )
{
  return a.second < b.second;
}

int main()
{
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int T;
  cin >> T;
  REP(testIt, T)
  {
    ll x, s, r;
    dbl t;
    int n;
    cin >> x >> s >> r >> t >> n;
    assert(r >= s);

    vector<pll> seg(n);
    REP(i, n)
    {
      int b, e, w;
      cin >> b >> e >> w;
      assert(e - b > 0 && w > 0);
      seg[i] = pll(e - b, w);
      x -= (e - b);
    }

    assert(x >= 0);
    seg.pb(pll(x, 0));

    sort(ALL(seg), myLess);
    dbl ans = 0;
    REPC(si, seg)
    {
      dbl runSpeed = (r + si->second);
      dbl runTime = min(t, dbl(si->first) / runSpeed);
      t -= runTime;
      ans += runTime + (si->first - runSpeed * runTime) / (s + si->second);
    }

    cout.precision(20);
    cout << "Case #" << testIt + 1 << ": " << fixed << ans << endl;
  }

  return 0;
}
