#include <stdio.h>

long long gcd(int a, int b) {
    long long c;
    while (a != 0) {
        c = a; a = b%a;  b = c;
    }
    return b;
}


int main() {
    int T;
    scanf("%d", &T);
    for (int num = 1; num <= T; ++num) {
        int s[10000];
        int N, L, H;
        scanf("%d", &N);
        scanf("%d", &L);
        scanf("%d", &H);
        for (int i = 0; i < N; ++i)
            scanf("%d", &s[i]);
        int flag;
        for (int x = L; x <= H; ++x) {
            flag = 0;
            for (int i = 0; i < N; ++i) {
                if (x % s[i] != 0 && s[i] % x != 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                printf("Case #%d: %d\n", num, x);
                break;
            }
        }
        if (flag == 1) {
            printf("Case #%d: NO\n", num);
        }
    }
    return 0;
}
