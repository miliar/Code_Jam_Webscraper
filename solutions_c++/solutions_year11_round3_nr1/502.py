#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char map[100][100];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    int cases = 1;

    scanf("%d", &T);

    int R, C;
    int flag;

    while (T-- > 0)
    {
        scanf("%d %d", &R, &C);

        for (int i = 0; i < R; i++)
        {
            scanf("%s\n", map[i]);
//            printf("%s\n", map[i]);
        }

        int countB = 0;

        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                if (map[i][j] == '#')
                {
                    countB++;
                }
            }
        }
        flag = 1;
        if (countB % 4 != 0)
        {
            flag = 0;
        }

        for (int i = 0; i < R - 1; i++)
        {
            for (int j = 0; j < C - 1; j++)
            {
                if (map[i][j] == '#')
                {
                    if (map[i][j + 1] == '#' && map[i + 1][j] == '#' && map[i + 1][j + 1] == '#')
                    {
                        map[i][j] = '/';
                        map[i][j + 1] = '\\';
                        map[i + 1][j] = '\\';
                        map[i + 1][j + 1] = '/';
                    }
                    else
                    {
                        flag = 0;
                        goto end;
                    }
                }
            }
        }
end:
        printf("Case #%d:\n", cases++);
        if (flag == 0)
        {
            printf("Impossible\n");
        }
        else
        {
            for (int i = 0; i < R; i++)
            {
                printf("%s\n", map[i]);
            }
        }
    }

    return 0;
}
