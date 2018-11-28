#include <cstdio>
#include <iostream>
using namespace std;

bool isStatus(char mp[][10], char c)
{
    bool flag = false;
    for (int i = 0; i < 4; i++)
    {
        if ((mp[i][0] == c || mp[i][0] == 'T') &&
            (mp[i][1] == c || mp[i][1] == 'T') &&
            (mp[i][2] == c || mp[i][2] == 'T') &&
            (mp[i][3] == c || mp[i][3] == 'T'))
        {
            flag = true; break;
        }
        if ((mp[0][i] == c || mp[0][i] == 'T') &&
            (mp[1][i] == c || mp[1][i] == 'T') &&
            (mp[2][i] == c || mp[2][i] == 'T') &&
            (mp[3][i] == c || mp[3][i] == 'T'))
        {
            flag = true; break;
        }
        if ((mp[0][0] == c || mp[0][0] == 'T') &&
            (mp[1][1] == c || mp[1][1] == 'T') &&
            (mp[2][2] == c || mp[2][2] == 'T') &&
            (mp[3][3] == c || mp[3][3] == 'T'))
        {
            flag = true; break;
        }
        if ((mp[0][3] == c || mp[0][3] == 'T') &&
            (mp[1][2] == c || mp[1][2] == 'T') &&
            (mp[2][1] == c || mp[2][1] == 'T') &&
            (mp[3][0] == c || mp[3][0] == 'T'))
        {
            flag = true; break;
        }
    }
    return flag;
}

int main(void)
{
   // freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, cas = 1; scanf("%d", &T);
    while (T--)
    {
        char mp[10][10];

        for (int i = 0; i < 4; i++)
        {
            scanf("%s", mp[i]);
        }

        printf("Case #%d: ", cas++);

        if (isStatus(mp, 'X') == true)
        {
            printf("X won\n");
        }
        else if (isStatus(mp, 'O') == true)
        {
            printf("O won\n");
        }
        else
        {
            bool isEnd = true;
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (mp[i][j] == '.')
                    {
                        isEnd = false;
                        break;
                    }
                }
                if (isEnd == false) break;
            }
            if (isEnd == true)
            {
                printf("Draw\n");
            }
            else
            {
                printf("Game has not completed\n");
            }
        }

    }

    return 0;
}
