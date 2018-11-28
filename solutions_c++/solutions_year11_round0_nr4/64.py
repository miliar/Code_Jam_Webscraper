#include <cstdio>
#include <cstring>
#include <algorithm>

const int MAXN = 1100;

int n;
int a[MAXN];
int b[MAXN];

void init()
{
   scanf("%d", &n);
   for (int i=1; i<=n; ++i)
      scanf("%d", a+i);
}

void solve()
{
   memcpy(b, a, sizeof(a));
   std::sort(b+1, b+n+1);
   int i, ans = 0;
   for (i=1; i<=n; ++i)
   if (a[i] != b[i]) ++ans;
   printf("%d.000000\n", ans);
}

int main()
{
   int TT, CASE;
   scanf("%d", &TT);
   for (CASE=1; CASE<=TT; ++CASE)
   {
      init();
      printf("Case #%d: ", CASE);
      solve();
   }
   return 0;
}