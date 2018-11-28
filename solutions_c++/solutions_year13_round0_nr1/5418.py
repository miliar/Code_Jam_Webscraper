#include <cstdio>

const int N = 1000 + 1;

char board[N][N];
int n;

bool check(char token, int &number) {
    bool result = false;
    for (int i = 0; i < 4; ++ i) {
        for (int j = 0; j < 4; ++ j) {
            number += board[i][j] == token || board[i][j] == 'T';
        }
    }
    for (int i = 0; i < 4; ++ i) {
        int temp = 0;
        for (int j = 0; j < 4; ++ j) {
            temp += board[i][j] == token || board[i][j] == 'T';
        }
        if (temp == 4) {
            return true;
        }
        temp = 0;
        for (int j = 0; j < 4; ++ j) {
            temp += board[j][i] == token || board[i][j] == 'T';
        }
        if (temp == 4) {
            return true;
        }
    }
    int temp = 0;
    for (int i = 0; i < 4; ++ i) {
        temp += board[i][i] == token || board[i][i] == 'T';
    }
    if (temp == 4) {
        return true;
    }
    temp = 0;
    for (int i = 0; i < 4; ++ i) {
        temp += board[i][3 - i] == token || board[i][3 - i] == 'T';
    }
    return temp == 4;
}

int main() {
    freopen("input", "r", stdin);
    int test_count;
    scanf("%d", &test_count);
    for (int t = 1; t <= test_count; ++ t) {
        for (int i = 0; i < 4; ++ i) {
            scanf("%s", board[i]);
        }
        int number[2] = {0};
        bool win[2] = {0};
        win[0] = check('O', number[0]);
        win[1] = check('X', number[1]);
        printf("Case #%d: ", t);
        if (win[0]) {
            puts("O won");
        } else if (win[1]) {
            puts("X won");
        } else if (number[0] + number[1] >= 16) {
            puts("Draw");
        } else {
            puts("Game has not completed");
        }
    }
    return 0;
}
