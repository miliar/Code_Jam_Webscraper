#include <cstdio>
#include <algorithm>
using namespace std;

int N, C, M, A;

int main() {
    scanf("%d", &C);
    for (int cix=0; cix<C; cix++) {
        scanf("%d%d%d", &N, &M, &A);
        for (int x0=-N; x0<=N; x0++)
            for (int y0=-M; y0<=M; y0++)
                for (int x1=-N; x1<=N; x1++)
                    for (int y1=-M; y1<=M; y1++) {
                        int l=min(x0, x1);
                        int d=min(y0, y1);
                        //if (l<-N || d<-M) continue;
                        if (l>0) l=0;
                        if (d>0) d=0;
                        l=-l, d=-d;
                        if (x0+l<0 || x0+l>N || x1+l<0 || x1+l>N) continue;
                        if (y0+d<0 || y0+d>M || y1+d<0 || y1+d>M) continue;
                        int AA=x1*y0-y1*x0;
                        //printf("%d\n", AA);
                        if (AA<0) AA=-AA;
                        if (AA==A) {
                            printf("Case #%d: %d %d %d %d %d %d\n", cix+1, l, d, x0+l, y0+d, x1+l, y1+d);
                            goto next;
                        }
                    }
        
        printf("Case #%d: IMPOSSIBLE\n", cix+1);
        next: {}
    }
    return 0;
}
