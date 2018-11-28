#include <cstdio>

using namespace std;

typedef char board[4][8];

bool wins(board a, char sym) {
    for (int i = 0; i < 4; ++i) {
        bool good = true;
        for (int j = 0; good && j < 4; ++j) good = a[i][j] == sym || a[i][j] == 'T';
        if (good) return true;
    }

    for (int j = 0; j < 4; ++j) {
        bool good = true;
        for (int i = 0; good && i < 4; ++i) good = a[i][j] == sym || a[i][j] == 'T';
        if (good) return true;
    }

    bool good = true;
    for (int i = 0; good && i < 4; ++i) good = a[i][i] == sym || a[i][i] == 'T';
    if (good) return true;

    good = true;
    for (int i = 0; good && i < 4; ++i) good = a[3 - i][i] == sym || a[3 - i][i] == 'T';
    if (good) return true;

    return false;
}

bool complete(board a) {
    for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) if (a[i][j] == '.') return false;
    return true;
}

bool check(board a) {
    int t = 0;

    for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) {
        if (a[i][j] != '.' && a[i][j] != 'T' && a[i][j] != 'X' && a[i][j] != 'O') return false;
        if (a[i][j] == 'T') ++t;
    }

    return t <= 1 && !(wins(a, 'X') && wins(a, 'O'));
}

int main() {
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; ++t) {
        board a;
        for (int i = 0; i < 4; ++i) scanf("%s", a[i]);

        if (!check(a)) printf("*");
        printf("Case #%d: ", t);
        if (wins(a, 'X')) printf("X won\n");
        else if (wins(a, 'O')) printf("O won\n");
        else if (complete(a)) printf("Draw\n");
        else printf("Game has not completed\n");
    }

    return 0;
}
