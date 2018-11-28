#include <cstdio>
#include <string.h>

char board[6][6];

char check(int sr, int sc, int dr, int dc)
{
    static char chars[] = {'X', 'O'};
    bool ok;
    for (int i = 0; i < 2; ++i) {
        ok = true;
        for (int j = 0; j < 4; ++j) {
            ok &= (board[sr+dr*j][sc+dc*j] == 'T' || board[sr+dr*j][sc+dc*j] == chars[i]);
        }
        if (ok)
            return chars[i];
    }
    return 0;
}

void foo(int tst)
{
    memset((void*) board, 0, 36);
    for (int i = 0; i < 4; ++i) {
        fgets(board[i], 6, stdin);
    }
    scanf("%*c");

    char res;
    for (int i = 0; i < 4; ++i) {
        if ((res = check(i, 0, 0, 1)) > 0) {
            printf("Case #%d: %c won\n", tst, res);
            return;
        }
        if ((res = check(0, i, 1, 0)) > 0) {
            printf("Case #%d: %c won\n", tst, res);
            return;
        }
    }

    if ((res = check(0, 3, 1, -1)) > 0) {
        printf("Case #%d: %c won\n", tst, res);
        return;
    }

    if ((res = check(0, 0, 1, 1)) > 0) {
        printf("Case #%d: %c won\n", tst, res);
        return;
    }

    for (int sx = 0; sx < 4; ++sx)
        for (int sy = 0; sy < 4; ++sy)
            if (board[sx][sy] == '.') {
                printf("Case #%d: Game has not completed\n", tst);
                return;
            }

    printf("Case #%d: Draw\n", tst);

}

int main()
{
    int tst;
    scanf("%d%*c", &tst);
    for (int i = 0; i < tst; ++i)
        foo(i + 1);
}
