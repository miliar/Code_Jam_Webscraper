#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);

    int N, S, P, Mt, Mt2, t, G;
    for(int i = 1; i <= T; ++i) {
        G = 0;
        scanf("%d %d %d", &N, &S, &P);
        Mt = 3 * P - 2;
        Mt2 = (Mt - 2 > P) ? (Mt - 2) : P;
        for(int j = 0; j < N; ++j) {
            scanf("%d", &t);
            if (t >= Mt) {
                ++G;
            }
            else if (t >= Mt2) {
                if(S > 0) {
                    ++G;
                    --S;
                }
            }
        }
        printf("Case #%d: %d\n", i, G);
    }
    return 0;
}
