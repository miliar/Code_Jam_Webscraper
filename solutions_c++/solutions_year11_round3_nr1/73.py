#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)
#define sz(v) (int) ((v).size())

int R, C;
char field[100][100];

int main()
{
//    freopen("../DefaultProject/1.txt", "r", stdin);
    freopen("../DefaultProject/A-large.in", "r", stdin);
    freopen("../DefaultProject/A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    rep(tc, T)
    {
        printf("Case #%d:\n", tc + 1);

        scanf("%d%d", &R, &C);
        gets(field[0]);
        rep(i, R)
        {
            gets(field[i]);
        }

        for (;;)
        {
            bool wasSet = false;
            for (int i = 0; i < R - 1; i++)
            {
                for (int j = 0; j < C - 1; j++)
                {
                    if (field[i][j] == '#' && field[i + 1][j] == '#' && field[i][j + 1] == '#' && field[i + 1][j + 1] == '#')
                    {
                        field[i][j] = '/';
                        field[i + 1][j + 1] = '/';
                        field[i][j + 1] = '\\';
                        field[i + 1][j] = '\\';
                        wasSet = true;
                    }
                }
            }
            if (!wasSet)
                break;
        }

        bool can = true;
        rep(i, R)
        {
            rep(j, C)
            {
                if (field[i][j] == '#')
                {
                    can = false;
                    break;
                }
            }
            if (!can)
                break;
        }
        if (!can)
            puts("Impossible");
        else
        {
            rep(i, R)
            {
                rep(j, C)
                {
                    putchar(field[i][j]);
                }
                putchar('\n');
            }
        }
    }

    return 0;
}
