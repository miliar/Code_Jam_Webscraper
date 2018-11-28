#include <cstdio>

char a[5][5];

inline bool check(char x) {
    for (int i = 0; i < 4; ++i) {
        bool f = true;
        for (int j = 0; j < 4; ++j)
            if (a[i][j] != 'T' && a[i][j] != x)
                f = false;
        if (f) {
            printf("%c won\n", x);
            return true;
        }
    }
    for (int j = 0; j < 4; ++j) {
        bool f = true;
        for (int i = 0; i < 4; ++i)
            if (a[i][j] != 'T' && a[i][j] != x)
                f = false;
        if (f) {
            printf("%c won\n", x);
            return true;
        }
    }
    bool f = true;
    for (int i = 0; i < 4; ++i)
        if (a[i][i] != 'T' && a[i][i] != x)
            f = false;
    if (f) {
        printf("%c won\n", x);
        return true;
    }
    f = true;
    for (int i = 0; i < 4; ++i)
        if (a[i][3 - i] != 'T' && a[i][3 - i] != x)
            f = false;
    if (f) {
        printf("%c won\n", x);
        return true;
    }
    return false;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        printf("Case #%d: ", cs);
        for (int i = 0; i < 4; ++i)
            scanf("%s", a[i]);
        if (!check('O') && !check('X')) {
            bool f = false;
            for (int i = 0; i < 4; ++i)
                for (int j = 0; j < 4; ++j)
                    if (a[i][j] == '.')
                        f = true;
            puts(f ? "Game has not completed" : "Draw");
        }
    }
    return 0;
}
