#include <cstdio>
#include <cstring>

const int MAXN = 85;

struct Tcard
{
   int c, s, t;
};

struct Tstatu
{
   bool chk[MAXN];
   int p;
   int value;
   int left;
};

inline int max(int a, int b)
{
   return a>b ? a : b;
}

int n, m;
Tcard a[MAXN];
int ans;
Tstatu stack[MAXN];

void init()
{
   scanf("%d", &n);
   for (int i=1; i<=n; ++i)
      scanf("%d %d %d", &a[i].c, &a[i].s, &a[i].t);
   int k = n;
   scanf("%d", &m);
   for (int i=1; i<=m; ++i)
      scanf("%d %d %d", &a[n+i].c, &a[n+i].s, &a[n+i].t);
   n += m;
   m = k;
}

void print(Tstatu &b)
{
   for (int i=1; i<=n; ++i)
      printf("%d", b.chk[i]);
   printf(" %d %d %d\n", b.p, b.left, b.value);
}

void deal(Tstatu &b)
{
   int maxt, i, j;
   while (1)
   {
      maxt = -1;
      for (i=1; i<=b.p; ++i)
      if (!b.chk[i] && (a[i].t > maxt))
      {
         maxt = a[i].t;
         j = i;
      }
      if (maxt <= 0) return;
      b.chk[j] = true;
      b.p += a[j].c;
      if (b.p > n) b.p = n;
      b.left += maxt - 1;
      b.value += a[j].s;
   }
}

void dfs(int dep)
{
   if (stack[dep].left == 0) 
   {
      //print(stack[dep]);
      ans = max(stack[dep].value, ans);
      return;
   }
   deal(stack[dep]);
   //print(stack[dep]);
   ans = max(stack[dep].value, ans);
   int maxs, i, j, k;
   for (k=0; k<=2; ++k)
   {
      maxs = -1;
      for (i=1; i<=stack[dep].p; ++i)
      if (!stack[dep].chk[i] && (a[i].c == k) && (a[i].s > maxs))
      {
         maxs = a[i].s;
         j = i;
      }
      if (maxs == -1) continue;
      stack[dep+1] = stack[dep];
      stack[dep+1].chk[j] = true;
      stack[dep+1].p += a[j].c;
      if (stack[dep+1].p > n) stack[dep+1].p = n;
      stack[dep+1].left -= 1;
      stack[dep+1].value += a[j].s;
      dfs(dep+1);
   }
}

void solve()
{
   ans = 0;
   memset(stack[0].chk, 0, sizeof(stack[0].chk));
   stack[0].left = 1;
   stack[0].value = 0;
   stack[0].p = m;
   dfs(0);
   printf("%d\n", ans);
}

int main()
{
   int CASE, TT;
   scanf("%d", &TT);
   for (CASE=1; CASE<=TT; ++CASE)
   {
      init();
      printf("Case #%d: ", CASE);
      solve();
   }
   return 0;
}