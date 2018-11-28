#include <stdio.h>

int main(int argc, char* argv[])
{
    int T;
    scanf("%d\n", &T);

    for (int i=0;i<T;i++) {
        int N, K;
        scanf("%d %d\n", &N, &K);
        int pow2N = 1 << N;
//        printf("pow2N %d\n", pow2N);

        if (K>pow2N) K = K % pow2N;
            if (K==(pow2N-1)) {
                printf("Case #%d: ON\n", i+1);
            }else 
                printf("Case #%d: OFF\n", i+1);
    }
    return 0;
}
