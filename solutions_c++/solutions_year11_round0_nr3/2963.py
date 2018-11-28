#include <cstdio>

int main (void)
{
    int T, N, C[1000], dcount[20];
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        for (int i = 0; i < 20; i++)
            dcount[i] = 0;
        int total = 0, min = 1000000;
        for (int i = 0; i < N; i++) {
            int c;
            scanf("%d", &c);
            C[i] = c;
            total += c;
            if (c < min)
                min = c;
            int j = 0;
            while (c > 0) {
                if (c & 1) {
                    dcount[j]++;
                }
                c >>= 1;
                j = j + 1;
            }
        }
        bool possible = true;
        for (int i = 0; i < 20; i++) {
            if (dcount[i] % 2 != 0) {
                possible = false;
                break;
            }
        }
        printf("Case #%d: ", t);
        if (possible == false) {
            printf("NO\n");
        } else {
            printf("%d\n", total-min);
        }
    }
    return 0;
}


