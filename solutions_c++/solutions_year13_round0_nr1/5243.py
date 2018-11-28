#include <iostream>
#include <cstdio>

using namespace std;

int t;
char s[10][10];

char check_row(int r)
{
    char res = '.';
    bool find = false;
    for (int i = 0; i < 4; i++)
        if (s[r][i] != 'O' && s[r][i] != 'T')
        {
            find = true;
            break;
        }

    if (!find)
    {
        res = 'O';
        return res;
    }

    find = false;
    for (int i = 0; i < 4; i++)
        if (s[r][i] != 'X' && s[r][i] != 'T')
        {
            find = true;
            break;
        }

    if (!find)
    {
        res = 'X';
        return res;
    }

    return res;
}

char check_col(int r)
{
    char res = '.';
    bool find = false;
    for (int i = 0; i < 4; i++)
        if (s[i][r] != 'O' && s[i][r] != 'T')
        {
            find = true;
            break;
        }

    if (!find)
    {
        res = 'O';
        return res;
    }

    find = false;
    for (int i = 0; i < 4; i++)
        if (s[i][r] != 'X' && s[i][r] != 'T')
        {
            find = true;
            break;
        }

    if (!find)
    {
        res = 'X';
        return res;
    }

    return res;
}

char check_diag(int n, int m)
{
    char res = '.';
    bool find = false;
    for (int i = 0; i < 4; i++)
        if (s[i][n + m * i] != 'O' && s[i][n + m * i] != 'T')
        {
            find = true;
            break;
        }

    if (!find)
    {
        res = 'O';
        return res;
    }

    find = false;
    for (int i = 0; i < 4; i++)
        if (s[i][n + m * i] != 'X' && s[i][n + m * i] != 'T')
        {
            find = true;
            break;
        }

    if (!find)
    {
        res = 'X';
        return res;
    }

    return res;
}

void Solve()
{
    char win = '.';
    for (int i = 0; i < 4; i++)
        if (check_row(i) != '.')
           win = check_row(i);

    for (int i = 0; i < 4; i++)
        if (check_col(i) != '.')
           win = check_col(i);

    if (check_diag(0, 1) != '.')
        win = check_diag(0, 1);
    if (check_diag(3, -1) != '.')
        win = check_diag(3, -1);
    if (win != '.')
        printf("%c won\n", win);
    else
    {
        bool find = false;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (s[i][j] == '.')
                {
                    find = true;
                    break;
                }
        if (!find)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
}


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d\n", &t);
    for (int j = 0; j < t; j++)
    {
        for (int i = 0; i < 4; i++)
            scanf("%s", s[i]);
        scanf("\n");
        printf("Case #%d: ", j + 1);
        Solve();
    }

    return 0;
}
