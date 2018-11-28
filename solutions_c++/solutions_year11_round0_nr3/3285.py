#include <stdio.h>

#define add_patrick(a, b) (((a) & (~(b))) | ((~(a)) & (b)))
#define extract_bit(a, n) ((a >> n) & 1)

int t, n, n2, y, patrick, sean, value;

int main()
{
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d", &n);
        n2 = 2 << (n-1);
        int candies[n];
        for (int j = 0; j < n; j++) {
            scanf("%d", &(candies[j]));
        }
        y = 0;
        for (int j = 1; j < n2; j++) {
            patrick = sean = value = 0;
            for (int k = 0; k < n; k++) {
                if (extract_bit(j, k)) {
                    patrick = add_patrick(patrick, candies[k]);
                }
                else {
                    sean = add_patrick(sean, candies[k]);
                    value += candies[k];
                }
            }
            if ((patrick == sean) && (value > y)) {
                y = value;
            }
        }
        printf("Case #%d: ", i);
        if (y > 0) {
            printf("%d", y);
        }
        else {
            printf("NO");
        }
        printf("\n");
    }
}