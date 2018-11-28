#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main (void)
{
  int test, tests, i, k[111], n, reso, resb, oi, bi, ok, bk, bc, oc;
  char c[111];
  freopen ("a.in", "rt", stdin);
  freopen ("a.out", "wt", stdout);
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    scanf ("%d", &n);
    reso = resb = 0; 
    oi = bi = 1;
    ok = bk = 1;
    oc = bc = 0;
    for (i = 1; i <= n; i++)
    {
      scanf (" %c %d", &c[i], &k[i]);
      if (c[i] == 'O')
      {
        reso += max (bc, max (abs (k[i] - ok) + 1, 1));
        oi = i; ok = k[i];
        bc = 0;
        oc = reso - resb + 1;
      }
      else
      {
        resb += max (oc, max (abs (k[i] - bk) + 1, 1));
        bi = i; bk = k[i];
        oc = 0;
        bc = resb - reso + 1;
      }
    }
    printf ("Case #%d: %d\n", test + 1, max (reso, resb));
  }
  return 0;
}
