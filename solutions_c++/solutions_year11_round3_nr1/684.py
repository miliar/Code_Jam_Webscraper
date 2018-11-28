#include <cstdio>

int main () {
    int T, R, C;
    char row[100], result[100][100];
    bool okay;
    
    scanf ("%d", &T);
    for (int t = 1; t <= T; ++t) {
        printf ("Case #%d:\n", t);
        scanf ("%d %d", &R, &C);
        okay = true;
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                result[r][c] = '.';
            }
        }
        for (int r = 0; r < R; ++r) {
            scanf ("%s", row);
            if (!okay) {
                continue;
            }
            for (int c = 0; c < C; ++c) {
                if (row[c] == '.') {
                    if (result[r][c] != '.') {
                        okay = false;
                        break;
                    }
                } else {
                    if (result[r][c] == '.') {
                        if (c == C - 1 || r == R - 1) {
                            okay = false;
                            break;
                        } else {
                            result[r][c] = 0;
                            result[r][c + 1] = 1;
                            result[r + 1][c] = 3;
                            result[r + 1][c + 1] = 2;
                        }
                    }
                }
            }
        }
        if (okay) {
            for (int r = 0; r < R; ++r) {
                for (int c = 0; c < C; ++c) {
                    if (result[r][c] == '.') {
                        printf ("%c", result[r][c]);
                    } else {
                        printf ("%c", (result[r][c] % 2 == 0) ? '/' : '\\');
                    }
                }
                puts ("");
            }
        } else {
            puts ("Impossible");
        }
    }
    return 0;
}
