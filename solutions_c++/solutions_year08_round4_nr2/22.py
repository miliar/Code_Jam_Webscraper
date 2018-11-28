#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)

int main()
{
  int nn;
  scanf("%d", &nn);
  forn (test, nn)
  {
    int n, m, a;
    scanf("%d%d%d", &n, &m, &a);
    int k = (a + m - 1) / m;
    int t = m * k - a;
    int x1 = 1, y1 = m;
    int x2 = k, y2 = t;
    if (0 <= x1 && x1 <= n && 0 <= x2 && x2 <= n && 0 <= y1 && y1 <= m && 0 <= y2 && y2 <= m)
    {
      if (abs(x1 * y2 - y1 * x2) != a)
        fprintf(stderr, "botva!\n");
      printf("Case #%d: %d %d %d %d %d %d\n", test + 1, 0, 0, x1, y1, x2, y2);
    }
    else if (m * n >= a)
    {
      fprintf(stderr, "Case #%d: %d %d %d %d %d %d\n", test + 1, 0, 0, x1, y1, x2, y2);
      fprintf(stderr, "??? %d,%d,%d\n", m, n, a);
    }
    else
      printf("Case #%d: IMPOSSIBLE\n", test + 1);
  //  x1*y2-x2*y1
  //  k = (A + m - 1) / m
  //  k=n,t=o-> (m,0)(1,n)
  //  m*k-1*t = A
  //  t = A-m*k <= m
  }
  return 0;
}

