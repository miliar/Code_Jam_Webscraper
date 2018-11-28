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

const dbl eps = 1e-9;

bool doInterval( dbl& left, dbl t, dbl x, dbl D, int cnt )
{
  if (left < x + eps)
  {
    dbl reachLeft = max(left, x - t);
    dbl reachRight = reachLeft + (cnt - 1) * D;
    if (reachRight > x + t + eps)
      return false;
    left = reachRight + D;
    return true;
  }  
  else
  {
    dbl reachRight = left + (cnt - 1) * D;
    if (reachRight > x + t + eps)
      return false;
    left = reachRight + D;
    return true;
  }
}

void solve()
{
  int n, D;
  scanf("%d%d", &n, &D);
  vector<pii> in(n);
  REP(i, n)
    scanf("%d%d", &in[i].first, &in[i].second);
  sort(ALL(in));

  vector<int> cnt(n), pos(n);
  REP(i, n)
    pos[i] = in[i].first, cnt[i] = in[i].second;

  dbl tleft = 0, tright = 1e+16, t = 0;
  REP(iter, 400)
  {
    t = (tleft + tright) * 0.5;
    dbl left = pos.front() - t;
    bool can = true;

    REP(i, n)
      if (!doInterval(left, t, pos[i], D, cnt[i]))
      {
        can = false;
        break;
      }
    if (can)
      tright = t;
    else
      tleft = t;
  }

  cout.precision(20);
  cout << fixed << t << "\n";
}

int main()
{
  freopen("input.txt", "rt", stdin);
  freopen("output.txt", "wt", stdout);

  int T;
  scanf("%d", &T);
  REP(ti, T)
  {
    cout << "Case #" << (ti + 1) << ": ";
    solve();
  }

  return 0;
}
