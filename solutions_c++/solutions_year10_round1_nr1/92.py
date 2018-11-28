#include <stdio.h>
#include <string.h>

char tmp[1000];
char map[100][100];
int color[100][100], cnt[100][100][3];
int n, K;

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        printf("Case #%d: ", T);
        memset(map, 0, sizeof(map));
        scanf("%d%d", &n, &K);
        gets(tmp);
        for (int i = 0; i < n; i++) {
            gets(tmp);
            for (int j = 0; j < n; j++) {
                map[j][n - i - 1] = tmp[j];
            }
        }
        for (int j = 0; j < n; j++) {
            int row;
            for (int i = n - 1, row = n - 1; i >= 0; i--) {
                while (row >= 0 && map[row][j] != '.') {
                    row--;
                }
                if (map[i][j] != '.' && i < row) {
                    map[row][j] = map[i][j];
                    map[i][j] = '.';
                }
            }
        }
        bool blue = false, red = false;
        memset(color, -1, sizeof(color));
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] != '.') {
                    color[i][j] = map[i][j] == 'R';
                    cnt[i][j][0] = cnt[i][j][1] = cnt[i][j][2] = 1;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            int colorL = -1, num = 0;
            for (int j = 0; j < n; j++) {
                if (map[i][j] == '.') {
                    colorL = -1;
                    num = 0;
                } else {
                    if (color[i][j] == colorL) {
                        num++;
                    } else {
                        colorL = color[i][j];
                        num = 1;
                    }
                }
                if (colorL == 0 && num >= K) {
                    blue = true;
                }
                if (colorL == 1 && num >= K) {
                    red = true;
                }
            }
            if (i < n - 1) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < 3; k++) {
                        int x = i + 1, y = j + k - 1;
                        if (y >= 0 && y < n) {
                            if (map[x][y] != '.') {
                                if (color[i][j] == color[x][y]) {
                                    cnt[x][y][k] = cnt[i][j][k] + 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < 3; k++) {
                    if (cnt[i][j][k] >= K) {
                        if (color[i][j] == 0) {
                            blue = true;
                        } else {
                            red = true;
                        }
                    }
                }
            }
        }
        if (blue) {
            if (red) {
                puts("Both");
            } else {
                puts("Blue");
            }
        } else {
            if (red) {
                puts("Red");
            } else {
                puts("Neither");
            }
        }
    }
    return 0;
}
