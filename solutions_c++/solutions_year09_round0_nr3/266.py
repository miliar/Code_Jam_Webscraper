#include <iostream>
using namespace std;

const int mo = 10000, maxm = 501;
const char w[20] = {' ', 'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ',
                   'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm'};
int f[maxm][20];
char a[maxm], c;
int n, m, tt;

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);
    scanf("%d\n", &n); tt = 0;
    while (n--) {
          scanf("%c", &c); m = 0;
          while (c != '\n') {
                a[++m] = c; scanf("%c", &c);
          }
          memset(f, 0, sizeof(f));
          f[0][0] = 1;
          for (int i = 0; i < m; ++i)
              for (int j = 0; j < 20; ++j) {
                  f[i + 1][j] = (f[i + 1][j] + f[i][j]) % mo;
                  if (j < 19 && a[i + 1] == w[j + 1])
                     f[i + 1][j + 1] = (f[i + 1][j + 1] + f[i][j]) % mo;
              }
          printf("Case #%d: ", ++tt);
          if (f[m][19] > 999) printf("%d\n", f[m][19]);
          else if (f[m][19] > 99) printf("0%d\n", f[m][19]);
          else if (f[m][19] > 9) printf("00%d\n", f[m][19]);
          else printf("000%d\n", f[m][19]);
    }
    return 0;
}
