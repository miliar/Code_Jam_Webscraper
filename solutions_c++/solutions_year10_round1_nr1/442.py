#include <cstdio>

int T, N, K;
char map[100][100];
int isB, isR;

void rotate() {
    int i, j, k, c;
    for (i = 0; i < N; i++) {
        for (j = N - 1; j >= 0; j--) {
            c = N + 1;
            while (map[i][j] == '.' && c > 0) {
                for (k = j; k > 0; k--) map[i][k] = map[i][k - 1];
                map[i][0] = '.';
                c--;
            }
        }
    }
}

void check(char x) {
    int i, j, count;
    for (i = 0; i < N; i++) {
        count = 0;
        for (j = 0; j < N; j++) {
            if (map[i][j] == x) count++;
            else count = 0;
            if (count >= K) {
                if (x == 'B') isB = 1;
                else isR = 1;
                return;
            }
        }
    }
    for (j = 0; j < N; j++) {
        count = 0;
        for (i = 0; i < N; i++) {
            if (map[i][j] == x) count++;
            else count = 0;
            if (count >= K) {
                if (x == 'B') isB = 1;
                else isR = 1;
                return;
            }
        }
    }
    for (i = 0; i < N; i++) {
        count = 0;
        for (j = 0; j < N; j++) {
            if (i + j >= N) break;
            if (map[i + j][j] == x) count++;
            else count = 0;
            if (count >= K) {
                if (x == 'B') isB = 1;
                else isR = 1;
                return;
            }
        }
    }
    for (j = 0; j < N; j++) {
        count = 0;
        for (i = 0; i < N; i++) {
            if (i + j >= N) break;
            if (map[i][i + j] == x) count++;
            else count = 0;
            if (count >= K) {
                if (x == 'B') isB = 1;
                else isR = 1;
                return;
            }
        }
    }
    for (i = 0; i < N; i++) {
        count = 0;
        for (j = 0; j < N; j++) {
            if (i + j >= N) break;
            if (map[i + j][N - j] == x) count++;
            else count = 0;
            if (count >= K) {
                if (x == 'B') isB = 1;
                else isR = 1;
                return;
            }
        }
    }
    for (j = 0; j < N; j++) {
        count = 0;
        for (i = 0; i < N; i++) {
            if (j - i < 0) break;
            if (map[i][j - i] == x) count++;
            else count = 0;
            if (count >= K) {
                if (x == 'B') isB = 1;
                else isR = 1;
                return;
            }
        }
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-out.txt", "w", stdout);
    int tc;
    int i;
    scanf("%d", &T);
    for (tc = 1; tc <= T; tc++) {
        scanf("%d%d", &N, &K);
        for (i = 0; i < N; i++) scanf("%s", map[i]);
        rotate();
        isB = isR = 0;
        check('B');
        check('R');
        printf("Case #%d: ", tc);
        if (isB && isR) printf("Both\n");
        else if (isB) printf("Blue\n");
        else if (isR) printf("Red\n");
        else printf("Neither\n");
    }
    return 0;
}
