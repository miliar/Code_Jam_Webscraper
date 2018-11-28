#include <cstdio>
#include <cstring>

using namespace std;

int gen[300][300];
int vis[300][300];
char sta[310];
int cc[310];

int main()
{
    int cn, cns;
    char str[310];

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        int c, d, n;
        scanf("%d", &c);
        memset(vis, 0, sizeof(vis));
        memset(gen, -1, sizeof(gen));
        for (int i = 0; i < c; i++) {
            scanf("%s", str);
            gen[str[0]][str[1]] = str[2];
            gen[str[1]][str[0]] = str[2];
        }
        scanf("%d", &d);
        for (int i = 0; i < d; i++) {
            scanf("%s", str);
            vis[str[0]][str[1]] = 1;
            vis[str[1]][str[0]] = 1;
        }
        scanf("%d", &n);
        scanf("%s", str);
        int top = 0;
        //memset(cc, 0, sizeof(cc));
        for (int i = 0; i < n; i++) {
            if (top > 0 && gen[sta[top - 1]][str[i]] != -1) {
                //cc[sta[top - 1]]--;
                char ch = gen[sta[top - 1]][str[i]];
                top--;
                sta[top++] = ch;
                //cc[sta[top - 1]]++;
            } else {
                bool ok = true;
                for (int j = 0; j < top; j++) {
                    if (vis[sta[j]][str[i]]) {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                    sta[top++] = str[i];
                else
                    top = 0;
                //cc[sta[top - 1]]++;
            }
        }
        printf("Case #%d: [", cn + 1);
        for (int i = 0; i < top; i++) {
            printf("%c", sta[i]);
            if (i != top - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    return 0;
}
