#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

void Solve( int w, int h, int a )
{
  if (w * h < a)
  {
    printf("IMPOSSIBLE");
    return;
  }
  
  for (int x1 = -w; x1 <= w; x1++)
    for (int x2 = x1; x2 <= w; x2++)
    {
      int xmi = min(x1, 0), xma = max(x2, 0);
      if (xma - xmi > w)
        continue;
      for (int y1 = 0; y1 <= h; y1++)
        for (int y2 = 0; y2 <= h; y2++)
          if (abs(x2 * y1 - x1 * y2) == a)
          {
            int cx = x1 < 0 ? x1 : 0;
            printf("%d %d %d %d %d %d", x1 - cx, y1, x2 - cx, y2, 0 - cx, 0);
            return;
          }
//          else if (abs(abs(x2 * y1 - x1 * y2) - a) <= 10)
//            printf("(%d) ", a);
    }
  printf("IMPOSSIBLE");
}

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  
  int tn;
  scanf("%d", &tn);
  forn(tt, tn)
  {
    int w, h, a;
    scanf("%d%d%d", &w, &h, &a);
    
    printf("Case #%d: ", tt + 1);
    Solve(w, h, a);
    puts("");
  }
  
  return 0;
}
