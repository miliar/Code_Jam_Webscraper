#include <cstdio>

char buf[4][4];
char msg[4][64] = {"X won", "O won", "Draw", "Game has not completed"};

int status()
{
    int cntx = 0;
    int cnto = 0;
    int cntt = 0;
    int empty = 0;
    /* horizontal */
    for (int i = 0; i < 4; ++i) {
        cntx = cnto = cntt = 0;
        for (int j = 0; j < 4; ++j) {
            if (buf[i][j] == 'X') {
                ++cntx;
            } else if (buf[i][j] == 'O') {
                ++cnto;
            } else if (buf[i][j] == 'T') {
                ++cntt;
            } else {
                ++empty;
            }
        }
        if (cntx + cntt == 4) {
            return 0;
        }
        if (cnto + cntt == 4) {
            return 1;
        }
    }

    /* vertical */
    for (int i = 0; i < 4; ++i) {
        cntx = cnto = cntt = 0;
        for (int j = 0; j < 4; ++j) {
            if (buf[j][i] == 'X') {
                ++cntx;
            } else if (buf[j][i] == 'O') {
                ++cnto;
            } else if (buf[j][i] == 'T') {
                ++cntt;
            } else {
                ++empty;
            }
        }
        if (cntx + cntt == 4) {
            return 0;
        }
        if (cnto + cntt == 4) {
            return 1;
        }
    }

    cntx = cnto = cntt = 0;
    for (int i = 0; i < 4; ++i) {
        if (buf[i][i] == 'X') {
            ++cntx;
        } else if (buf[i][i] == 'O') {
            ++cnto;
        } else if (buf[i][i] == 'T') {
            ++cntt;
        } else {
            ++empty;
        }
    }
    if (cntx + cntt == 4) {
        return 0;
    }
    if (cnto + cntt == 4) {
        return 1;
    }

    cntx = cnto = cntt = 0;
    for (int i = 0; i < 4; ++i) {
        if (buf[i][3 - i] == 'X') {
            ++cntx;
        } else if (buf[i][3 - i] == 'O') {
            ++cnto;
        } else if (buf[i][3 - i] == 'T') {
            ++cntt;
        } else {
            ++empty;
        }
    }
    if (cntx + cntt == 4) {
        return 0;
    }
    if (cnto + cntt == 4) {
        return 1;
    }
    
    if (!empty) {
        return 2;
    } else {
        return 3;
    }
}

int main()
{
    int testnum;
    FILE * fd = fopen("input", "r");

    fscanf(fd, "%d ", &testnum);
    for (int test = 1; test <= testnum; ++test) {
        /* input */
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                fscanf(fd, " %c ", &buf[i][j]);
            }
        }

        /* compute status */
        int rv = status();
        printf("Case #%d: %s\n", test, msg[rv]);
    }

    fclose(fd);
}

