#include <cstdio>
#include <cstring>

const int MAXN = 1100;

int n, t, s;
int a[MAXN];

void init()
{
   scanf("%d", &n);
   t = 0;
   s = 0;
   for (int i=1; i<=n; ++i)
   {
      scanf("%d", a+i);
      t ^= a[i];
      s += a[i];
   }
}

void solve()
{
   if (t != 0)
   {
      printf("NO\n");
      return;
   }
   int min= a[1];
   for (int i=2; i<=n; ++i)
   {
      if (a[i] < min) min = a[i];
   }
   printf("%d\n", s - min);
}

int main()
{
   int TT, CASE;
   scanf("%d", &TT);
   for (CASE=1; CASE <= TT; ++CASE)
   {
      init();
      printf("Case #%d: ", CASE);
      solve();
   }
   return 0;
}