#include <cstdio>
#include <algorithm>

using namespace std;

inline int get(void) {
    int x;
    scanf("%x", &x);
    return x;
}

const int MAXN = 50+3;

void rotate(char board[MAXN][MAXN], int n) {
    char tmp[MAXN][MAXN] = {{}};
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            tmp[i][j] = board[i][j];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            board[j][n-i-1] = tmp[i][j];
        }
    }
}

void gravity(char board[MAXN][MAXN], int n) {
    for (int i = n-1; i >=0; i--) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == '.') {
                for (int k = i-1; k >=0; k--) {
                    if (board[k][j] != '.') {
                        swap(board[k][j], board[i][j]);
                        break;
                    }
                }
            }
        }
    }
}

bool win(char board[MAXN][MAXN], int n, int k, char player) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int across = 0, down = 0, diag = 0, diag2 = 0;
            for (int h = 0; h+j < n; h++) {
                if (board[i][h+j] == player) {
                    across++;
                } else {
                    break;
                }
            }
            for (int h = 0; h+i < n; h++) {
                if (board[h+i][j] == player) {
                    down++;
                } else {
                    break;
                }
            }
            for (int h = 0; h+i < n && h+j <n; h++) {
                if (board[h+i][h+j] == player) {
                    diag++;
                } else {
                    break;
                }
            }
            for (int h = 0; h+i<n && h+j >=0; h++) {
                if (board[h+i][j-h] == player) {
                    diag2++;
                } else {
                    break;
                }
            }
            if (diag >= k || down >= k || across >= k || diag2 >=k) {
                return true;
            }
        }
    }
    return false;
}

void solve(int t) {
    int n = get();
    int k = get();
    char board[MAXN][MAXN];
    scanf("\n");
    for (int i = 0; i < n; i++) {
        fgets(board[i], MAXN, stdin);
    }
    rotate(board, n);
    gravity(board,n);

    bool r = win(board, n, k, 'R');
    bool b = win(board, n, k, 'B');

    printf("Case #%d: ", t+1);

    if (r && b) {
        printf("Both\n");
    } else if (r) {
        printf("Red\n");
    } else if (b) {
        printf("Blue\n");
    } else {
        printf("Neither\n");
    }
}

int main(void) {
    int tests;
    scanf("%d\n", &tests);
    for (int t = 0; t < tests; t++) {
        solve(t);
    }
    return 0;
}
