#define MAXN 30
#define L 1010

#include <cstdio>
#include <cstring>

int main() {
    int t, i, j, c, d, n, top, cas;
    char com[MAXN][MAXN], cla[MAXN][MAXN], stack[L], buff[L];

//    freopen("B-large.in", "r", stdin);
//    freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    for (cas = 1; cas <= t; cas++) {
        memset(com, -1, sizeof(com));
        memset(cla, 0, sizeof(cla));
        top = 0;

        scanf("%d", &c);
        for (i = 0; i < c; i++) {
            scanf("%s", buff);
            com[buff[0] - 'A'][buff[1] - 'A'] = buff[2] - 'A';
            com[buff[1] - 'A'][buff[0] - 'A'] = buff[2] - 'A';
        }
        scanf("%d", &d);
        for (i = 0; i < d; i++) {
            scanf("%s", buff);
            cla[buff[0] - 'A'][buff[1] - 'A'] = cla[buff[1] - 'A'][buff[0] - 'A'] = 1;
        }
        scanf("%d", &n);
        scanf("%s", buff);

        for (i = 0; i < n; i++) {
            stack[top++] = buff[i] - 'A';
            while (top > 1 && com[stack[top - 1]][stack[top - 2]] != -1) {
                stack[top - 2] = com[stack[top - 1]][stack[top - 2]];
                top--;
            }
            for (j = 0; j < top - 1; j++) {
                if (cla[stack[top - 1]][stack[j]]) {
                    top = 0;
                    break;
                }
            }
        }

        printf("Case #%d: [", cas);
        for (i = 0; i < top; i++) {
            if (i) printf(", ");
            printf("%c", stack[i] + 'A');
        }
        printf("]\n");
    }

    return 0;
}
