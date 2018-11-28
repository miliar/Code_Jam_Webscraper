#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 30
#define MAXN 210
#define IDX(x) ((x) - 'A')

using namespace std;

char mat[MAX][MAX], op[MAX];
int vis[MAX];

char stk[MAXN];
int top;

char buff[MAXN];

int main() {
    int n, c, d, i, t, cnt = 1;
    char x;

//    freopen("B-small-attempt2.in", "r", stdin);
//    freopen("B-small-attempt2.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        memset(mat, -1, sizeof(mat));
        memset(op, -1, sizeof(op));
        scanf("%d", &c);
        for (i = 0; i < c; i++) {
            scanf("%s", buff);
            mat[IDX(buff[0])][IDX(buff[1])] = mat[IDX(buff[1])][IDX(buff[0])] = buff[2];
        }
        scanf("%d", &d);
        for (i = 0; i < d; i++) {
            scanf("%s", buff);
            op[IDX(buff[0])] = buff[1];
            op[IDX(buff[1])] = buff[0];
        }
        scanf("%d %s", &n, buff);
        memset(vis, 0, sizeof(vis));
        top = 0;
        for (i = 0; i < n; i++) {
            vis[IDX(stk[++top] = buff[i])]++;
            if (top > 1) {
                if (~(x = mat[IDX(stk[top])][IDX(stk[top - 1])])) {
                    vis[IDX(stk[top--])]--;
                    vis[IDX(stk[top--])]--;
                    vis[IDX(stk[++top] = x)]++;
                }
                if (~(x = op[IDX(stk[top])]) && vis[IDX(x)]) {
                    top = 0;
                    memset(vis, 0, sizeof(vis));
                }
            }
        }
        printf("Case #%d: [", cnt++);
        if (!top) printf("]\n");
        else {
            printf("%c", stk[1]);
            for (i = 2; i <= top; i++) printf(", %c", stk[i]);
            printf("]\n");
        }
    }

    return 0;
}
