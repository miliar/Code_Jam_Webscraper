#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int n;
int d[105][105];
struct comm {
    int r, p;
} command[105];

const int inf = int(1e9);

void go(int comnum, int srpos) {
    int pos[2];
    int curr = command[comnum].r;
    pos[curr] = command[comnum].p;
    pos[1 - curr] = srpos;
    int i, k;

    int nextr = command[comnum + 1].r;
    k = abs(pos[nextr] - command[comnum + 1].p) + 1;

    for (i = 0; i <= k && pos[1 - nextr] + i <= 100; ++i)
        d[comnum + 1][pos[1 - nextr] + i] = min(d[comnum + 1][pos[1 - nextr] + i], d[comnum][srpos] + k);

    for (i = 0; i <= k && pos[1 - nextr] - i >= 1; ++i)
        d[comnum + 1][pos[1 - nextr] - i] = min(d[comnum + 1][pos[1 - nextr] - i], d[comnum][srpos] + k);
}

int main() {
    int tests, i, k, m;
    scanf("%d\n", &tests);
    for (int cases = 1; cases <= tests; ++cases) {
        scanf("%d ", &n);
        //printf("%d\n", n);

        char rc;
        for (i = 1; i <= n; ++i) {
            scanf("%c %d", &rc, &command[i].p);
            getchar();
            if (rc == 'O')
                command[i].r = 0;
            else
                command[i].r = 1;
            //printf("%d %d\n", command[i].r, command[i].p);
        }
        command[0].r = 0;
        command[0].p = 1;

        for (i = 0; i <= n; ++i)
            for (k = 0; k <= 100; ++k)
                d[i][k] = inf;
        d[0][1] = 0;

        for (i = 0; i < n; ++i) {
            for (k = 1; k <= 100; ++k) if (d[i][k] < inf)
                go(i, k);
        }

        int res = d[n][1];
        for (k = 1; k <= 100; ++k)
            res = min(res, d[n][k]);

        printf("Case #%d: %d\n", cases, res);
    }
    return 0;
}
