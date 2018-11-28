#include <stdio.h>

/*for(a = 10; a >= 0; a--) {
                for(b = a; b >= a-2 && b >= 0; b--) {
                    c = total - a - b;
                    if(c >= 0 && c <= b && a-c <= 2) {
                        printf("%d %d %d", a, b, c);
                        ok = 1;
                        if(a == c+2 || a == b+2 || b == c+2) {
                            printf(" s");
                            sups++;
                        }
                        printf("\n");
                    }
                }
            }
            printf("\n");*/

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-out.txt", "w", stdout);
    int x, y, ys, t, n, s, p, total, a, b, c, i, j, v[50][5];

    for(total = 0; total <= 30; total++) {
        j = 0;
        for(a = 10; a >= 0; a--) {
            for(b = a; b >= a-2 && b >= 0; b--) {
                c = total - a - b;
                if(c >= 0 && c <= b && a-c <= 2) {
                    v[total][j++] = a;
                    v[total][j] = -1;
                }
            }
        }
    }

    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%d %d %d", &n, &s, &p);
        y = ys = 0;
        for(i = 0; i < n; i++) {
            scanf("%d", &total);
            if( total < 2 || total > 28 ) y = v[total][0] >= p? y+1 : y;
            else if(v[total][0] >= p) {
                if(v[total][1] >= p)
                    y++;
                else
                    ys++;
            }
        }
        printf("Case #%d: %d\n", x, ys > s? y + s : y + ys);
    }
    return 0;
}
