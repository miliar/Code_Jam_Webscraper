#include <cstdio>

int main() {
    int ox, bx, n, t, cas, x, dis, i, oc, bc;
    char op[2], pre;

//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    for (cas = 0; cas < t; cas++) {
        ox = bx = 1;
        oc = bc = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s", op);
            scanf("%d", &x);
            if (!i) pre = op[0];
            if (op[0] == 'O') {
                dis = (ox - x) > 0 ? (ox - x) : (x - ox);
                ox = x;
            }
            else {
                dis = (bx - x) > 0 ? (bx - x) : (x - bx);
                bx = x;
            }

            if (op[0] == pre) {
                if (op[0] == 'O') {
                    oc += dis + 1;
                }
                else {
                    bc += dis + 1;
                }
            }
            else {
                pre = op[0];
                if (op[0] == 'O') {
                    if (dis + oc <= bc) {
                        oc = bc + 1;
                    }
                    else {
                        oc += dis + 1;
                    }
                }
                else {
                    if (dis + bc <= oc) {
                        bc = oc + 1;
                    }
                    else {
                        bc += dis + 1;
                    }
                }
            }
        }

        printf("Case #%d: %d\n", cas + 1, bc > oc ? bc : oc);
    }

    return 0;
}
