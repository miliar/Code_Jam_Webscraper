#include <stdio.h>
//#include <math.h>
#include <algorithm>

int main() {
    int T = 0;
    scanf("%d", &T);

    for (int i = 0; i < T; ++i) {
        int res = 0;
        int N = 0;
        scanf("%d", &N);
        int oPos = 1, bPos = 1;
        int oLMTime = 0, bLMTime = 0;
        for (int j = 0; j < N; ++j) {
            char R[3];
            int p;
            scanf("%s %d", R, &p);

            if (R[0] == 'O') {
                if (oPos != p) {
                    const int waitTime = res - oLMTime;
                    const int len = abs(p - oPos);
                    if (len > waitTime)
                        res += (len - waitTime);
                }
                oPos = p;
                oLMTime = res + 1;
            } else {
                if (bPos != p) {
                    const int waitTime = res - bLMTime;
                    const int len = abs(p - bPos);
                    if (len > waitTime)
                        res += (len - waitTime);
                }
                bPos = p;
                bLMTime = res + 1;
            }
            ++res;
            //printf("%d\t%d\t%d\n", res, oPos, bPos);
        }
        printf("Case #%d: %d\n", i+1, res);
    }

}
