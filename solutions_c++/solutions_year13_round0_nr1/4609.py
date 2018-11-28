#include <cstdio>

char board[5][5];

void load() {
    for (int i = 0; i < 4; ++i) {
        scanf("%s", board[i]);
    }
}

// 0 if nothing
// -1 if X
// 1 if O
int check(int x, int y, int dx, int dy) {
    int onot = 0, xnot = 0;

    for (int i = 0; i < 4; ++i, x += dx, y += dy) {
        if (board[x][y] == '.') return 0;
        if (board[x][y] == 'T') continue;
        if (board[x][y] == 'X') onot = 1;
        if (board[x][y] == 'O') xnot = 1;
    }

    if (xnot == 1 && onot == 1) return 0;
    if (xnot == 1) return 1;
    if (onot == 1) return -1;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int tt = 1; tt <= T; ++tt) {
        load();
        int over = 1;
        int sum = 0;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (board[i][j] == '.') over = 0;
            }
            sum += check(i, 0, 0, 1);
            sum += check(0, i, 1, 0);
        }
        sum += check(0, 0, 1, 1);
        sum += check(3, 0, -1, 1);

        if (sum > 0) printf("Case #%d: O won\n", tt);
        if (sum < 0) printf("Case #%d: X won\n", tt);
        if (sum == 0) {
            if (over == 0) printf("Case #%d: Game has not completed\n", tt);
            else printf("Case #%d: Draw\n", tt);
        }
    }
    return 0;
}
