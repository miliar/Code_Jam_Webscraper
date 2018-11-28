#include <cstdio>

int main()
{
  int TestCases;
  scanf("%d", &TestCases);
  
  for (int T = 1; T <= TestCases; T++)
  {
    int n, k, b, t, v[50], x[50];
    scanf("%d%d%d%d", &n, &k, &b, &t);
    for (int i = 0; i < n; i++)
      scanf("%d", &x[i]);
    for (int i = 0; i < n; i++)
      scanf("%d", &v[i]);
      
    int count = 0, res = 0, i = n-1;
    while (i >= 0 && k > 0)
    {
      while (i >= 0 && t*v[i] < (b-x[i]))
      {
        count++;
        i--;
      }
      if (i < 0)
        break;
      //printf(">%d\n", i);
      res += count;
      i--;
      k--;
    }
    
    if (k > 0)
      printf("Case #%d: IMPOSSIBLE\n", T);
    else
      printf("Case #%d: %d\n", T, res);
  }
  
  return 0;
}
