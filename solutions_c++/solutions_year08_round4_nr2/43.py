#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main(void) {
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;++t) {

    
        int N, M, A;

        scanf("%d%d%d", &N, &M, &A);

        int x0, y0, x1, y1, x2, y2;
        bool achei = false;

        y0 = x1 = 0;

        if(A> N*M) {
            goto done;
        }

        for(x0 = 0; x0 <= N; ++ x0) {
            for(y1 = 0; y1 <= M; ++y1) {
                if(A > (N+M) * (int(sqrt(x0*x0+y1*y1))+1) ) {
                    continue;
                }
                int v0x = x1-x0;
                int v0y = y1-y0;
                if(v0x == 0 or v0y == 0) continue;
                for(x2=0;x2<=N;++x2) {
                    for(int s = -1; s <= 1; s += 2) {
                        int v1x = x2-x1;
                        int v1y = A*s + v1x*v0y;
                        if(v1y % v0x != 0) {
                            continue;
                        }
                        v1y /= v0x;

                        y2 = y1 + v1y;

                        if(y2 >= 0 and y2 <= M) {
                            achei = true;
                            goto done;
                        }
                    }
                }
            }
        }

done:



        printf("Case #%d: ", t);

        if(achei) {
            printf("%d %d %d %d %d %d", x0, y0, x1, y1, x2, y2);
        } else {
            printf("IMPOSSIBLE");
        }
        printf("\n");
    }
    return 0;
}
