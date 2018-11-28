#include <cstdio>
#include <iostream>
#include <queue>
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

const int inf = 1000000000;

int a[128];
int f[128][256];
int n, del, ins, dif;
priority_queue<pii,vector<pii>,greater<pii> > q;


inline void push(int pos, int last, int dd)
{
  if (f[pos][last] <= dd) return;
  f[pos][last] = dd;
  q.push(mp(dd, pos*1000+last));
}

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);

  int tc;
  scanf("%d", &tc);

  for (int tt=1; tt<=tc; ++tt)
  {
    printf("Case #%d:", tt);

    scanf("%d %d %d %d", &del, &ins, &dif, &n);
    forn (i, n) scanf("%d", a+i);

    forn (i, 128) forn (j, 256) f[i][j] = inf;

    int res = inf;


    forn (i, 256) push(0, i, ins);
    forn (i, 256) push(1, i, abs(i-a[0]));

    while (!q.empty())
    {
      int dd = q.top().first;
      int pos = q.top().second/1000;
      int last = q.top().second%1000;
      q.pop();

      if (pos >= n)
      {
        res = min(res, dd);
        continue;
      }

      if (dd > f[pos][last]) continue;

      push(pos+1, last, dd+del);

      forn (i, 256) if (abs(i-last) <= dif) push(pos, i, dd+ins);
      forn (i, 256) if (abs(i-last) <= dif) push(pos+1, i, dd+abs(i-a[pos]));

    }

    printf(" %d\n", res);




  }

  return 0;
}
