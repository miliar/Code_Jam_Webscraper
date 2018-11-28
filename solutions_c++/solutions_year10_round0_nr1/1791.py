#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>

int main(void) {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        int n, k;
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", i);
        if ((k & (1<<(n-1))) && !((k+1) & (1<<(n-1))))
            printf("ON");
        else
            printf("OFF");
        printf("\n");
    }
    return 0;
}
