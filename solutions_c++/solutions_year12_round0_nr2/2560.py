#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
              
int main (void)
{
  int test, tests;

  freopen ("B-large.in", "rt", stdin);
  freopen ("B-large.out", "wt", stdout);

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int res, ok, susp, ball, surp, l1, l2, i, n, sum;
    scanf ("%d %d %d", &n, &surp, &ball);
    res = 0;
    ok = 0; 
    susp = 0;
    l1 = ball * 3 - 2;
    l2 = ball * 3 - 4;
    for (i = 0; i < n; i++)
    {
      scanf ("%d", &sum);
      if (sum >= l1)
        ok++;
      else if (sum >= l2 && sum >= 2 && sum <=28)
        susp++;
    }
    res = ok + min(susp, surp);
    printf ("Case #%d: %d\n", test + 1, res);
    
  }
  return 0;
}
