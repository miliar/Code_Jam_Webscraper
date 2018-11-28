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

const int inf = (1 << 30) - 1;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef long long int64;
typedef set < int > si;

int n, m, t[11][1024];
bool a[11][11];

bool check (int j, int k)
{
  for (int i = 0; i < m; i ++)
    if (j & (1 << i))
      {
        if (i > 0)
          {
            if (k & (1 << (i-1)))
              return false;
          }
        if (i < m - 1)
          {
            if (k & (1 << (i+1)))
              return false;
          }
      }
  return true;
}

bool chk (int v)
{
  for (int i = 0; i < m-1; i ++)
    if ((v & (1 << i)) && (v & (1 << (i + 1))))
      return false;
  return true;
}

int calcs (int v)
{
  int res = 0;
  while (v)
    {
      res += v & 1;
      v >>= 1;
    }
  return res;
}

int main ()
{
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  int nn;
  scanf ("%d\n", &nn);
  for (int ii = 1; ii <= nn; ii ++)
    {
      char c;
      memset (a, 0, sizeof (a));
      scanf ("%d %d\n", &n, &m);
      for (int i = 1; i <= n; i ++)
        for (int j = 1; j <= m; j ++)
          {
            c = 0;
            while (!(c =='x' || c == '.'))
              scanf ("%c", &c);
            a[i][j] = c == '.';
          }
       for (int i = 0; i <= 10; i ++)
         for (int j = 0; j < 1024; j ++)
           t[i][j] = -inf;
       t[0][0] = 0;
       int ans = 0;
       for (int i = 1; i <= n; i ++)
         for (int j = 0; j < (1 << m); j ++)
          if (chk (j))
           {
             bool ch = true;
             for (int k = 0; k < m; k ++)
               if ((j & (1 << k)) && (!a[i][k+1]))
                 ch = false;
             if (!ch)
               continue;
             t[i][j] = 0;
             for (int k = 0; k < (1 << m); k ++)
               if (chk (k))
                 if (check (j, k))
                   t[i][j] = max (t[i][j], t[i-1][k] + calcs (j));
             ans = max (ans, t[i][j]);
           }
        printf ("Case #%d: %d\n", ii, ans);
    }
}
