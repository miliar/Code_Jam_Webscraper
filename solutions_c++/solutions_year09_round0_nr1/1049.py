#include <stdio.h>
#include <algorithm>
using namespace std;

const int N = 5001;
const int M = 1<<26;

int L, D, n;
int a[N][16], p[16];

int main()
{
    char str[1024];
    int i, j, k;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    while (scanf("%d%d%d", &L, &D, &n) == 3)
    {
          memset(a, 0, sizeof(a));
          for (i = 0; i < D; i++)
          {
              scanf("%s", str);
              for (j = 0; j < L; j++)
                  a[i][j] = 1 << (str[j] - 'a');
          }
          for (int testcase = 1; testcase <= n; testcase++)
          {
              scanf("%s", str);
              memset(p, 0, sizeof(p));
              for (i = j = 0; i < L; i++)
              if (str[j] == '(')
              {
                  for (k = j + 1; str[k] != ')'; k++)
                      p[i] += 1 << (str[k] - 'a');
                  j = k + 1;
              } else
                  p[i] = 1 << (str[j++] - 'a');
                    
//              for (i = 0; i < L; i++) printf("p[%d] = %d\n", i, p[i]);
              int ans = 0;
              for (i = 0; i < D; i++)
              {
                  for (j = 0; j < L; j++)
                  if ((p[j] & a[i][j]) == 0)
                      break;
                  if (j >= L)
                      ans++;
              }
              printf("Case #%d: %d\n", testcase, ans);
          }
    }
    return 0;
}
