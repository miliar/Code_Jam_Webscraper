#include <vector>
#include <algorithm>
#include <sstream>
#include <utility>
#include <cstdio>
#include <iostream>

using namespace std;



int main(void)
{
    int T, N, S, p;
    int cur, cnt;
    bool ans = false;

    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        scanf("%d %d %d\n", &N, &S, &p);
        cnt = 0;

        for (int j = 0; j < N; ++j) {
            scanf("%d", &cur);

            if (cur - p >= 0 && cur - (3 * (p - 2) + 2) >= 0) {
                if ((cur - p - 2 * (p - 1)) >= 0) {
                    ++cnt;
                } else if (S) {
                    --S;
                    ++cnt;
                }
            }
        }

        printf("Case #%d: %d\n", t, cnt);
    }

    return 0;
}
