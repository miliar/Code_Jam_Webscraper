#include <stdio.h>

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-out.txt", "w", stdout);
    int x, t, a, b, i, j, k, f, lastk, n, m, resp, aux, nmemo, rep;
    int pot[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
    int memo[20];

    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%d %d", &a, &b);
        resp = 0;
        n = 0;
        aux = a;
        while(aux > 0) {
            aux /= 10;
            n++;
        }
        for(i = a; i < b; i++) {
            if(i == pot[n+1]) n++;
            f = i/10;
            nmemo = 0;
            for(lastk = i%10, k = 1; f > 0; k++) {
                m = pot[n-k]*lastk + f;
                if(m > i && m <= b) {
                    rep = 0;
                    for(j = 0; j < nmemo; j++)
                        if(m == memo[j]) {
                            rep = 1;
                            break;
                        }
                    if(rep == 0) {
                        resp++;
                        memo[nmemo++] = m;
                    }
                }
                lastk = (f%10)*pot[k] + lastk;
                f = f/10;
            }
        }
        printf("Case #%d: %d\n", x, resp);
    }
    return 0;
}
