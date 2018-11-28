#include <cstdio>
#include <cstring>

char board[60][60];
char dboard[60][60];
int N, K;

void drop() {
    int i, j, k;
    for (i = 0; i < N; i++) {
        for (j = N - 1; j >= 0; j--) {
            if (board[i][j] != '.')
                continue;
            for (k = j - 1; k >= 0; k--) {
                if (board[i][k] != '.') {
                    board[i][j] = board[i][k];
                    board[i][k] = '.';
                    break;
                }
            }
        }
    }
}

const int dx[] = {0, 1, 1, 1};
const int dy[] = {1, 0, -1, 1};

bool scan(char ch) {
    bool flag = false;
    int i, j, k, l, ni, nj;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            if (board[i][j] != ch)
                continue;
            for (k = 0; k < 4; k++) {
                flag = true;
                for (l = 1; l < K; l++) {
                    ni = i + l * dx[k];
                    nj = j + l * dy[k];
                    if (nj < 0 || nj >= N || ni >= N || board[ni][nj] != ch) {
                        flag = false;
                        break;
                    }
                }
                if (flag)
                    return flag;
            }
        }
    }
    return flag;
}

void print() {
    for (int i = 0; i < N; i++) {
        printf("%s", board[i]);
    }
}

const char* result[] = { "Neither", "Red", "Blue", "Both" };

int t, T, i, fr, fb;

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        scanf("%d%d ", &N, &K);
        memset(board, '.', sizeof(board));
        for (i = 0; i < N; i++)
            fgets(board[i], sizeof(board[i]), stdin);
        drop();
        //print();
        fr = scan('R');
        fb = scan('B');
        printf("Case #%d: %s\n", t, result[fb << 1 | fr]);
    }
}

