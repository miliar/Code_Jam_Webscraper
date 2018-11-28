#include <cstdio>

using namespace std;

char map[4][4];

int main() {
    int N;
    scanf("%d", &N);

    for (int k = 0; k < N; k++) {
        bool hasDot = false, noAns = true;
        for (int i = 0; i < 4; i++) {
            scanf("%s", map[i]);
            for (int j = 0; j < 4; j++) {
                if (map[i][j] == '.') {
                    hasDot = true;
                }
            }
        }

        for (int i = 0; i < 4; i++) {
            char type = map[i][0];
            if (type != '.') {
                bool fail = false;
                for (int j = 1; j < 4; j++) {
                    if (type != map[i][j] && map[i][j] != 'T') {
                        fail = true;
                        break;
                    }
                }

                if (!fail) {
                    if (type == 'O') {
                        printf("Case #%d: O won\n", k + 1);
                    } else {
                        printf("Case #%d: X won\n", k + 1);
                    }
                    noAns = false;
                }
            }
        }

        for (int i = 0; i < 4; i++) {
            char type = map[0][i];
            if (type != '.') {
                bool fail = false;
                for (int j = 1; j < 4; j++) {
                    if (type != map[j][i] && map[j][i] != 'T') {
                        fail = true;
                        break;
                    }
                }

                if (!fail) {
                    if (type == 'O') {
                        printf("Case #%d: O won\n", k + 1);
                    } else {
                        printf("Case #%d: X won\n", k + 1);
                    }
                    noAns = false;
                }
            }
        }

        bool fail = false;
        char type = map[0][0];
        if (type != '.') {
            for (int i = 1; i < 4; i++) {
                if (type != map[i][i] && map[i][i] != 'T') {
                    fail = true;
                    break;
                }
            }

            if (!fail) {
                if (type == 'O') {
                    printf("Case #%d: O won\n", k + 1);
                } else {
                    printf("Case #%d: X won\n", k + 1);
                }
                noAns = false;
            }
        }

        fail = false;
        type = map[0][3];
        if (type != '.') {
            for (int i = 1; i < 4; i++) {
                if (type != map[i][3 - i] && map[i][3 - i] != 'T') {
                    fail = true;
                    break;
                }
            }

            if (!fail) {
                if (type == 'O') {
                    printf("Case #%d: O won\n", k + 1);
                } else {
                    printf("Case #%d: X won\n", k + 1);
                }
                noAns = false;
            }
        }

        if (noAns) {
            if (hasDot) {
                printf("Case #%d: Game has not completed\n", k + 1);
            } else {
                printf("Case #%d: Draw\n", k + 1);
            }
        }
    }

    return 0;
}
