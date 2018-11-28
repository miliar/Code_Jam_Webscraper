#include<stdio.h>
#include<string.h>
#include<math.h>

int nextstep(int lastP, int lastT, int nowP, int nowT)
{
    int timeneed = abs(nowP - lastP);
    if (nowT - lastT > timeneed)
        return nowT + 1;
    else
        return lastT + timeneed + 1;
}

int main()
{
    int i, j, k;
    int t, nowt, n;
    int step, po, pb, to, tb, button;
    char str[100];
    int nexttime;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    nowt = 0;
    scanf("%d", &t);
    while (t--) {
        nowt ++;
        scanf("%d", &n);
        to = tb = 0;
        po = pb = 1;
        step = 0;
        for (i = 0; i < n; i ++) {
            scanf("%s %d", str, &button);
            if (str[0] == 'O') {
                nexttime = nextstep(po, to, button, step);
                step = nexttime;
                po = button;
                to = nexttime;
            }
            else {
                nexttime = nextstep(pb, tb, button, step);
                step = nexttime;
                pb = button;
                tb = nexttime;
            }
        }
        printf("Case #%d: %d\n", nowt, step);
    }
}
