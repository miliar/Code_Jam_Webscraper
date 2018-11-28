#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int a[3][101];
char q[101];

int min(int a, int b)
{
    if (a < b) return a;
    else return b;
}

int main()
{
    int t, cases, n, i, p, h1, h2, tt, n1, n2;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for (cases = 1; cases <= t; cases++) {
        scanf("%d", &n);
        a[1][0] = 0; a[2][0] = 0;
        for (i = 1; i <= n; i++) {
            scanf("%c%c%d", &q[i], &q[i], &p);
            if (q[i] == 'O') a[1][++a[1][0]] = p;
            else a[2][++a[2][0]] = p;
        }
        h1 = 0; h2 = 0; tt = 0; n1 = 1; n2 = 1;
        for (i = 1; i <= n; i++)
            if (q[i] == 'O') {
                h1++;
                if (h2 < a[2][0])
                    if (n2 < a[2][h2 + 1]) n2 += min(abs(n1 - a[1][h1]) + 1, a[2][h2 + 1] - n2);
                    else n2 -= min(abs(n1 - a[1][h1]) + 1, n2 - a[2][h2 + 1]);
                tt += abs(n1 - a[1][h1]) + 1;
                n1 = a[1][h1];
            }
            else {
                h2++;
                if (h1 < a[1][0])
                    if (n1 < a[1][h1 + 1]) n1 += min(abs(n2 - a[2][h2]) + 1, a[1][h1 + 1] - n1);
                    else n1 -= min(abs(n2 - a[2][h2]) + 1, n1 - a[1][h1 + 1]);
                tt += abs(n2 - a[2][h2]) + 1;
                n2 = a[2][h2];
            }
        printf("Case #%d: %d\n", cases, tt);
    }
    return 0;
}
