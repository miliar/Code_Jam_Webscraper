#include <stdio.h>
#include <stdlib.h>

int main() {
    int Ntc;
    scanf("%d", &Ntc);
    for (int tc = 0; tc < Ntc; tc++) {
        printf("Case #%d: ", tc+1);
        int W, H, A;
        scanf("%d %d %d", &W, &H, &A);
        for (int x1 = 0; x1 <= W; x1++)
            for (int y1 = 0; y1 <= H; y1++)
                for (int x2 = 0; x2 <= W; x2++)
                    for (int y2 = 0; y2 <= H; y2++) {
                        if (abs(x1*y2 - x2*y1) == A) {
                            printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
                            goto nexttc;
                        }
                    }
        printf("IMPOSSIBLE\n");
        nexttc:
        int k =0;
    }
    return 0;
}
