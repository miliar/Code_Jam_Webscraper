#include <stdio.h>
#include <iostream>
//#include <vector>
using namespace std;

typedef unsigned int ui32;

int main() {
    int T = 0;
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        int N = 0;
        scanf("%d", &N);

        ui32 sum = 0;
        ui32 minElem = 1000*1000*10;
        ui32 totalXor = 0;

        for (int j = 0; j < N; ++j) {
            ui32 v = 0;
            scanf("%d", &v);

            sum += v;
            if (v < minElem)
                minElem = v;
            totalXor ^= v;
        }

        if (totalXor == 0)
            printf("Case #%d: %d\n", i+1, sum - minElem);
        else
            printf("Case #%d: NO\n", i+1);
    }
}
