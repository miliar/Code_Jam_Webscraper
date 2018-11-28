#include <cstdio>

int f[31];

int main()
{
   freopen("input", "r", stdin);
   freopen("output", "w", stdout);
   f[0] = 0;
   for (int i = 1; i <= 30; i++)
     f[i] = f[i - 1] * 2 + 1;
   int t;
   int n,k;
   scanf("%d", &t);
   for (int i = 0; i < t; i++)
   {
      scanf("%d%d", &n, &k);
      printf("Case #%d: ", i + 1);
      if (f[n] == k % (f[n] + 1))
        puts("ON");
      else
        puts("OFF");
   }
   return 0;
}
