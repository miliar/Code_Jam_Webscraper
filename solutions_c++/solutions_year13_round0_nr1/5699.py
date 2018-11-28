#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
const int N = 100005;
char s[4][5];
int check ()
{
    for (int i = 0; i < 4; i ++)
    {
        if (s[i][0] == 'X' && s[i][1] == 'X' && s[i][2] == 'X'
            && s[i][3] == 'X')
        {
            puts("X won");
            return 1;
        }

        if (s[i][0] == 'O' && s[i][1] == 'O' && s[i][2] == 'O'
            && s[i][3] == 'O')
        {
            puts("O won");
            return 1;
        }

        if (s[0][i] == 'X' && s[1][i] == 'X' && s[2][i] == 'X'
            && s[3][i] == 'X')
        {
            puts("X won");
            return 1;
        }

        if (s[0][i] == 'O' && s[1][i] == 'O' && s[2][i] == 'O'
            && s[3][i] == 'O')
        {
            puts("O won");
            return 1;
        }
    }

    if (s[0][0] == 'X' && s[1][1] == 'X' && s[2][2] == 'X'
            && s[3][3] == 'X')
    {
            puts("X won");
            return 1;
    }

    if (s[0][0] == 'O' && s[1][1] == 'O' && s[2][2] == 'O'
            && s[3][3] == 'O')
    {
        puts("O won");
        return 1;
    }


    if (s[3][0] == 'X' && s[2][1] == 'X' && s[1][2] == 'X'
            && s[0][3] == 'X')
    {
        puts("X won");
        return 1;
    }


    if (s[3][0] == 'O' && s[2][1] == 'O' && s[1][2] == 'O'
            && s[0][3] == 'O')
    {
        puts("O won");
        return 1;
    }
    return 0;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas ++)
    {
        int x, y;
        bool empty = 0;
        for (int i = 0; i < 4; i ++)
        {
            scanf("%s", s[i]);
            for (int j = 0; j < 4; j ++)
            {
                 if (s[i][j] == 'T')
                    x = i, y = j;

                if (s[i][j] == '.')
                    empty = 1;
            }


        }

        printf("Case #%d: ", cas);

        s[x][y] = 'X';
        if (!check ())
        {
            s[x][y] = 'O';
            if (!check())
                puts(empty ? "Game has not completed" : "Draw");
        }
    }
}
