#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

int nt, no, n, top;

char trans[256][256], buf[256], stack[256];
bool oppo[256][256];

void insert(char c) {
    if (top > 0 && trans[stack[top - 1]][c]) {
        top--;
        insert(trans[stack[top ]][c]);
    } else {
        int i;
        for (i = 0; i < top; i++)
            if (oppo[stack[i]][c]) {
                top = 0;
                return;
            }
        stack[top++] = c;
    }
}

int main() {
    //freopen("D:\\B-small-attempt0.in","r",stdin);
    //freopen("D:\\B-small-attempt0.out","w",stdout);
    int t, c, i;
    scanf("%d", &t);
    for (c = 1; c <= t; c++) {
        scanf("%d", &nt);
        memset(trans, 0, sizeof (trans));
        memset(oppo, 0, sizeof (oppo));
        for (i = 0; i < nt; i++) {
            scanf("%s", buf);
            trans[buf[0]][buf[1]] = trans[buf[1]][buf[0]] = buf[2];
        }
        scanf("%d", &no);
        for (i = 0; i < no; i++) {
            scanf("%s", buf);
            oppo[buf[0]][buf[1]] = oppo[buf[1]][buf[0]] = true;
        }
        scanf("%d%s", &n, buf);
        top = 0;
        for (i = 0; buf[i]; i++) {
            insert(buf[i]);
        }
        printf("Case #%d: [", c);
        if (!top)
            puts("]");
        else {
            putchar(*stack);
            for (i=1;i<top;i++)
                printf(", %c",stack[i]);
            puts("]");
        }
    }
    return 0;
}
