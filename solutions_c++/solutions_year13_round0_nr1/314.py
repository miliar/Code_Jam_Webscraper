// vim:set ts=8 sw=4 et smarttab:
// Qualification Round 2013

#include <cstdio>
#include <cstring>
#include <cassert>

char board[4][5];

bool row(int i, char &ch)
{
    ch = 'T';
    for (int j = 0; j < 4; ++j)
    {
        if (board[i][j] == '.')
            return false;
        if (board[i][j] == 'T')
            continue;
        ch = board[i][j];
        break;
    }

    for (int j = 0; j < 4; ++j)
        if (board[i][j] != 'T' && board[i][j] != ch)
            return false;
    return true;
}

bool col(int j, char &ch)
{
    ch = 'T';
    for (int i = 0; i < 4; ++i)
    {
        if (board[i][j] == '.')
            return false;
        if (board[i][j] == 'T')
            continue;
        ch = board[i][j];
        break;
    }

    for (int i = 0; i < 4; ++i)
        if (board[i][j] != 'T' && board[i][j] != ch)
            return false;
    return true;
}

bool dia1(char &ch)
{
    ch = 'T';
    for (int i = 0, j = 0; i < 4; ++i, ++j)
    {
        if (board[i][j] == '.')
            return false;
        if (board[i][j] == 'T')
            continue;
        ch = board[i][j];
        break;
    }

    for (int i = 0, j = 0; i < 4; ++i, ++j)
        if (board[i][j] != 'T' && board[i][j] != ch)
            return false;
    return true;
}

bool dia2(char &ch)
{
    ch = 'T';
    for (int i = 0, j = 3; i < 4; ++i, --j)
    {
        if (board[i][j] == '.')
            return false;
        if (board[i][j] == 'T')
            continue;
        ch = board[i][j];
        break;
    }

    for (int i = 0, j = 3; i < 4; ++i, --j)
        if (board[i][j] != 'T' && board[i][j] != ch)
            return false;
    return true;
}

bool have_empty()
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (board[i][j] == '.')
                return true;
    return false;
}

const char *solve()
{
    const char *o_won = "O won";
    const char *x_won = "X won";
    const char *draw = "Draw";
    const char *not_completed = "Game has not completed";
    char ch;

    for (int i = 0; i < 4; ++i)
    {
        if (row(i, ch))
        {
            assert(ch == 'O' || ch == 'X');
            if (ch == 'O')
                return o_won;
            else
                return x_won;
        }
    }

    for (int j = 0; j < 4; ++j)
    {
        if (col(j, ch))
        {
            assert(ch == 'O' || ch == 'X');
            if (ch == 'O')
                return o_won;
            else
                return x_won;
        }
    }

    if (dia1(ch))
    {
        assert(ch == 'O' || ch == 'X');
        if (ch == 'O')
            return o_won;
        else
            return x_won;
    }

    if (dia2(ch))
    {
        assert(ch == 'O' || ch == 'X');
        if (ch == 'O')
            return o_won;
        else
            return x_won;
    }

    if (have_empty())
        return not_completed;
    else
        return draw;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        for (int i = 0; i < 4; ++i)
            scanf("%s", board[i]);
        const char *ans = solve();
        printf("Case #%d: %s\n", tc, ans);
    }
}
