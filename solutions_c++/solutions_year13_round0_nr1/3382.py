#include <cstdio>
#include <cstring>

int mat[4][4], cnt[4][4][4][2];
const int CODE_O = 0;
const int CODE_X = 1;
const int CODE_T = 2;
const int CODE_EMPTY = -1;
const int O_WIN = 0;
const int X_WIN = 1;
const int NOBODY_WIN = -1;
const int DRAW = -2;

const int dir[4][2] = {{0, -1}, {-1, 0}, {-1, -1}, {-1, 1}};

void work() {
    static char str[10];
    for (int i = 0; i < 4; i++)
    {
        scanf("%s", str);
        for (int j = 0; j < 4; j++)
            switch (str[j])
            {
                case 'X' : mat[i][j] = CODE_X; break;
                case 'O' : mat[i][j] = CODE_O; break;
                case 'T' : mat[i][j] = CODE_T; break;
                case '.' : mat[i][j] = CODE_EMPTY; break;
            }
    }

    int stat = DRAW;

    for (int d = 0; d < 3; d++)
        for (int c = 0; c < 2; c++)
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                {
                    int px = i + dir[d][0], py = j + dir[d][1];
                    if (mat[i][j] == c || mat[i][j] == CODE_T)
                    {
                        if (0 <= px && px < 4 && 0 <= py && py < 4)
                            cnt[d][i][j][c] = cnt[d][px][py][c] + 1;
                        else
                            cnt[d][i][j][c] = 1;
                    }
                    else cnt[d][i][j][c] = 0;
                    if (cnt[d][i][j][c] >= 4) stat = c;
                }

    for (int c = 0; c < 2; c++)
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
            {
                int px = i + dir[3][0], py = j + dir[3][1];
                if (mat[i][j] == c || mat[i][j] == CODE_T)
                {
                    if (0 <= px && px < 4 && 0 <= py && py < 4)
                        cnt[3][i][j][c] = cnt[3][px][py][c] + 1;
                    else
                        cnt[3][i][j][c] = 1;
                }
                else cnt[3][i][j][c] = 0;
                if (cnt[3][i][j][c] >= 4) stat = c;
            }
    if (stat == DRAW)
    {
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (mat[i][j] == CODE_EMPTY)
                    stat = NOBODY_WIN;
    }
    switch (stat)
    {
        case O_WIN: puts("O won"); break;
        case X_WIN: puts("X won"); break;
        case NOBODY_WIN: puts("Game has not completed"); break;
        case DRAW: puts("Draw");
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        work();
    }
    return 0;
}
