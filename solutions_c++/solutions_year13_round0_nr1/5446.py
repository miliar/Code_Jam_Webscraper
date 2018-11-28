#include <cstdio>

char map[30][30];
char tab[30];

char check(char *chars) {
    int xc = 0, yc = 0, tc = 0;
    for (int i = 0; i < 4; i++) {
        if (chars[i] == 'X') xc++;
        else if (chars[i] == 'O') yc++;
        else if (chars[i] == 'T') tc++;
    }
    if (xc == 4 || (xc == 3 && tc == 1)) return 'X';
    if (yc == 4 || (yc == 3 && tc == 1)) return 'O';
    return 0;
}

void test() {
    for (int i = 0; i < 4; i++) scanf(" %s ", map[i]);
    char res = 0;
    for (int i = 0; i < 4 && res == 0; i++) {
        res = check(map[i]);
    }
    for (int i = 0; i < 4 && res == 0; i++) {
        tab[0] = map[0][i]; tab[1] = map[1][i]; tab[2] = map[2][i]; tab[3] = map[3][i];
        res = check(tab);
    }
    if (res == 0) {
        tab[0] = map[0][0]; tab[1] = map[1][1]; tab[2] = map[2][2]; tab[3] = map[3][3];
        res = check(tab);
    }
    if (res == 0) {
        tab[0] = map[0][3]; tab[1] = map[1][2]; tab[2] = map[2][1]; tab[3] = map[3][0];
        res = check(tab);
    }
    if (res == 'X') {
        puts("X won");
    } else if (res == 'O') {
        puts("O won");
    } else {
        int dc = 0;
        for (int i = 0; i < 4; i++) for (int j = 0; j < 4; j++) if (map[i][j] == '.') dc++;
        puts(dc > 0 ? "Game has not completed" : "Draw");
    }
}

int main() {
    int t; scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i+1);
        test();
    }
    return 0;
}