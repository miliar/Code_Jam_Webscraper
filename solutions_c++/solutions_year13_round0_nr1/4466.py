#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int ca = 0; ca < T; ca++) {
        printf("Case #%d: ", ca + 1);
        bool has_empty = false;
        char board[4][4];
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                char ch;
                do {
                    ch = getchar();
                } while (ch != 'X' && ch != 'O' && ch != 'T' && ch != '.');

                board[i][j] = ch;
                if (ch == '.')
                    has_empty = true;
            }

        int fx[8][2] = {{-1, 0}, {-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}};
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                // printf("root is %d %d\n", i, j);
                for (int k = 0; k < 4; k++) {
                    int cnt[256] = {0};
                    for (int l = 0; l < 4; l++) {
                        int ni = i + l * fx[k][0];
                        int nj = j + l * fx[k][1];
                        // printf("check %d %d\n", ni, nj);
                        if (ni >= 0 && ni < 4 && nj >= 0 && nj < 4)
                            cnt[board[ni][nj]]++;
                    }

                    if (cnt['O'] + cnt['T'] == 4) {
                        printf("O won\n");
                        goto done;
                    }
                    if (cnt['X'] + cnt['T'] == 4) {
                        printf("X won\n");
                        goto done;
                    }

                }

            }

        if (has_empty)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
done:;
    }

}