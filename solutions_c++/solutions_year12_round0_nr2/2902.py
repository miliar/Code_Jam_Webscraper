#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <assert.h>

int main(int argc, char *argv[])
{
    int T;
    scanf("%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        int N, S, p;
        std::cin >> N >> S >> p;
        int total = 0;
        for (int j = 0; j < N; ++j) {
            int t; // total score
            std::cin >> t;
            const int mp = t / 3;
            if (p <= mp) {
                total++;
                continue;
            }
            t -= p; // try assign p to first judge
            if (t < 0) {
                continue;
            }
            if (t % 2 == 0) {
                int avg = t/2;
                const int diff = abs(avg - p);
                if (diff > 2) {
                    continue;
                }
                if (diff == 2) {
                    if (S > 0) {
                        S--;
                        total++;
                    }
                    continue;
                }
                assert(diff < 2);
                total++;
                continue;
            }
            else {
                int smaller = t/2;
                int larger = smaller + 1;
                const int diff1 = abs(smaller - p);
                const int diff2 = abs(larger - p);
                if (diff1 < 2 && diff2 < 2) {
                    total++;
                    continue;
                }
                if (diff1 < 2 || diff2 < 2 || (diff1 == 2 && diff2 == 2)) {
                    if (S > 0) {
                        S--;
                        total++;
                        continue;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", i, total);
    }
    return 0;
}
