#include <cstdio>
#include <cstring>
#include <cstdio>

void print_board(int N, char board[64][64]) {
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            printf("%c", board[r][c]);
        }
        printf("\n");
    }
    printf("\n");
}

const char* solve() {
    int N, K;
    scanf("%d%d", &N, &K);
    char board[64][64]; // row, column
    for (int i = 0; i < N; i++) {
        scanf("%s", board[i]);
    }

    /* Drop to right. */
    char board2[64][64];
    memset(board2, '.', sizeof(board2));
    for (int r = 0; r < N; r++) {
        int c2 = N-1;
        for (int c1 = N-1; c1 >= 0; c1--) {
            if (board[r][c1] != '.') {
                board2[r][c2--] = board[r][c1];
            }
        }
    }

    int most_conseq[2] = {0,0};
    /* Solve rows. */
    static const char pmap[2] = {'R', 'B'};
    for (int r = 0; r < N; r++) {
        int cur_conseq[2] = {0,0};
        for (int c = 0; c < N; c++) {
            for (int t = 0; t < 2; t++) {
                if (board2[r][c] == pmap[t]) {
                    cur_conseq[t]++;
                    if (cur_conseq[t] > most_conseq[t]) {
                        most_conseq[t] = cur_conseq[t];
                    }
                } else {
                    cur_conseq[t] = 0;
                }
            }
        }
    }
    /* Solve columns. */
    for (int r = 0; r < N; r++) {
        int cur_conseq[2] = {0,0};
        for (int c = 0; c < N; c++) {
            for (int t = 0; t < 2; t++) {
                if (board2[c][r] == pmap[t]) {
                    cur_conseq[t]++;
                    if (cur_conseq[t] > most_conseq[t]) {
                        most_conseq[t] = cur_conseq[t];
                    }
                } else {
                    cur_conseq[t] = 0;
                }
            }
        }
    }
    int sr = N-1;
    int sc = 0;
    while (sc < N) {
        int r = sr, c = sc;
        int cur_conseq[2] = {0,0};
        while (r < N && c < N) {
            for (int t = 0; t < 2; t++) {
                if (board2[c][r] == pmap[t]) {
                    cur_conseq[t]++;
                    if (cur_conseq[t] > most_conseq[t]) {
                        most_conseq[t] = cur_conseq[t];
                    }
                } else {
                    cur_conseq[t] = 0;
                }
            }
            r++;
            c++;
        }
        if (sr == 0) {
            sc++;
        } else {
            sr--;
            c = 0;
        }
    }
    sr = 0;
    sc = 0;
    while (sr < N) {
        int r = sr, c = sc;
        int cur_conseq[2] = {0,0};
        while (r < N && c >= 0) {
            for (int t = 0; t < 2; t++) {
                if (board2[c][r] == pmap[t]) {
                    cur_conseq[t]++;
                    if (cur_conseq[t] > most_conseq[t]) {
                        most_conseq[t] = cur_conseq[t];
                    }
                } else {
                    cur_conseq[t] = 0;
                }
            }
            r++;
            c--;
        }
        if (sc == N-1) {
            sr++;
        } else {
            sc++;
            r = 0;
        }
    }

    bool rWins = most_conseq[0] >= K;
    bool bWins = most_conseq[1] >= K;
    if (bWins && rWins) {
        return "Both";
    } else if (bWins) {
        return "Blue";
    } else if (rWins) {
        return "Red";
    } else {
        return "Neither";
    }

#if 0
    printf("Board:\n");
    print_board(N, board);
    printf("Rotated:\n");
    print_board(N, board2);
#endif
}

int main() {
    int T;

    scanf("%d", &T);
    for (int i = 0; i < T; i++) {
        printf("Case #%d: %s\n", i+1, solve());
    }
}
