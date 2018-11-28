#include <cstdio>

using namespace std;

int T;
char board[4][4];

inline char &helper(int t, int i, int j)
{
    if (t == 0)
        return board[j][i];
    if (t == 1)
        return board[i][j];
    if (t == 2)
        return board[i][i];
    return board[3-i][i];
}

bool hasdot()
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (board[i][j] == '.')
                return true;
    return false;
}

char check(int t, int k)
{
    char s = 'T';
    for (int i = 0; i < 4; ++i)
    {
        if (helper(t, i, k) == '.')
            return 0;
        if (helper(t, i, k) != s)
        {
            if (s == 'T')
                s = helper(t, i, k);
            else if (helper(t, i, k) != 'T')
                return 0;
        }
    }
    return s;
}

char compute()
{
    char ret = '\0';
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < 4; ++j)
            if (ret = check(i, j))
                return ret;
    for (int i = 2; i < 4; ++i)
        if (ret = check(i, 0))
            return ret;
    if (hasdot())
        ret = 'T';
    return ret;
}

void printer(int i, char s)
{
    switch (s)
    {
    case 'X':
        printf("Case #%d: X won\n", i);
        break;
    case 'O':
        printf("Case #%d: O won\n", i);
        break;
    case 'T':
        printf("Case #%d: Game has not completed\n", i);
        break;
    case '\0':
        printf("Case #%d: Draw\n", i);
        break;
    }
}

int main()
{
    freopen("a.txt", "r", stdin);
    freopen("a-out.txt", "w", stdout);

    scanf("%d", &T);
    for (int CS = 1; CS <= T; ++CS)
    {
        gets(board[0]); // get rid of newline
        for (int i = 0; i < 4; ++i)
            gets(board[i]);
        char s = compute();
        printer(CS, s);
    }
    return 0;
}
