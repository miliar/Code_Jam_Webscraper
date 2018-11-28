#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <vector>

int main(void) {
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        int nPieces;
        std::vector<int> vals;
        scanf("%d", &nPieces);
        int sum = 0;
        int xorsum = 0;
        for (int i = 0; i < nPieces; ++i) {
            int inval;
            scanf("%d", &inval);
            sum += inval;
            xorsum ^= inval;
            vals.push_back(inval);
        }

        if (xorsum) {
            printf("Case #%d: NO\n", cC + 1);
        } else {
            std::sort(vals.begin(), vals.end());
            sum -= vals[0];
            printf("Case #%d: %d\n", cC + 1, sum);
        }
    }
}
