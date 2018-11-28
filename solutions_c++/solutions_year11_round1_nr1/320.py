#include<iostream>
using namespace std;
bool judge(long long n, long long pd, long long pg)
{
      if (pd != 100 && pg == 100)return false;
      if (pd != 0 && pg == 0)return false;
      long long g = __gcd(pd, 100ll);
      long long mn = 100 / g;
      return n >= mn;
}
int main()
{
      int cas, t;
       freopen("A-large.in", "r", stdin);
       freopen("aout.txt", "w", stdout);
      scanf("%d", &t);
      for (cas = 1; cas <= t; cas++)
      {
            long long  n, pd, pg;
            scanf("%I64d%I64d%I64d", &n, &pd, &pg);
            if (judge(n, pd, pg))
            {
                  printf("Case #%d: Possible\n", cas);
            } else
            {
                  printf("Case #%d: Broken\n", cas);
            }
      }
      return 0;
}
