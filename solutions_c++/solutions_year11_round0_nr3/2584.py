#include <iostream>
#include <cstdio>

int compare (const void * a, const void * b) {
      return ( *(int*)a - *(int*)b );
}

int main() {
    int T; scanf("%d", &T);
    for(int Ti = 1; Ti <= T; ++Ti) {
        int N; scanf("%d", &N);
        int X[1005];
        int x = 0;
        for(int Ni = 0; Ni < N; ++Ni) {
            scanf("%d", &X[Ni]);
            x = x ^ X[Ni];
        }
        if(x != 0)
            printf("Case #%d: NO\n", Ti);
        else {
            qsort(X, N, sizeof(int), compare);
            int Y[1005];
            Y[0] = X[0];
            for(int i = 1; i < N; ++i) {
                Y[i] = Y[i-1] + X[i];
                //printf("Y[%d]=%d", i, Y[i]);
            }
            int y = 0;
            int output = 0;

            for(int j = N-1; j >0; --j) {
                y = y^X[j];
                if (y == X[j-1]) {
                    output = Y[N-1] - Y[j-1];
                }

            }
            printf("Case #%d: %d\n", Ti, output);
        }
    }
}
