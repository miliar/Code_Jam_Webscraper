#include <iostream>
#include <sstream>
#include <string.h>
#include <stdio.h>
#include <math.h>

using namespace std;

//#define MY_DEBUG

char board[4][4];
int X_count[3][4];
int O_count[3][4];
int dot_num = 0;

enum RESULT
{
    X_WIN = 1,
    O_WIN = 2,
    DRAW = 3,
    NOT_END = 4,   
};

void debugXOcount()
{
    for (int i=0; i<3; i++)
    {
        for (int j=0; j<4; j++)
        {
            printf("=> X_count[%d][%d]=%d\n", i, j, X_count[i][j]);
            printf("=> O_count[%d][%d]=%d\n", i, j, O_count[i][j]);
        }
    }
}

char * result(int i)
{
    switch (i)
    {
        case X_WIN:
            return (char*)"X won";
        case O_WIN:
            return (char*)"O won";
        case DRAW:
            return (char*)"Draw";
        case NOT_END:
            return (char*)"Game has not completed";
    }
    return (char*)"";
}

int check_result()
{
    for (int i=0; i<3; i++)
    {
        for (int j=0; j<4; j++)
        {
            if (X_count[i][j] == 4)
                return X_WIN;
            if (O_count[i][j] == 4)
                return O_WIN;
        }
    }
    if (dot_num > 0)
        return NOT_END;
    return DRAW;
}

int main(void)
{
    int T=0, loop=0, r=0;

    cin >> T;
    
#ifdef MY_DEBUG
    printf("=> T=%d\n", T);
#endif

    while (++loop <= T)
    {
        memset(board, 0, sizeof(board));
        memset(X_count, 0, sizeof(X_count));
        memset(O_count, 0, sizeof(O_count));
        dot_num = 0;
        
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                cin >> board[i][j];
                if (board[i][j] == '.')
                    dot_num++;
            }
        }

#ifdef MY_DEBUG
        printf("=> Case #%d\n", loop);
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
                printf("=> %c", board[i][j]);
            printf("\n");
        }
#endif

        // check horizontal
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                if (board[i][j] == 'X' || board[i][j] == 'T')
                    X_count[0][i]++;
                if (board[i][j] == 'O' || board[i][j] == 'T')
                    O_count[0][i]++;
            }
        }
#ifdef MY_DEBUG
        printf("=> check horizontal\n");
        debugXOcount();
#endif
        r = check_result();
        if (r != NOT_END && r != DRAW)
        {
            printf("Case #%d: %s\n", loop, result(r));
            continue;
        }

        // check vertical
        for (int j=0; j<4; j++)
        {
            for (int i=0; i<4; i++)
            {
                if (board[i][j] == 'X' || board[i][j] == 'T')
                    X_count[1][j]++;
                if (board[i][j] == 'O' || board[i][j] == 'T')
                    O_count[1][j]++;
            }
        }
#ifdef MY_DEBUG
        printf("=> check vertical\n");
        debugXOcount();
#endif
        r = check_result();
        if (r != NOT_END && r != DRAW)
        {
            printf("Case #%d: %s\n", loop, result(r));
            continue;
        }
        
        // check diagonal
        for (int i=0; i<4; i++)
        {
            if (board[i][i] == 'X' || board[i][i] == 'T')
                X_count[2][0]++;
            if (board[i][i] == 'O' || board[i][i] == 'T')
                O_count[2][0]++;
                
            if (board[i][3-i] == 'X' || board[i][3-i] == 'T')
                X_count[2][1]++;
            if (board[i][3-i] == 'O' || board[i][3-i] == 'T')
                O_count[2][1]++;
        }
#ifdef MY_DEBUG
        printf("=> check diagonal\n");
        debugXOcount();
#endif
        r = check_result();
        printf("Case #%d: %s\n", loop, result(r));
    }

    return 0;
}
