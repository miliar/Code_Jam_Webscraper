#include<cstdio>

#define DEBUG

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

#ifdef DEBUG
    printf("num tests = %d\n", T);
#endif

    int N;
    unsigned int k, mask;
    bool result;
    for (int t=1; t<=T; ++t) {
        scanf("%d%u", &N, &k);
#ifdef DEBUG
        printf("N = %d, k = %u\n", N, k);
#endif

        mask = (1 << N) - 1;
        result = ((mask & k) == mask);
#ifdef DEBUG
        printf("mask = %u, result = %d\n", mask, result);
#endif
        if (result) {
            printf("Case #%d: ON\n", t);
        } else {
            printf("Case #%d: OFF\n", t);
        }
    }

    return 0;
}
