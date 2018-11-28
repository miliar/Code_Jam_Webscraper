#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <cstdlib>

using namespace std;

#define pb push_back
#define all(x) x.begin(), x.end()
#define mp make_pair

const int inf = (1 << 29) - 1;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int64;
typedef set < int > si;

int n, vl;
int g[20000], c[20000], st[20000], t[20000][2];

int go (int v, int cs)
{
  if (v > (n - 1) / 2)
    {
      if (st[v] == cs)
        return 0;
       else
        return inf;
    }
  if (t[v][cs] != -1)
    return t[v][cs];
  int res = inf;
  for (int i = 0; i < 2; i ++)
    for (int j = 0; j < 2; j ++)
      {
        if ((g[v] == 1) && ((i & j) == cs))
          res = min (res, go (v*2, i) + go (v*2+1, j));
        if ((g[v] == 0) && ((i | j) == cs))
          res = min (res, go (v*2, i) + go (v*2+1, j));

        if ((c[v] == 1) && (g[v] == 0) && ((i & j) == cs))
          res = min (res, go (v*2, i) + go (v*2+1, j) + 1);
        if ((c[v] == 1) && (g[v] == 1) && ((i | j) == cs))
          res = min (res, go (v*2, i) + go (v*2+1, j) + 1);
      }
  if (res > inf)
    res = inf;
  return t[v][cs] = res;
}

int main ()
{
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  int nn, ii;
  scanf ("%d", &nn);
  for (ii = 1; ii <= nn; ii ++)
    {
      scanf ("%d%d", &n, &vl);
      cerr << n << " " << vl << endl;
      for (int i = 1; i <= (n-1)/2; i ++)
        scanf ("%d%d", &g[i], &c[i]);
      for (int i = ((n-1)/2)+1; i <= n; i ++)
        scanf ("%d", &st[i]);
      memset (t, 255, sizeof (t));
      int ans = go (1, vl);
      cerr << go (1, vl) << " " << go (1, 1-vl) << endl;
      printf ("Case #%d: ", ii);
      if (ans == inf)
        printf ("IMPOSSIBLE\n");
       else
        printf ("%d\n", ans);
    }
}
