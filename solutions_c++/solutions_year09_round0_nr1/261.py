#include <iostream>
using namespace std;

const int maxd = 50001, maxn = 501, maxl = 16;
char a[maxd][maxl];
bool v[maxl][300];
int n, d, l;

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    char c; int i, j, k, t;
    scanf("%d%d%d\n", &l, &d, &n);
    for (i = 1; i <= d; ++i) {
        scanf("%c", &c); j = 0;
        while (c != '\n') {
              a[i][++j] = c; scanf("%c", &c);
        }
    }
    for (i = 1; i <= n; ++i) {
        memset(v, 0, sizeof(v));
        scanf("%c", &c); j = 0;
        while (c != '\n') {
              ++j;
              if (c == '(')
                 while (c != ')') {
                       v[j][c] = true;
                       scanf("%c", &c);
                 }
              else
                  v[j][c] = true;
              scanf("%c", &c);
        }
        t = 0;
        for (j = 1; j <= d; ++j) {
            k = 1;
            while (k <= l && v[k][a[j][k]]) ++k;
            if (k > l) ++t;
        }
        printf("Case #%d: %d\n", i, t);
    }
    return 0;
}
