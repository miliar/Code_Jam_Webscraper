#include <cstdio>
#include <cstring>

const int MAXN = 110;

int n, m1, m2;
int a[MAXN], b[MAXN];
int c[MAXN], d[MAXN];

void init()
{
   char s[10];
   scanf("%d", &n);
   m1 = m2 = 0;
   int i, j;
   for (i=1; i<=n; ++i)
   {
      scanf("%s %d", s, &j);
      if (s[0] == 'O')
      {
         a[i] = 1;
         c[++m1] = j;
      }
      else 
      {
         a[i] = 2;
         d[++m2] = j;
      }
      b[i] = j;
   }
}

void solve()
{
   int i, j, k, ans = 0;
   int r1 = 1;
   int r2 = 1;
   int l1 = 1;
   int l2 = 1;
   int l = 1;
   c[m1+1] = 0x7F7F7F7F;
   d[m2+1] = 0x7F7F7F7F;
   bool f;
   while (l <= n)
   {
      f = 0;
      if ((r1 == c[l1]) && (a[l] == 1))
      {
         ++l1;
         ++l;
         f = true;
      }
      else if (r1 > c[l1]) --r1;
      else if (r1 < c[l1]) ++r1;
      if ((r2 == d[l2]) && (a[l] == 2) && !f)
      {
         ++l2;
         ++l;
      }
      else if (r2 > d[l2]) --r2;
      else if (r2 < d[l2]) ++r2;
      ++ans;
   }
   printf("%d\n", ans);
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
