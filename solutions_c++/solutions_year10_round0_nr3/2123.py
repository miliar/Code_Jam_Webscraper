#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <deque>
#include <iostream>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

int f[2002],next[2002];
double a[2002],num[2002];

int main()
{
    freopen("c1.in","r",stdin);
    freopen("c1.ou","w",stdout);
    int T;
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
          printf("Case #%d: ", it);
          int r,n;  double k;
          scanf("%d %lf %d", &r, &k, &n);
          for (int i = 1; i <= n; i++) scanf("%lf", &a[i]);
          for (int i = 1; i <= n; i++) a[i + n] = a[i];
          
          //Special case
          double total = 0;
          for (int i = 1; i <= n; i++) total += a[i];
          if (total <= k)
          {
                    double ret = (double) r * total;
                    printf("%.0lf\n", ret);
          }
          else
          {
              for (int i = 1; i <= n; i++)
              {
                  next[i] = i;
                  num[i] = a[i];
                  while (num[i] <= k)
                  {
                        next[i]++;  num[i] += a[next[i]];
                  };
                  num[i] -= a[next[i]];  if (next[i] > n) next[i] -= n;
              };
              double ret = 0;  int st = 1;  int time = 0;
              memset(f,0,sizeof(f));
              while (1)
              {
                    time++;
                    if (f[st] || time > r) break;
                    f[st] = time;
                    ret += num[st];  st = next[st];
              };
              if (time <= r)
              {
                int cur = next[st];  double lencyc = num[st];
                while (cur != st)
                {
                    lencyc += num[cur];  cur = next[cur];
                };
                r -= (time - 1);
                int cycle = r/(time - f[st]);
                ret += (double) cycle * lencyc;
                r %= (time - f[st]);
                while (r)
                {
                    r--;
                    ret += num[st];  st = next[st];
                };
              };
              printf("%.0lf\n", ret);
          };
    };
};
