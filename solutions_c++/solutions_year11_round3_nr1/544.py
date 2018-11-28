#include <stdio.h>
#include <string.h>

int R, C;

int x[50][50];
int blue;

int dfs(int a, int b) {
    if (a == R - 1 || b == C - 1) return 0;
    if (x[a][b] == '#' && x[a + 1][b + 1] == '#' && x[a + 1][b] == '#' && x[a][b + 1] == '#') {
        x[a][b] = '/';
        x[a][b + 1] = '\\';
        x[a + 1][b] = '\\';
        x[a + 1][b + 1] = '/';
        blue -= 4;
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                    dfs(i, j);
                    if (blue == 0) {
                        return 0;
                    }
            }
        }
        x[a][b] = '#';
        x[a][b + 1] = '#';
        x[a + 1][b] = '#';
        x[a + 1][b + 1] = '#';

        blue += 4;
    }
    return 0;
}

void output() {
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j) {
            printf("%c", x[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int num = 1; num <= T; ++num) {
        scanf("%d", &R);
        scanf("%d", &C);
        memset(x, 0, sizeof(x));
        blue = 0;
        for (int i = 0; i < R; ++i) {
            char tmp[60];
            scanf("%s", tmp);
            for (int j = 0; j < C; ++j) {
                if (tmp[j] == '#') {
                    x[i][j] = '#';
                    ++blue;
                } else {
                    x[i][j] = '.';
                }
            }
        }
        if (blue % 4 != 0) {
            printf("Case #%d:\nImpossible\n", num);
            continue;
        }
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j) {
                dfs(i, j);
                if (blue == 0) {
                    printf("Case #%d:\n", num);
                    output();
                    i = R;
                    j = C;
                }
            }
        if (blue > 0) {
            printf("Case #%d:\nImpossible\n", num);
        }
    }
    return 0;
}
