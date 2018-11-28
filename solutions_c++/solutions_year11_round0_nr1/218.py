#include <cstdio>
#include <cstdlib>
#include <cstring>

int t1, t2, p1, p2, n;
char cmd[10];

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int Test; scanf("%d", &Test);
    for (int tts = 1; tts <= Test; ++tts) {
        printf("Case #%d: ", tts);
        scanf("%d", &n);
        t1 = t2 = 0; p1 = p2 = 1;
        for (int i = 1; i <= n; ++i) {
            int k;
            scanf("%s %d", cmd, &k);
            if (cmd[0] == 'O') {
                if (t1 + abs(p1 - k) + 1 > t2) t1 += abs(p1 - k) + 1;
                else t1 = t2 + 1;
                p1 = k;
            } else {
                if (t2 + abs(p2 - k) + 1 > t1) t2 += abs(p2 - k) + 1;
                else t2 = t1 + 1;
                p2 = k;
            }
        }
        if (t2 > t1) t1 = t2;
        printf("%d\n", t1);
    }
    return 0;
}
