#include <cstdio>
#include <iostream>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

const int N = 4;

bool outof(int x, int y) {
    if (x < 0 || x >= N) return true;
    if (y < 0 || y >= N) return true;
    return false;
}

bool iswin(char player, char bd[][N], int x, int y, int dx, int dy) {
    int my = 0;

    while (!outof(x, y)) {
        if (bd[x][y] == player ||
            bd[x][y] == 'T') {
            my++;
        }
        x += dx;
        y += dy;
    }

    // printf("%d %c (%d %d) (%d %d)\n", my, player, x, y, dx, dy);
    return my == 4;
}

bool win(char player, char bd[][N], int x, int y) {
    bool w =
        iswin(player, bd, x, y, 0, 1) ||
        iswin(player, bd, x, y, 1, 0) ||
        iswin(player, bd, x, y, 1, 1) ||
        iswin(player, bd, x, y, -1, 1);
    return w;
}

void calc(char bd[][N]) {
    For(i, N) For(j, N) {
        if (i > 0 && j > 0) continue;

        if (win('X', bd, i, j)) {
            puts("X won");
            return;
        }

        if (win('O', bd, i, j)) {
            puts("O won");
            return;
        }
    }

    bool existsSpace = false;
    For(i, N) For(j, N) {
        if (bd[i][j] == '.') {
            existsSpace = true;
            break;
        }
    }

    if (existsSpace) {
        puts("Game has not completed");
        return;
    }

    puts("Draw");
}

void display(char bd[][N]) {
    For(i, N) {
        For(j, N) {
            printf("%c", bd[i][j]);
        }
        puts("");
    }
}
        
int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        char s[100];

        char bd[N][N];
        For(i, N) {
            scanf("%s", s);
            For(j, N) bd[i][j] = s[j];
        }

        printf("Case #%d: ", cc+1);
        // puts(""); display(bd);
        calc(bd);
    }
}
