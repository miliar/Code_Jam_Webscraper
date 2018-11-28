#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <cstring>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)n; i++)
#define all(a) a.begin(), a.end()
#define fs first
#define sc second

typedef long long int64;


int w, ans = 0, n, k, t;
int a[200][200];
bool g[200][200];
bool u[200];
int mt[200];



bool ok(int x, int y)
{
  forn(i, k)
    if (a[x][i] > a[y][i])
      continue;
     else
      return false;

  return true;
}

bool go(int x)
{
  if (u[x])
    return false;

  u[x] = true;

  forn(i, n)
    if (g[x][i])
      {
        if (mt[i] == -1 || go(mt[i]))
          {
            mt[i] = x;
            return true;
          }
      }

  return false;
}

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  scanf("%d", &t);

  forn(w, t)
    {
      scanf("%d%d", &n, &k);

      forn(i, n)
        forn(j, k)
          scanf("%d", &a[i][j]);

      memset(g, 0, sizeof(g));
                                                                       
      forn(i, n)
        forn(j, n)
          if ( ok(i, j) )
            g[i][j] = true;

      memset(mt, 255, sizeof(mt));

      ans = n;

      forn(i, n)
        {
          memset(u, 0, sizeof(u));
          if (go(i))
            ans--;
        }
      
      printf("Case #%d: %d\n", w+1, ans);
    }
}
