#include <cstdio>
#include <cstring>

void solve()
{
   int Pd, Pg;
   long long n;
   scanf("%lld %d %d", &n, &Pd, &Pg);
   if (((Pg == 0) && (Pd != 0)) || ((Pg == 100) && (Pd != 100)))
   {
      printf("Broken\n");
      return;
   }
   if (n > 100) n = 100;
   for (int i=1; i<=n; ++i)
   if (i * Pd % 100 == 0)
   {
      printf("Possible\n");
      return;
   }
   printf("Broken\n");
}

int main()
{
   int CASE, TT;
   scanf("%d", &TT);
   for (CASE=1; CASE<=TT; ++CASE)
   {
      printf("Case #%d: ", CASE);
      solve();
   }
   return 0;
}