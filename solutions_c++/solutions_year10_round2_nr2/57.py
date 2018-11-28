#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>

#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

const int maxn = 103;

int x[maxn], v[maxn], good[maxn];

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {  
    int n, k, b, t;
    scanf("%d%d%d%d", &n, &k, &b, &t);
    forn(i, n)
      scanf("%d", &x[i]);
    forn(i, n)
      scanf("%d", &v[i]);
    forn(i, n)
      good[i] = (x[i] + v[i] * t >= b);
//    forn(i, n)
//      printf("%d : %d\n", i, good[i]);

    int cnt = 0, res = 0;
    for (int i = n - 1; i >= 0; i--)
    {
      if (good[i] && k)
        res += cnt, k--;
      else
        cnt++;
    }
    printf("Case #%d: ", tt);
    if (k)
      puts("IMPOSSIBLE");
    else 
      printf("%d\n", res);
  }
  return 0;
}
