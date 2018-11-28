#include <stdio.h>

bool ended(char * board);
bool xwon(char * board);
bool owon(char * board);

int main()
{
    int t;
    char board[16];
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        scanf("%s %s %s %s", board, board+4, board+8, board+12);
        printf("Case #%d: ", i+1);
        if (xwon(board))
        {
            printf("X won\n");
        } else if (owon(board)) {
            printf("O won\n");
        } else if (ended(board)) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }
    }
    return 0;
}

bool ended(char * board)
{
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[4*i+j] == '.') 
            {
                return false;
            }
        }
    }
    return true;
}

bool xwon(char * board)
{
    bool fail = false;
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[4*i+j] == '.' || board[4*i+j] == 'O')
            {
                fail = true;
            }
        }
        if (!fail)
        {
            return true;
        } else {
            fail = false;
        }
    }
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[4*j+i] == '.' || board[4*j+i] == 'O')
            {
                fail = true;
            }
        }
        if (!fail)
        {
            return true;
        } else {
            fail = false;
        }
    }
    for (int i = 0; i < 4; ++i)
    {
        if (board[5*i] == '.' || board[5*i] == 'O')
        {
            fail = true;
        }
    }
    if (!fail)
    {
        return true;
    } else {
        fail = false;
    }
    for (int i = 1; i < 5; ++i)
    {
        if (board[3*i] == '.' || board[3*i] == 'O')
        {
            fail = true;
        }
    }
    if (!fail)
    {
        return true;
    } else {
        fail = false;
    }
    return false;
}

bool owon(char * board)
{
    bool fail = false;
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[4*i+j] == '.' || board[4*i+j] == 'X')
            {
                fail = true;
            }
        }
        if (!fail)
        {
            return true;
        } else {
            fail = false;
        }
    }
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[4*j+i] == '.' || board[4*j+i] == 'X')
            {
                fail = true;
            }
        }
        if (!fail)
        {
            return true;
        } else {
            fail = false;
        }
    }
    for (int i = 0; i < 4; ++i)
    {
        if (board[5*i] == '.' || board[5*i] == 'X')
        {
            fail = true;
        }
    }
    if (!fail)
    {
        return true;
    } else {
        fail = false;
    }
    for (int i = 1; i < 5; ++i)
    {
        if (board[3*i] == '.' || board[3*i] == 'X')
        {
            fail = true;
        }
    }
    if (!fail)
    {
        return true;
    } else {
        fail = false;
    }
    return false;
}
