#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

char c[100][100];
char d[100][100];
char ans[110];
char s[110];

int main()
{
    freopen("s.in", "r", stdin);
    freopen("s.out", "w", stdout);
    int i, n, t;
    char a, b, e;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas ++) {
        memset(c, 0, sizeof c);
        memset(d, 0, sizeof d);
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            getchar();
            scanf("%c%c%c", &a, &b, &e);
            c[a][b] = c[b][a] = e;
        }
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            getchar();
            scanf("%c%c%c", &a, &b, &e);
            d[a][b] = d[b][a] = e;
        }
        int top = -1;
        scanf("%d %s", &n, s);
        for (i = 0; i < n; i++) {
            if (top == -1) {
                ans[++top] = s[i];
                continue;
            }
            else ans[++top] = s[i];
            while (e = c[ans[top]][ans[top - 1]]) {
                ans[top - 1] = e;
                top--;
            }
            for (int j = 0; j < top; j++)
                if (d[ans[top]][ans[j]]) {
                    top = -1;
                    break;
                }
        }
        if (top == -1) {
            printf("Case #%d: []\n", cas);
            continue;
        }
        printf("Case #%d: [%c", cas, ans[0]);
        for (i = 1; i <= top; i++)
            printf(", %c", ans[i]);
        printf("]\n");
    }
    return 0;
}
