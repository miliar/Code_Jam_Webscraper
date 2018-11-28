#include <cstdio>
#include <iostream>
#include <vector>
#include <memory.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 132;

char a[maxn][maxn];
int n, m, d;

inline int get(int x, int y, int sx, int sy, int k)
{
  if (x == sx && y == sy) return 0;
  if (x == sx && y == sy+k-1) return 0;
  if (x == sx+k-1 && y == sy) return 0;
  if (x == sx+k-1 && y == sy+k-1) return 0;
  return a[x][y]+d;
}

bool check(int k)
{
  //printf("k = %d\n", k);
  for (int i=0; i+k<=n; ++i)
    for (int j=0; j+k<=m; ++j)
    {
      int sumX = 0;
      if (k % 2 == 1)
      {
        for (int t=-k/2; t<=k/2; ++t)
        {
          for (int y=0; y<k; ++y)
            sumX += t*get(i+k/2+t, j+y, i, j, k);         
        }
      }
      else
      {
        for (int t=1; t<=k/2; ++t)
          for (int y=0; y<k; ++y)
            sumX += -t*get(i+k/2-t, j+y, i, j, k) + t*get(i+k/2+t-1, j+y, i, j, k);
      }
      int sumY = 0;
      if (k % 2 == 1)
      {
        for (int t=-k/2; t<=k/2; ++t)
        {
          for (int y=0; y<k; ++y)
            sumY += t*get(i+y, j+k/2+t, i, j, k);         
        }
      }
      else
      {
        for (int t=1; t<=k/2; ++t)
          for (int y=0; y<k; ++y)
            sumY += -t*get(i+y, j+k/2-t, i, j, k) + t*get(i+y, j+k/2+t-1, i, j, k);
      }
      if (sumX == 0 && sumY == 0) 
      {
      //  printf("%d %d\n", i, j);
        return true;
        
      }
    }
  return false;   
}

int main()
{
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  
  int tc; scanf("%d", &tc);
  for (int tt=1; tt<=tc; ++tt)
  {
    scanf("%d %d %d", &n, &m, &d);
    gets(a[0]);
    forn (i, n) gets(a[i]);
    forn (i, n) forn (j, m) a[i][j] -= '0';
    int k;
    for (k=min(n, m); k>=3; --k)
    {
      if (check(k)) break;
    }
    printf("Case #%d: ", tt);
    if (k < 3) puts("IMPOSSIBLE");
    else printf("%d\n", k);   
  }
  
  return 0;
}
