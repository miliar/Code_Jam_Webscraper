#include <iostream>
using namespace std;

int task, n, a[46];
char ch;

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    int i, j, t, ans, p = 0;
    scanf("%d", &task);
    while (task--) {
          scanf("%d\n", &n);
          memset(a, 0, sizeof(a));
          for (i = 1; i <= n; ++i) {
              for (j = 1; j <= n; ++j) {
                  scanf("%c", &ch);
                  if (ch == '1') a[i] = j;
              }
              scanf("\n");
          }
          ans = 0;
          for (i = 1; i <= n; ++i) {
              if (a[i] <= i) continue;
              j = i + 1;
              while (a[j] > i) ++j;
              ans += j - i;
              for (t = j; t > i; --t)
                  a[t] = a[t - 1];
          }
          printf("Case #%d: %d\n", ++p, ans);
    }
    return 0;
}
