#include <stdio.h>
#include <memory.h>
#include <algorithm>

const char PLAYERS[] = {'X', 'O'};
const char *RESULT[] = {"X won", "O won", "Draw", "Game has not completed"};

char B[4][5];

bool check(const char *p, int stride, char player) {
    for (int i = 0; i < 4; i++, p += stride) {
        if (*p != player && *p != 'T')
            return false;
    }
    return true;
}

const char* solve() {
    scanf("%s %s %s %s", B[0], B[1], B[2], B[3]);
    for (int p = 0; p < 2; p++) {
        for (int i = 0; i < 4; i++) {
            if (check(B[i], 1, PLAYERS[p]) || check(&B[0][i], 5, PLAYERS[p]))
                return RESULT[p];
        }
        if (check(B[0], 6, PLAYERS[p]) || check(&B[0][3], 4, PLAYERS[p]))
            return RESULT[p];
    }
    if (memchr(B, '.', sizeof(B)))
        return RESULT[3];
    else
        return RESULT[2];
}

int main() {
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; i++)
        printf("Case #%d: %s\n", i, solve());
    return 0;
}
