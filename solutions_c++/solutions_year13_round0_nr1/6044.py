#include <cstdio>
#include <cstring>

char mat[0x10][0x10];

int check() {
    bool allX, allO;

    for (int i = 0; i < 4; ++i) {
        allX = true; allO = true;
        for (int j = 0; j < 4; ++j) {
            if (mat[i][j] != 'X' && mat[i][j] != 'T') allX = false;
            if (mat[i][j] != 'O' && mat[i][j] != 'T') allO = false;
        }
        if (allX) return -1;
        if (allO) return 1;
    }

    for (int j = 0; j < 4; ++j) {
        allX = true; allO = true;
        for (int i = 0; i < 4; ++i) {
            if (mat[i][j] != 'X' && mat[i][j] != 'T') allX = false;
            if (mat[i][j] != 'O' && mat[i][j] != 'T') allO = false;
        }
        if (allX) return -1;
        if (allO) return 1;
    }

    allX = true; allO = true;
    for (int i = 0; i < 4; ++i) {
        if (mat[i][i] != 'X' && mat[i][i] != 'T') allX = false;
        if (mat[i][i] != 'O' && mat[i][i] != 'T') allO = false;
    }
    if (allX) return -1;
    if (allO) return 1;

    allX = true; allO = true;
    for (int i = 0; i < 4; ++i) {
        if (mat[i][3 - i] != 'X' && mat[i][3 - i] != 'T') allX = false;
        if (mat[i][3 - i] != 'O' && mat[i][3 - i] != 'T') allO = false;
    }
    if (allX) return -1;
    if (allO) return 1;

    return 0;
}

int chance() {
    int ret, ret2 = 0;

    for (int i = 0; i < 4; ++i) {
        ret = 3;
        for (int j = 0; j < 4; ++j) {
            if (mat[i][j] == 'X') ret &= 2;
            if (mat[i][j] == 'O') ret &= 1;
        }
        ret2 |= ret;
    }

    for (int j = 0; j < 4; ++j) {
        ret = 3;
        for (int i = 0; i < 4; ++i) {
            if (mat[i][j] == 'X') ret &= 2;
            if (mat[i][j] == 'O') ret &= 1;
        }
        ret2 |= ret;
    }

    ret = 3;
    for (int i = 0; i < 4; ++i) {
        if (mat[i][i] == 'X') ret &= 2;
        if (mat[i][i] == 'O') ret &= 1;
    }
    ret2 |= ret;

    ret = 3;
    for (int i = 0; i < 4; ++i) {
        if (mat[i][3 - i] == 'X') ret &= 2;
        if (mat[i][3 - i] == 'O') ret &= 1;
    }
    ret2 |= ret;

    return ret2;
}

int main() {
    int t;

    freopen("a.in", "r", stdin);
    freopen("out", "w", stdout);

    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++cas) {
        for (int i = 0; i < 4; ++i) {
            scanf("%s", mat[i]);
        }
        int ret = check(), ret2 = chance();
        if (ret < 0) printf("Case #%d: X won\n", cas);
        else if (ret > 0) printf("Case #%d: O won\n", cas);
        else {
            if (ret2 == 0) printf("Case #%d: Draw\n", cas);
            else if (ret2 == 1) printf("Case #%d: O won\n", cas);
            else if (ret2 == 2) printf("Case #%d: X won\n", cas);
            else printf("Case #%d: Game has not completed\n", cas);
        }
    }

    return 0;
}
