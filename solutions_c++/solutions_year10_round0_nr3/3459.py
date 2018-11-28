#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int t, r, k, n, ans;
int g[1001];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    for (int casenum = 1; casenum <= t; casenum++)
    {
          scanf("%d%d%d", &r, &k, &n);
          for (int i = 0; i < n; i++)
          {
              scanf("%d", &g[i]);
          }
          int be = 0; ans = 0;
          for (int i = 0; i < r; i++)
          {
              int sum = 0;
              int id = be;
              bool sign = true;
              while (sum + g[id] <= k && (id != be || sign)) 
              {
                    sum += g[id];
                    id = (id + 1) % n;
                    sign = false;
              }
              ans += sum; be = id;
          }
          printf("Case #%d: %d\n", casenum, ans);
    }
    return 0;
}
