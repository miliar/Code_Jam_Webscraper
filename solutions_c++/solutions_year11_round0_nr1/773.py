#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int len;
char blor[1 << 7];
int but[1 << 7];

int go() {
    int b_time = 0;
    int o_time = 0;
    int b_pos = 1;
    int o_pos = 1;

    for (int i = 0; i < len; ++i) {
        if (blor[i] == 'B') {
            b_time = max(b_time + abs(but[i] - b_pos), o_time) + 1;
            b_pos = but[i];
        } else {
            o_time = max(o_time + abs(but[i] - o_pos), b_time) + 1;
            o_pos = but[i];
        }
    }

    return max(b_time, o_time);
}

int main() {
    int kases;

    scanf("%d", &kases);
    for (int k = 1; k <= kases; ++k) {
        scanf("%d", &len);
        for (int i = 0; i < len; ++i) scanf(" %c%d", blor + i, but + i);

        printf("Case #%d: %d\n", k, go());
    }

    return 0;
}
