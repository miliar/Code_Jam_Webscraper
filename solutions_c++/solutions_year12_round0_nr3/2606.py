#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
int a[10000000];
              
int main (void)
{
  int test, tests;

  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, k, A, B, tres, t, d;
    long long res;
    scanf ("%d %d", &A, &B);
    memset (a, 0, sizeof a);
    res = 0;
    t = A / 10; d = 1;
    while (t > 0)
    {
      t /= 10;
      d *= 10;
    }
    for (i = A; i <= B; i++)
    {
      k = i;
      tres = 0;
      do 
      {
        if (a[k] == 0)
        {
          if (A <= k && k <= B)
            tres++;
        }  
        a[k] = i;
        k = k % 10 * d + k / 10;
        
      } while (k != i);
      res += tres * (tres - 1) / 2;
    }  
    printf ("Case #%d: %I64d\n", test + 1, res);
    
  }
  return 0;
}
