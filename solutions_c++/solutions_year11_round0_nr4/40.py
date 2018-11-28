#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <vector>

int main(void) {
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        int elems[1000];
        std::vector<int> sorted;
        int count;
        int oop = 0;
        scanf("%d", &count);
        for (int i = 0; i < count; ++i) {
            scanf("%d", &elems[i]);
            sorted.push_back(elems[i]);
        }

        std::sort(sorted.begin(), sorted.end());
        for (int i = 0; i < count; ++i) {
            if (elems[i] != sorted[i]) ++oop;
        }
        printf("Case #%d: %d.000000\n", cC + 1, oop);
    }
}
