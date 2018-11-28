#include <iostream>
#include <algorithm>
typedef unsigned long long uint64;
uint64 N, n, A, B, C, D, M,
    xs[100001], ys[100001];

int main() {
    std::cin >> N;
    for (uint64 i=1; i<=N; i++) {
        uint64 count = 0;
        std::cin >> n >> A >> B >> C >> D >> xs[0] >> ys[0] >> M;
        for (uint64 j=1; j<n; j++) {
            xs[j] = (A * xs[j-1] + B) % M;
            ys[j] = (C * ys[j-1] + D) % M;
            for (uint64 k=1; k<j; k++)
            for (uint64 l=0; l<k; l++) {
                //printf("Trees: (%d,%d) (%d,%d) (%d,%d) = %d, %d\n", xs[j], ys[j], xs[k], ys[k], xs[l], ys[l],
                    //(xs[j]+xs[k]+xs[l]) % 3, ys[j]+ys[k]+ys[l] % 3);
                if ((xs[j]+xs[k]+xs[l]) % 3 == 0 &&
                    (ys[j]+ys[k]+ys[l]) % 3 == 0)
                    count++;
            }
        }
        printf("Case #%llu: %llu\n", i, count);
    }
}
