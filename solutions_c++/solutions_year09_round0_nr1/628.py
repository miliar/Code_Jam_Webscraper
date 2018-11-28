#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>

using namespace std;

const int MaxN = 5007, MaxK = 32, MaxL = 1024;

char w [MaxN] [MaxK];
char s [MaxL];
int d, l, n;

int main (void)
{
 int i, j, k, p, res;
 bool ok;
 while (scanf (" %d %d %d", &l, &d, &n) != EOF)
 {
  for (i = 0; i < d; i++)
   scanf (" %s", w[i]);
  for (j = 1; j <= n; j++)
  {
   scanf (" %s", s);
   res = 0;
   for (i = 0; i < d; res += ok, i++)
    for (p = 0, k = 0, ok = true; p < l && ok; p++, k++)
     if (s[k] == '(')
     {
      for (k++, ok = false; s[k] != ')'; k++)
       if (s[k] == w[i][p])
        ok = true;
     }
     else
     {
      ok &= (s[k] == w[i][p]);
     }
   printf ("Case #%d: %d\n", j, res);
  }
 }
 return 0;
}
