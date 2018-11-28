#include <cstdio>
#include <iostream>
#include <string>
#include <memory.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <set>
#include <sstream>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

string a[126];
int n, k;

bool calc(char c)
{
  forn (i, n) forn (j, n) for (int dx=-1; dx<=1; ++dx) for (int dy=-1; dy<=1; ++dy) if (dx!=0 || dy!=0)
  {
    int x = i, y = j, t = 0;
    for (; t<k; ++t)
    {
      if (x < 0 || x>=n || y < 0 || y>=n) break;
      if (a[x][y]!=c) break;
      x += dx, y += dy;
    }
    if (t >= k) return true;

  }
  return false;
}

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);

  int tc;
  scanf("%d", &tc);

  for (int tt=1; tt<=tc; ++tt)
  {
    printf("Case #%d:", tt);
    cin >> n >> k;
    forn (i, n) cin >> a[i];

    forn (i, n)
    {
      string s = "";
      for (int j=n-1; j>=0; --j)
        if (a[i][j]!='.') s = a[i][j]+s;
      while (sz(s) < n) s = "."+s;
      a[i] = s;
    }

    int x = calc('R');
    int y = calc('B');

    if (x && y) puts(" Both");
    else if (x && !y) puts(" Red");
    else if (!x && y) puts(" Blue");
    else puts (" Neither");




  }

  return 0;
}
