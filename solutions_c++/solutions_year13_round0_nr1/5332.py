#include <cstdio>

char tab[17];
int T, x, y, i, turns, s0, s1, s2, s3, sum, win, twin;

int s(int p1, int p2, int p3, int p4) {
    return tab[p1] + tab[p2] + tab[p3] + tab[p4];
}

int p() {
    if (sum == s0 || sum == s1) return 1;
    if (sum == s2 || sum == s3) return 2;
    return 0;
}

void pp() {
    if (win == 1) return;
    twin = p();
    if (twin) win = twin;
}

int main() {
    scanf("%d\n", &T);
    for (int t = 0; t < T; ++t) {
        for (y = 0; y < 4; ++y) {
            scanf("%s\n", tab + y * 4);
        }
        scanf("\n");
        turns = 0;
        for (i = 0; i < 16; ++i) {
            if (tab[i] != '.') ++turns;
        }
        if (turns % 2) {
            s0 = 348;
            s1 = 352;
            s2 = 316;
            s3 = 321;
        } else {
            s0 = 316;
            s1 = 321;
            s2 = 348;
            s3 = 352;
        }
        win = 0;
        for (y = 0; y < 4; ++y) {
            sum = s(y * 4, y * 4 + 1, y * 4 + 2, y * 4 + 3);
            pp();
        }
        for (x = 0; x < 4; ++x) {
            sum = s(x, x + 4, x + 8, x + 12);
            pp();
        }
        sum = s(0, 5, 10, 15);
        pp();
        sum = s(3, 6, 9, 12);
        pp();
        printf("Case #%d: ", t + 1);
        if (win) {
            printf("%c won\n", (turns % 2) ^ (win - 1) ? 'X' : 'O');
        } else if (turns == 16) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }
    }
}
