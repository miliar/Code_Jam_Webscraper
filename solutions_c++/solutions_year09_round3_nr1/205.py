#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

typedef struct node
{
    long long p;
    char ch;
};
    
int ncase, testcase, ans[256];
int have[256], f[256], n, m, base;
node a[256];

bool cmp(node u, node v)
{
     if (u.p > v.p)
         return 1;
     return 0;
}
main()
{
      int i, j, front, r, c, k;
      char str[64];
//      freopen("A-large.in", "r", stdin);
//      freopen("A-large.out", "w", stdout);
      
      scanf("%d",&ncase);
      for (testcase = 1; testcase <= ncase; testcase++)
      {
          memset(have, 0, sizeof(have));
          scanf("%s", str);
          printf("Case #%d: ", testcase);
          m = strlen(str);
            
          for (i = 0; i < 256; i++)
          {
              a[i].ch = i;
              a[i].p = 0;
          }
          
          long long temp = 1;
          for (i = m - 1; i >= 0; i--)
          {
              have[str[i]] = 1;
              a[str[i]].p += temp;
              temp = temp * 2;
          }
              
          base = 0;
          for (i = 0; i < 256; i++)
          if (have[i])
              base++;
          if (base < 2)
              base = 2;
          sort(a, a + 256, cmp);

/*          
          for (i = 0; i < base; i++)
              printf("%c %I64d\n", a[i].ch, a[i].p);
*/
              
          f[a[0].ch] = 1;
          f[a[1].ch] = 0;
          front = 2;
          for (i = 2; i < base; i++)
              f[a[i].ch] = front++;
          memset(ans, 0, sizeof(ans));
          ans[0] = 1;
          for (i = 1; i < m; i++)
          {
              for (j = r = 0; j < 256; j++)
              {
                  c = ans[j] * base + r;
                  r = c / 10;
                  ans[j] = c % 10;
              }
              ans[0] += f[str[i]];
              for (j = r = 0; j < 256; j++)
              {
                  c = ans[j] + r;
                  r = c / 10;
                  ans[j] = c % 10;
              }
          }
          for (i = 255; i > 0; i--)
          if (ans[i] > 0)
              break;
          while (i >= 0)
              printf("%d", ans[i--]);
          printf("\n");
      }
      return 0;
}
